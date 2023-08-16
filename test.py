import requests

base_url = 'http://127.0.0.1:5000'


def successful_create_user():
    url = f'{base_url}/create_user'
    data = {'username': 'john_doe', 'email': 'test.email@example.com'}
    response = requests.post(url, json=data)
    assert response.json() == {'message': 'User created successfully'}


def failed_create_user():
    url = f'{base_url}/create_user'
    data = {'username': 'john_doe1'}
    response = requests.post(url, json=data)
    assert response.json() == {'message': 'Missing username or email'}


def successful_get_user():
    username = 'john_doe'
    url = f'{base_url}/get_user/{username}'
    response = requests.get(url)
    assert response.json() == {'email': 'test.email@example.com', 'username': 'john_doe'}


def failed_get_user():
    username = 'john_doe1'
    url = f'{base_url}/get_user/{username}'
    response = requests.get(url)
    assert response.json() == {'message': 'User not found'}


def successful_update_user():
    username = 'john_doe'
    email = 'email@example.com'
    url = f'{base_url}/update_user/{username}'
    data = {'email': email}
    response = requests.put(url, json=data)
    assert response.json() == {'message': "User's email updated successfully"}


def failed_update_user():
    username = 'john_doe1'
    email = 'email1@example.com'
    url = f'{base_url}/update_user/{username}'
    data = {'email': email}
    response = requests.put(url, json=data)
    assert response.json() == {'message': 'User not found'}


def successful_delete_user():
    username = 'john_doe'
    url = f'{base_url}/delete_user/{username}'
    response = requests.delete(url)
    assert response.json() == {'message': 'User deleted successfully'}


def failed_delete_user():
    username = 'john_doe1'
    url = f'{base_url}/delete_user/{username}'
    response = requests.delete(url)
    assert response.json() == {'message': 'User not found'}


if __name__ == "__main__":
    successful_create_user()
    failed_create_user()
    successful_get_user()
    failed_get_user()
    successful_update_user()
    failed_update_user()
    successful_delete_user()
    failed_delete_user()
