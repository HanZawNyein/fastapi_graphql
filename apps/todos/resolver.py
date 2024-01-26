import strawberry
from typing import List
from .types import User

# In-memory database for demonstration purposes
db = [
    User(id=1, name="Patrick", age=100),
    User(id=2, name="John", age=30),
    User(id=3, name="Alice", age=25),
]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, user_id: int) -> User:
        # Read operation - retrieve a user by id
        for user in db:
            if user.id == user_id:
                return user
        return None

    @strawberry.field
    def users(self) -> List[User]:
        # Read operation - retrieve all users
        return db

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, age: int) -> User:
        # Create operation - add a new user
        new_user = User(id=len(db) + 1, name=name, age=age)
        db.append(new_user)
        return new_user

    @strawberry.mutation
    def update_user(self, user_id: int, name: str, age: int) -> User:
        # Update operation - modify user details by id
        for user in db:
            if user.id == user_id:
                user.name = name
                user.age = age
                return user
        return None

    @strawberry.mutation
    def delete_user(self, user_id: int) -> User:
        # Delete operation - remove a user by id
        for user in db:
            if user.id == user_id:
                db.remove(user)
                return user
        return None