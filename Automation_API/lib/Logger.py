from requests import Response
import datetime
import os


class Logger:
    FileName = "Automation_API/logs/log_" + str(datetime.datetime.now().strftime("%d.%m.%Y_%H-%M-%S")) + ".log"

    @classmethod
    def _WriteLogToFile(cls, data: str):
        with open(cls.FileName, 'a', encoding='utf-8') as LogFile:
            LogFile.write(data)

    @classmethod
    def add_requests(cls, url: str, data: str or dict, headers: dict, cookies: dict, method: str):
        TestName = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {TestName}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request text: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += f"\n"

        cls._WriteLogToFile(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        headers = dict(response.headers)
        cookies = dict(response.cookies)

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response headers: {headers}\n"
        data_to_add += f"Response cookies: {cookies}\n"
        data_to_add += f"\n-----\n"

        cls._WriteLogToFile(data_to_add)
