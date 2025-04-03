import graphene
from graphene_django.types import DjangoObjectType
from .models import Profile

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        

class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)

    def resolve_profiles(self, info):
        return Profile.objects.all()

schema = graphene.Schema(query=Query)