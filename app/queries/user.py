import graphene_django.types
from django.contrib.auth import get_user_model

class User(graphene_django.types.DjangoObjectType):
    """User model to show how to use 'info.context.user'."""

    class Meta:
        """Wrap Django user model."""

        model = get_user_model()