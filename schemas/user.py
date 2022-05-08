def userEntity(item) -> dict:
    return {
        "id": str(item['_id']),
        "email": item['email'],
        "username": item['username'],
        "password": item['password']
    }


def usersEntity(items) -> list:
    return [userEntity(item) for item in items]

