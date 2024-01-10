import pytest
from urls import ENDPOINTS, URL
from data import Order
from creat_user import GenerateUser
from api.api_base_methods import BaseMethods


@pytest.fixture
def create_user_for_del():
    user_data = GenerateUser.creat_user()
    response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_USER, user_data)
    yield user_data, response
    BaseMethods.del_request(URL.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO,
                                  response.json()['accessToken'])


@pytest.fixture
def create_order(create_user_for_del):
    order_payment = {"ingredients": Order.INGREDIENTS}
    response = BaseMethods.post_request(URL.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, order_payment,
                                                 create_user_for_del[1].json()['accessToken'])
    return response
