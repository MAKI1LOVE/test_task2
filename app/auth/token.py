from jose import jwt

from config import settings

algorithm = 'HS256'
secret = settings.SECRET


def create_token(uuid: str) -> str:
    token = jwt.encode({'uuid': uuid}, key=secret, algorithm=algorithm)
    return token


def verify_token(token: str, uuid: str) -> bool:
    try:
        data = jwt.decode(token, key=secret, algorithms=algorithm)
        return data['uuid'] == uuid
    except jwt.JWTError as e:
        print(e)
        return False
