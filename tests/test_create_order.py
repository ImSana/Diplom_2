from data import MessageText, Order, StatusCode
from urls import ENDPOINTS, URL
import pytest
import allure
from api.api_check_methods import CheckMethods
from api.api_base_methods import BaseMethods


@allure.feature("Проверка создания заказа")
class TestCreateOrder:
    @allure.title("Проверка создания заказа авторизированных пользователей")
    @allure.description("Запросы авторизованного пользователя с ингредиентами и без ингредиентов, "
                        "ожидаем ответ 200 / ошибку 400 текста ответа 'True' / 'False'")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, StatusCode.CODE_200, MessageText.SUCCESS_OPERATION),
                              (Order.INGREDIENTS_EMPTY, StatusCode.CODE_400, MessageText.FALSE_OPERATION)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_authorized_no_ingredients(self, create_user_for_del, ingredients, status_code, text_answer):
        order_payment = {"ingredients": ingredients}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, order_payment,
                                               create_user_for_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, text_answer)

    @allure.title("Проверка создания заказа не авторизированного пользователя с ингредиентами и без ингредиентов")
    @allure.description("Запросы не авторизованного пользователя c ингредиентами и без ингредиентов, "
                        "ожидаем ответ 200 / ошибку 400 текст ответа 'True' / 'False'")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, StatusCode.CODE_200, MessageText.SUCCESS_OPERATION),
                              (Order.INGREDIENTS_EMPTY, StatusCode.CODE_400, MessageText.FALSE_OPERATION)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_unauthorized_no_ingredients(self, create_user_for_del, ingredients, status_code, text_answer):
        order_payment = {"ingredients": ingredients}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, order_payment)
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, text_answer)

    @allure.title("Проверка создания заказа авторизированного пользователя с неправильным ингредиентом")
    @allure.description("Запрос с авторизацией с несуществующим ингредиентом, ожидаем ошибку "
                        "500, текст ответа 'Internal Server Error'")
    def test_create_order_authorized_ingredients_error(self, create_user_for_del):
        order_payment = {"ingredients": Order.INGREDIENTS_ERROR}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, order_payment,
                                               create_user_for_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, StatusCode.CODE_500)
        CheckMethods.check_message_text(response, MessageText.SERVER_ERROR)

    @allure.title("Проверка создания заказа для не авторизированного пользователя с неправильным игредиентом")
    @allure.description("Запрос не авторизованного пользователя с несуществующим ингредиентом, ожидаем ошибку "
                        "500, текст ответа 'Internal Server Error'")
    def test_create_order_unauthorized_ingredients_error(self, create_user_for_del):
        order_payment = {"ingredients": Order.INGREDIENTS_ERROR}
        response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, order_payment)
        CheckMethods.check_status_code(response, StatusCode.CODE_500)
        CheckMethods.check_message_text(response, MessageText.SERVER_ERROR)
