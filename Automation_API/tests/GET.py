from Automation_API.lib.Assertions import Assertions
from Automation_API.lib.Requests import Requests


class Tests:
    def test_01(self):
        """ GET /users (указать все обязательные параметры) """
        response = Requests.get("users/2")
        ExpectedKeys1 = ['data', 'support']
        ExpectedKeys2 = ['id', 'email', 'first_name', 'last_name', 'avatar']
        ExpectedKeys3 = ['url', 'text']
        Assertions.check_status_code(response, 200)
        Assertions.json_has_keys(response, expected_keys=ExpectedKeys1)
        Assertions.json_has_keys(response, "data", expected_keys=ExpectedKeys2)
        Assertions.json_has_keys(response, "support", expected_keys=ExpectedKeys3)

    def test_02(self):
        pass
