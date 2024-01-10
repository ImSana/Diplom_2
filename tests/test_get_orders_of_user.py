import allure
from data import MessageText, StatusCode
from urls import ENDPOINTS, URL
from api.api_check_methods import CheckMethods
from api.api_base_methods import BaseMethods


@allure.feature("Проверка получения заказа пользователя")
class TestGetOrder:
    @allure.title("Проверка заказа авторизованного пользователя")
    @allure.description("Запрос от существующего пользователя"
                        "статус ответа (200) и текста ответа (True)")
    def test_get_order_not_authorized_user(self, create_user_for_del, create_order):
        response = BaseMethods.get_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER,
                                              token=create_user_for_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка получения ошибки при заказе не авторизованного пользователя")
    @allure.description("Запрос от неавторизованного пользователя, статус ответа (401) и текста ответа 'You "
                        "should be authorised'")
    def test_get_order_of_unauthorized_user(self, create_user_for_del, create_order):
        response = BaseMethods.get_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.NOT_AUTHORIZET)
