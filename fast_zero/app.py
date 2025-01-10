from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserEntity, UserList, UserResponse, UserSchema

app = FastAPI()

db = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá NF!', "age": 28}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserResponse)
def create_user(user: UserSchema):

    user_with_id = UserEntity(**user.model_dump(), id=len(db) + 1)

    db.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def list_users():
    return {'users': db}


@app.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id: int):

    if user_id < 1 or user_id > len(db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")

    founded_user = None

    for user in db:
        if user.id == user_id:
            founded_user = user
            break

    return founded_user


@app.put('/users/{user_id}', response_model=UserResponse)
def update_user(user_id: int, user: UserSchema):

    if user_id < 1 or user_id > len(db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")

    new_user = UserEntity(**user.model_dump(), id=user_id)
    db[user_id - 1] = new_user

    return new_user

@app.delete('/users/{user_id}', response_model=UserResponse)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")

    deleted_user = db.pop(user_id - 1)

    return deleted_user