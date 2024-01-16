import pytest
import allure
from data import MessageText, UserData, StatusCode
from urls import ENDPOINTS, URL
from api.api_check_methods import CheckMethods
from api.api_base_methods import BaseMethods


@allure.feature("Проверка изменения пользователя")
class TestChangeUserData:
    @allure.title("Проверка успешного изменения данных пользователя")
    @allure.description("Запросы авторизованного пользователя на изменения данных, ожидаемый статус 200"
                        "ответ 'True'")
    @pytest.mark.parametrize('key_field, new_data', [("name", UserData.NEW_NAME),
                                                     ("password", UserData.NEW_PASSWORD),
                                                     ("email", UserData.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_data_user_success_new_data(self, create_user_for_del, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseMethods.patch_request(URL.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data,
                                                create_user_for_del[1].json()['accessToken'], )
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка получения ошибки изменения данных не авторизованного пользователя")
    @allure.description("Запросы не авторизованного пользователя на изменения данных, ожидаем ошибку со статусом 401"
                        "ответ 'You should be authorised'")
    @pytest.mark.parametrize('key_field, new_data', [("name", UserData.NEW_NAME),
                                                     ("password", UserData.NEW_PASSWORD),
                                                     ("email", UserData.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_error_change_user_data_not_authorized(self, create_user_for_del, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseMethods.patch_request(URL.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.NOT_AUTHORIZET)
