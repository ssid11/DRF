"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('todos', ToDoModelViewSet)
router.register('projects', ProjectModelViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="ToDo List",
      default_version='0.1',
      description="Documentation to ToDo List project",
      contact=openapi.Contact(email="a@b.com"),
      license=openapi.License(name="GP License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/<str:version>/users/', UserModelViewSet()),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserModelViewSet.as_view),
    # path('api/users/0.2/', UserModelViewSet.as_view(), namespace='0.2'),
    #  path('api/users/0.1/', UserModelViewSet.as_view(), namespace='0.1'),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui()),
    path('swagger/<str:format>/', schema_view.without_ui() ),
    # path('redoc/', schema_view.without_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', schema_view.with_ui('redoc')),
]
