import pytest
import allure
from data import MessageText, UserData, StatusCode
from urls import ENDPOINTS, URL
from api.api_check_methods import CheckMethods
from api.api_base_methods import BaseMethods


@allure.feature("Проверка входа в систему")
class TestAuthorizedUser:
    @allure.title("Проверка успешного входа в систему")
    @allure.description("Запрос с корректными email и паролем,статус ответа (200)"
                        "ответ 'True'")
    def test_authorized_success(self, create_user_for_del):
        user_data = {"email": create_user_for_del[0]["email"],
                     "password": create_user_for_del[0]["password"]}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.LOGIN_USER, user_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка получения ошибки авторизации с некорректным логином/паролем")
    @allure.description("Запросы с корректным email и некорректными паролем"
                        "email и корректным паролем, ожидаем ошибку 401 и текст ответа "
                        "'email or password are incorrect'")
    @pytest.mark.parametrize("email, password", [(UserData.EMAIL, UserData.ERROR_PASSWORD),
                                                 (UserData.ERROR_EMAIL, UserData.PASSWORD)],
                             ids=['ERROR_PASSWORD', 'ERROR_EMAIL'])
    def test_authorized_error_data(self, email, password):
        user_data = {"email": email,
                     "password": password}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.LOGIN_USER, user_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.INVALID_DATA)
