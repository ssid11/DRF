import graphene
from graphene import String, Int, List, ID
from graphene_django import DjangoObjectType

from todoapp.models import ToDo, Project
from users.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_ToDo = graphene.List(ToDoType)
    all_project = graphene.List(ProjectType)
    all_user = graphene.List(UserType)
    ToDo_by_user = graphene.List(ToDoType, user=String(required=True))
    ToDo_delete = graphene.List(ToDoType, id=Int(required=True))

    def resolve_all_ToDo(root, info):
        return ToDo.objects.all()

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_all_user(root, info):
        return User.objects.all()

    def resolve_ToDo_by_user(self, info, user):
        user_id=User.objects.get(username=user).id
        try:
            return ToDo.objects.filter(author=user_id)
        except User.DoesNotExist:
            return None

    def resolve_ToDo_delete(self, info, id):
        try:
            ToDo.objects.get(id=id).delete()
        except ToDo.DoesNotExist:
            pass
        return ToDo.objects.all()


class ProjectMutation(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        repo = String(required=True)
        devops = List(String)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, repo, devops):
        project = Project.objects.create(name=name, repo=repo)
        project.authors.set(devops)
        return ProjectMutation(project=project)


class ToDoMutation(graphene.Mutation):
    class Arguments:
        id = ID()
        text = String()
        project = String()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, id, text=None, project=None):
        todo = ToDo.objects.get(id=id)
        if text:
            todo.text = text
        if project:
            todo.project = project
        todo.save()
        return ToDoMutation(todo=ToDo)


class Mutation(graphene.ObjectType):
    project_create = ProjectMutation.Field()
    ToDo_update = ToDoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
