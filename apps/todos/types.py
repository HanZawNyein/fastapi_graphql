import strawberry
from typing import Optional
@strawberry.type
class User:
    id: int
    name: str
    age: int
