# Typing schemas for hint

from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    age: int
