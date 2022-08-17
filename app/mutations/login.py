import graphene
from django.contrib.auth import authenticate
import asgiref
import channels

class Login(graphene.Mutation, name="LoginPayload"):  # type: ignore
    """Login mutation.

    Login implementation, following the Channels guide:
    https://channels.readthedocs.io/en/latest/topics/authentication.html
    """

    ok = graphene.Boolean(required=True)

    class Arguments:
        """Login request arguments."""

        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        """Login request."""

        # Ask Django to authenticate user.
        user = authenticate(username=username, password=password)
        if user is None:
            return Login(ok=False)

        # Use Channels to login, in other words to put proper data to
        # the session stored in the scope. The `info.context` is
        # practically just a wrapper around Channel `self.scope`, but
        # the `login` method requires dict, so use `_asdict`.
        asgiref.sync.async_to_sync(channels.auth.login)(info.context._asdict(), user)
        # Save the session, `channels.auth.login` does not do this.
        info.context.session.save()

        return Login(ok=True)
