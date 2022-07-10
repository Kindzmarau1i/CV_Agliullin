import requests
from Automation_API.lib.Logger import Logger


class Requests:
    @staticmethod
    def get(url: str, data: str or dict = None, headers: dict = None, cookies: dict = None):
        return Requests._send(url, data, headers, cookies, "GET")

    @staticmethod
    def post(url: str, data: str or dict = None, headers: dict = None, cookies: dict = None):
        return Requests._send(url, data, headers, cookies, "POST")

    @staticmethod
    def put(url: str, data: str or dict = None, headers: dict = None, cookies: dict = None):
        return Requests._send(url, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, data: str or dict = None, headers: dict = None, cookies: dict = None):
        return Requests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, data: str or dict, headers: dict, cookies: dict, method: str):
        url = f"https://reqres.in/api/{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_requests(url, data, headers, cookies, method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received!")

        Logger.add_response(response)

        return response