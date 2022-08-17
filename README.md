# spreadly-api

This is the api for the spreadly decentralized exchange. This 

## GraphQL

GraphQL takes a different approach to client-server architecture when compared to the REST structure. The two major concepts for GraphQL are queries & mutations. Queries allow for flexible data fetching, while mutations allow you to create, update, and delete objects with defined logic. 

### GraphQL queries in websockets

Using django-channels-graphql-ws (https://github.com/datadvance/DjangoChannelsGraphqlWs), which utilizes Django Channels v2 (https://github.com/django/channels) under the hood, we can connect to websockets whose return value will be the result of an inputted GraphQL query. This allows for all types of data to be live streamed to the client. This additional module is managed under the subscriptions.py file. 

## Structure

The major components are queries, mutations, subscriptions, and types.

In the graphql folder of the api module:
- views.py: provides view to display html, rendering interface.
- asgi.py: provides the entry point to the channels for django, along with middleware & a consumer class for the websockets (multithread for scaling).
- mutation.py: provides all of the valid mutations on django objects.
- query.py: provides all the django models valid in GraphQL.
- subscription.py: provides all of the websocket connections.
- /mutations/...:  Mutation objects that will provide custom logic for creating, updating, or deleting data.
- /types/...: Provides all of the graphene types that will be used to build queries, mutations, and subscriptions
- /subscriptions/...: All websocket subscriptions with custom logic declared for how to handle caching

## To Do

- Implement token auth, same logic as Paideia's... waiting on nautilus auth to come alive.
- redis server setup
- Watchdog & kafka integration for updating redis cache
