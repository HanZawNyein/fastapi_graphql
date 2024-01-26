import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from apps.todos.resolver import Query,Mutation
from strawberry.tools import merge_types

# ComboQuery = merge_types("apps", (Query,))

schema = strawberry.Schema(query=Query,mutation=Mutation)

graphql_app = GraphQL(schema, debug=True)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
