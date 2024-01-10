import allure


class CheckMethods:
    @staticmethod
    @allure.step("Проверка статуса ответа")
    def check_status_code(response, code):
        assert response.status_code == code, (f"Возвращенный статус ответа не соответствует. ОР: {code}, "
                                              f"ФР: {response.status_code}")

    @staticmethod
    @allure.step("Проверка ответа 'message'")
    def check_message_json(response, key, text):
        assert response.json()[key] == text, (f"Ответ не соответствует ожидаемому: {text}, "
                                              f"ФР: {response.json()[key]}")

    @staticmethod
    @allure.step("Проверка текста в ответе")
    def check_message_text(response, text):
        assert text in response.text, (f"Ответ не соответствует ожидаемому: {text}, "
                                       f"ФР: {response.text}")



