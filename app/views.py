# -------------------------------------------------------------------- URL CONFIGURATION
import pathlib
from django.http.response import HttpResponse
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import (
#     authentication_classes,
#     permission_classes,
#     api_view,
# )
from graphene_django.views import GraphQLView
from graphene import Schema
from app.mutation import Mutation
from app.query import Query
from app.subscription import Subscription


def graphql():
    GraphQLView.graphiql_template = "app/graphiql.html"
    view = GraphQLView.as_view(
        graphiql=True,
        schema=Schema(query=Query, mutation=Mutation, subscription=Subscription),
    )
    # view = permission_classes((IsAuthenticated,))(view)
    # view = authentication_classes(
    #     (
    #         SessionAuthentication,
    #         TokenAuthentication,
    #     )
    # )(view)
    # view = api_view(["GET", "POST"])(view)
    return view
