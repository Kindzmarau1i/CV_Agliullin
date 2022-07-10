from Automation_API.lib.Assertions import Assertions
from Automation_API.lib.Requests import Requests


class Tests:
    def test_01(self):
        """ DELETE /users (указать все обязательные параметры) """
        response = Requests.delete("users/2")
        Assertions.check_status_code(response, 204)

    def test_02(self):
        """ DELETE /users (не указать id пользователя) """
        # Если не указать id, то удалятся все пользователи
        response = Requests.delete("users")
        Assertions.check_status_code(response, 204)

    def test_03(self):
        """ DELETE /users (указать несуществующий id пользователя) """
        response = Requests.delete("users/14")
        ExpectedResponse = '{"error":400,"errorMessage":"BAD_REQUEST"}'
        Assertions.check_status_code(response, 400)
        Assertions.check_json_schema(response, ExpectedResponse)

    def test_04(self):
        """ DELETE /users (указать несколько id через запятую) """
        # Если указать id конкретных пользователей через запятую, то они удалятся
        response = Requests.delete("users/2,3,4")
        Assertions.check_status_code(response, 204)

    def test_05(self):
        """ DELETE /users (указать несколько id через обратный слэш) """
        response = Requests.delete("users/2/3/4")
        Assertions.check_status_code(response, 404)
        ExpectedResponse = '{"error":404,"errorMessage":"NOT_FOUND"}'
        Assertions.check_json_schema(response, ExpectedResponse)

    def test_06(self):
        """ DELETE /users (указать id одного пользователя несколько раз """
        # Ошибки не будет, можно вызывать бесконечное количетсво раз
        Requests.delete("users/2")
        Requests.delete("users/2")
        response = Requests.delete("users/2")
        Assertions.check_status_code(response, 204)

    def test_07(self):
        """ DELETE /users (указать вместо id текст) """
        response = Requests.delete("users/two")
        ExpectedResponse = '{"error":400,"errorMessage":"BAD_REQUEST"}'
        Assertions.check_status_code(response, 400)
        Assertions.check_json_schema(response, ExpectedResponse)

    def test_08(self):
        """ DELETE /users (указать вместо id спецсимволы) """
        response = Requests.delete("users/!№%")
        ExpectedResponse = '{"error":400,"errorMessage":"BAD_REQUEST"}'
        Assertions.check_status_code(response, 400)
        Assertions.check_json_schema(response, ExpectedResponse)

    def test_09(self):
        """ DELETE /users (указать вместо id пробел) """
        response = Requests.delete("users/ ")
        ExpectedResponse = '{"error":400,"errorMessage":"BAD_REQUEST"}'
        Assertions.check_status_code(response, 400)
        Assertions.check_json_schema(response, ExpectedResponse)

    def test_10(self):
        """ DELETE /users (указать вместо id некорректный тип данных) """
        response = Requests.delete("users/'2'")
        ExpectedResponse = '{"error":400,"errorMessage":"BAD_REQUEST"}'
        Assertions.check_status_code(response, 400)
        Assertions.check_json_schema(response, ExpectedResponse)
