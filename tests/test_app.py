from http import HTTPStatus


def test_response(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá NF!', "age": 28}


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            "username": "nf",
            "email": "email@.com",
            "password": "123"
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "nf",
        "email": "email@.com"
    }


def test_list_users(client):

    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [{'id': 1, 'username': 'nf', 'email': 'email@.com'}]}


def test_get_user(client):

    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'id': 1, 'username': 'nf', 'email': 'email@.com'}


def test_get_user_not_found(client):

    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Item not found'}


def test_update_user(client):

    response = client.put(
        '/users/1',
        json={
            "username": "updated_name",
            "email": "updated@email.com",
            "password": "123"
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "updated_name",
        "email": "updated@email.com"
    }
