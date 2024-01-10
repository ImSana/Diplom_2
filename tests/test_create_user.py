import pytest
import allure
from data import MessageText, StatusCode
from urls import ENDPOINTS, URL
from creat_user import GenerateUser
from api.api_check_methods import CheckMethods
from api.api_base_methods import BaseMethods


@allure.feature("Проверка ручки создания пользователя")
class TestCreateUser:
    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Запрос создания нового пользователя с валидными данными (наличие email/пароля/имени), "
                        "ожидаемый успешный статус ответа (200) и текста ответа (True)")
    def test_create_user_success_new_user(self):
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_USER,
                                               GenerateUser.creat_user())
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка получения ошибки при повторном создании уже существующего пользователя")
    @allure.description("Невалидный запрос на создание пользователя, который уже существует в системе, ожидаем ошибку "
                        "клиента (403) и текста ответа 'User already exists'")
    def test_create_user_user_already_exists_error(self, create_user_for_del):
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_USER,
                                               create_user_for_del[0])
        CheckMethods.check_status_code(response, StatusCode.CODE_403)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.USER_ALREADY_EXISTS)

    @allure.title("Проверка получения ошибки при создании пользователя без email/пароля/имени")
    @allure.description("Запрос создания нового пользователя с невалидными данными (без email/пароля/имени), "
                        "ожидаем ошибку клиента (403) и текста ответа 'Email, password and name are required fields'")
    @pytest.mark.parametrize('email, password, name',
                             [(GenerateUser.creat_user()['email'], GenerateUser.creat_user()['password'],
                               None),
                              (GenerateUser.creat_user()['email'], None, GenerateUser.creat_user()['name']),
                              (None, GenerateUser.creat_user()['password'],
                               GenerateUser.creat_user()['name'])],
                             ids=['without_email', 'without_password', 'without_name'])
    def test_create_user_required_field_error(self, email, password, name):
        payload_user_data = {"email": email,
                             "password": password,
                             "name": name}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_USER, payload_user_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_403)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.REQUIRED_FIELD)
