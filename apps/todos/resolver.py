import strawberry
from .types import User


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

    @strawberry.field
    def users(self) -> list[User]:
        return [User(name="Patrick", age=100)]
