from django.test import TestCase

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from .models import Project, ToDo
from .views import ToDoModelViewSet, ProjectModelViewSet
from users.models import User


class TestToDoProjectViewSet(TestCase):
    def setUp(self):
        self.todos_link = '/api/todos/'
        self.projects_link = '/api/projects/'
        self.root = User.objects.create_superuser('root', 'root@a.com', '1')
        self.test_data_project = {'name': 'Test', ' repo': 'https://github.com/ssid11/DRF/',
                                  "devops": [1]}
        self.test_data_project_update = mixer.blend(Project)

    def test_get_list_todos(self):
        factory = APIRequestFactory()
        request = factory.get(self.todos_link)
        view = ToDoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_projects(self):
        factory = APIRequestFactory()
        request = factory.get(self.projects_link)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_project(self):
        factory = APIRequestFactory()
        data = {'name': 'Nev project', 'repo':'https://github.com/ssid11/DRF/', 'devops':[1]}
        request = factory.post(f'{self.projects_link}', data, format='json')
        force_authenticate(request, self.root)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_todos_list(self):
        todo = mixer.blend(ToDo)
        client = APIClient()
        response = client.get(f'{self.todos_link}{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_client_todo_put_noauth(self):
        todo = mixer.blend(ToDo)
        client = APIClient()
        response = client.put(f'{self.todos_link}{todo.id}/', {"text": 'Access denied'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_client_create_project(self):
        client = APIClient()
        client.login(username='root', password='1')
        response = client.post(self.projects_link, self.test_data_project)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_delete_project(self):
        client = APIClient()
        client.login(username='root', password='1')
        project = Project.objects.create(name='Delete test', repo='http:localhost/')
        response = client.delete(f'{self.projects_link}{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self) -> None:
        pass


class TestToDoProjectAPITestCase(APITestCase):
    def setUp(self):
        self.todos_link = '/api/todos/'
        self.projects_link = '/api/projects/'
        User.objects.create_superuser('root', 'root@a.com', '1')
        self.test_data_project = {'name': 'Test', ' repo': 'https://github.com/ssid11/DRF/',
                                  "devops": [1]}

    def test_get_list_todos(self):
        response = self.client.get(self.todos_link)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        self.client.login(username='root', password='1')
        response = self.client.post(self.projects_link, self.test_data_project)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self) -> None:
        pass
