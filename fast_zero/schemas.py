from pydantic import BaseModel


class Message(BaseModel):

    message: str
    age: int


class UserSchema(BaseModel):

    username: str
    email: str
    password: str


class UserResponse(BaseModel):

    id: int
    username: str
    email: str


class UserEntity(UserSchema):

    id: int


class UserList(BaseModel):

    users: list[UserResponse]
