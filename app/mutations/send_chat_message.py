import graphene
from app.subscriptions.on_new_chat_message import OnNewChatMessage
# from app import asgi

chats = []

class SendChatMessage(graphene.Mutation, name="SendChatMessagePayload"):  # type: ignore
    """Send chat message."""

    ok = graphene.Boolean()

    class Arguments:
        """Mutation arguments."""

        chatroom = graphene.String()
        text = graphene.String()

    def mutate(self, info, chatroom, text):
        """Mutation "resolver" - store and broadcast a message."""

        # Use the username from the connection scope if authorized.
        username = (
            info.context.user.username
            if info.context.user.is_authenticated
            else "Anonymous"
        )

        # Store a message.
        chats[chatroom].append({"chatroom": chatroom, "text": text, "sender": username})

        # Notify subscribers.
        OnNewChatMessage.new_chat_message(chatroom=chatroom, text=text, sender=username)

        return SendChatMessage(ok=True)