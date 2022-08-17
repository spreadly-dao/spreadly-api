
from app.subscriptions.on_new_chat_message import OnNewChatMessage
import graphene

class Subscription(graphene.ObjectType):
    """GraphQL subscriptions."""

    on_new_chat_message = OnNewChatMessage.Field()