from django.contrib import admin


from .models import User

# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','email',)
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name', )

admin.site.register(User, MyUserAdmin)
# Register your models here.
