from dataclasses import dataclass
from creat_user import GenerateUser


@dataclass
class UserData:
    EMAIL: str = "bun@ya.ru"
    PASSWORD: str = "qwerty"
    ERROR_EMAIL: str = "buster2024@ya.ru"
    ERROR_PASSWORD: str = "ytrewq"
    NAME: str = "tim"
    NEW_NAME: str = GenerateUser.creat_user()["name"]
    NEW_EMAIL: str = GenerateUser.creat_user()["email"]
    NEW_PASSWORD: str = GenerateUser.creat_user()["password"]


class MessageText:
    SUCCESS_OPERATION = True
    FALSE_OPERATION = False
    SUCCESS_KEY = 'success'
    MESSAGE_KEY = 'message'
    USER_NAME_KEY = []
    SERVER_ERROR = "Internal Server Error"
    NOT_AUTHORIZET = "You should be authorised"
    USER_ALREADY_EXISTS = 'User already exists' 
    INVALID_DATA = "email or password are incorrect"
    REQUIRED_FIELD = "Email, password and name are required fields"


class Order:
    INGREDIENTS = ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    INGREDIENTS_ERROR = ["5555555555"]
    INGREDIENTS_EMPTY = ""

class StatusCode:
    CODE_200 = 200
    CODE_202 = 202
    CODE_400 = 400
    CODE_401 = 401
    CODE_403 = 403
    CODE_500 = 500