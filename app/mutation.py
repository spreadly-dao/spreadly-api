import graphene
from app.mutations.login import Login
from app.mutations.send_chat_message import SendChatMessage

class Mutation(graphene.ObjectType):
    """Root GraphQL mutation."""

    send_chat_message = SendChatMessage.Field()
    login = Login.Field()