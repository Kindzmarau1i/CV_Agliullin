from Automation_API.lib.Assertions import Assertions
from Automation_API.lib.Requests import Requests


class Tests:
    """ POST /register (указать все обязательные параметры) """
    def test_01(self):
        response = Requests.post("register", data=f'{{"email": "eve.holt@reqres.in", "password": "pistol"}}',
                                headers={"Content-Type": "application/json"})
        ExpectedKeys = ['id', 'token']
        Assertions.check_status_code(response, 200)
        Assertions.json_has_keys(response, expected_keys=ExpectedKeys)

    def test_02(self):
        pass
