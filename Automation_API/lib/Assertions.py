from requests import Response
import json

class Assertions:
    @staticmethod
    def check_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Unexpected status code! Expect: '{expected_status_code}', Actual: '{response.status_code}'!"

    @staticmethod
    def json_has_key(response: Response, key1, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn`t JSON format!"

        if key2 is None:
            assert key1 in response.json(), f"There isn`t expected key '{key1}' in JSON!"
        elif key3 is None:
            assert key2 in response.json()[key1], f"There isn`t expected key '{key2}' in JSON!"
        elif key4 is None:
            assert key3 in response.json()[key1][key2], f"There isn`t expected key '{key3}' in JSON!"
        elif key5 is None:
            assert key4 in response.json()[key1][key2][key3], f"There isn`t expected key '{key4}' in JSON!"
        elif key6 is None:
            assert key5 in response.json()[key1][key2][key3][key4], f"There isn`t expected key '{key5}' in JSON!"
        elif key7 is None:
            assert key6 in response.json()[key1][key2][key3][key4][key5], f"There isn`t expected key '{key6}' in JSON!"
        elif key7 is not None:
            assert key7 in response.json()[key1][key2][key3][key4][key5][key6], f"There isn`t expected key '{key7}' in JSON!"

    @staticmethod
    def json_has_keys(response: Response, key1=None, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None, expected_keys: list = None):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn`t JSON format!"

        for c in expected_keys:
            if key1 is None:
                assert c in response.json(), f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key2 is None:
                assert c in response.json()[key1], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key3 is None:
                assert c in response.json()[key1][key2], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key4 is None:
                assert c in response.json()[key1][key2][key3], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key5 is None:
                assert c in response.json()[key1][key2][key3][key4], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key6 is None:
                assert c in response.json()[key1][key2][key3][key4][key5], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key7 is None:
                assert c in response.json()[key1][key2][key3][key4][key5][key6], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"
            elif key7 is not None:
                assert c in response.json()[key1][key2][key3][key4][key5][key6][key7], f"There isn`t one of the expected keys '{expected_keys}' in JSON!"

    @staticmethod
    def json_has_not_key(response: Response, key1, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn`t JSON format!"

        if key2 is None:
            assert key1 not in response.json(), f"There is unexpected key '{key1}' in JSON!"
        elif key3 is None:
            assert key2 not in response.json()[key1], f"There is unexpected key '{key2}' in JSON!"
        elif key4 is None:
            assert key3 not in response.json()[key1][key2], f"There is unexpected key '{key3}' in JSON!"
        elif key5 is None:
            assert key4 not in response.json()[key1][key2][key3], f"There is unexpected key '{key4}' in JSON!"
        elif key6 is None:
            assert key5 not in response.json()[key1][key2][key3][key4], f"There is unexpected key '{key5}' in JSON!"
        elif key7 is None:
            assert key6 not in response.json()[key1][key2][key3][key4][key5], f"There is unexpected key '{key6}' in JSON!"
        elif key7 is not None:
            assert key7 not in response.json()[key1][key2][key3][key4][key5][key6], f"There is unexpected key '{key7}' in JSON!"

    @staticmethod
    def json_has_not_keys(response: Response, key1=None, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None, unexpected_keys: list = None):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn`t JSON format!"

        for c in unexpected_keys:
            if key1 is None:
                assert c not in response.json(), f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key2 is None:
                assert c not in response.json()[key1], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key3 is None:
                assert c not in response.json()[key1][key2], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key4 is None:
                assert c not in response.json()[key1][key2][key3], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key5 is None:
                assert c not in response.json()[key1][key2][key3][key4], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key6 is None:
                assert c not in response.json()[key1][key2][key3][key4][key5], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key7 is None:
                assert c not in response.json()[key1][key2][key3][key4][key5][key6], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"
            elif key7 is not None:
                assert c not in response.json()[key1][key2][key3][key4][key5][key6][key7], f"There is one of the unexpected keys '{unexpected_keys}' in JSON!"

    @staticmethod
    def check_key_value(response: Response, key1, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None, value=None):
        if key2 is None:
            assert response.json()[key1] == value, f"Unexpected value of key '{key1}'! Expected: '{value}', Actual: '{response.json()[key1]}'!"
        elif key3 is None:
            assert response.json()[key1][key2] == value, f"Unexpected value of key '{key2}'! Expected: '{value}', Actual: '{response.json()[key1][key2]}'!"
        elif key4 is None:
            assert response.json()[key1][key2][key3] == value, f"Unexpected value of key '{key3}'! Expected: '{value}', Actual: '{response.json()[key1][key2][key3]}'!"
        elif key5 is None:
            assert response.json()[key1][key2][key3][key4] == value, f"Unexpected value of key '{key4}'! Expected: '{value}', Actual: '{response.json()[key1][key2][key3][key4]}'!"
        elif key6 is None:
            assert response.json()[key1][key2][key3][key4][key5] == value, f"Unexpected value of key '{key5}'! Expected: '{value}', Actual: '{response.json()[key1][key2][key3][key4][key5]}'!"
        elif key7 is None:
            assert response.json()[key1][key2][key3][key4][key5][key6] == value, f"Unexpected value of key '{key6}'! Expected: '{value}', Actual: '{response.json()[key1][key2][key3][key4][key5][key6]}'!"
        elif key7 is not None:
            assert response.json()[key1][key2][key3][key4][key5][key6][key7] == value, f"Unexpected value of key '{key7}'! Expected: '{value}', Actual: '{response.json()[key1][key2][key3][key4][key5][key6][key7]}'!"

    @staticmethod
    def check_json_schema(response: Response, expected_json):
        assert response.text == expected_json, f"Unexpected response JSON! Expect: '{expected_json}'. Actual: '{response.text}'!"

    @staticmethod
    def length(response: Response, key1=None, key2=None, key3=None, key4=None, key5=None, key6=None, key7=None, expected_length: int = None):
        if key1 is None:
            assert len(response.json()) == expected_length, f"Unexpected length! Expected '{expected_length}', Actual: '{len(response.json())}'."
        elif key2 is None:
            assert len(response.json()[key1]) == expected_length, f"Unexpected length of key '{key1}'! Expected '{expected_length}', Actual: '{len(response.json()[key1])}'."
        elif key3 is None:
            assert len(response.json()[key1][key2]) == expected_length, f"Unexpected length of key '{key2}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2])}'."
        elif key4 is None:
            assert len(response.json()[key1][key2][key3]) == expected_length, f"Unexpected length of key '{key3}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2][key3])}'."
        elif key5 is None:
            assert len(response.json()[key1][key2][key3][key4]) == expected_length, f"Unexpected length of key '{key4}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2][key3][key4])}'."
        elif key6 is None:
            assert len(response.json()[key1][key2][key3][key4][key5]) == expected_length, f"Unexpected length of key '{key5}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2][key3][key4][key5])}'."
        elif key7 is None:
            assert len(response.json()[key1][key2][key3][key4][key5][key6]) == expected_length, f"Unexpected length of key '{key6}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2][key3][key4][key5][key6])}'."
        elif key7 is not None:
            assert len(response.json()[key1][key2][key3][key4][key5][key6][key7]) == expected_length, f"Unexpected length of key '{key7}'! Expected '{expected_length}', Actual: '{len(response.json()[key1][key2][key3][key4][key5][key6][key7])}'."
