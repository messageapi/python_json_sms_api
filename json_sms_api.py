# coding=utf-8
"""
# пример

from json_sms_api import JsonSmsApi


access_point = 'http://message-api.com'
login = 'username'
password = 'password'


api = JsonSmsApi(access_point, login, password)

print api.get_balance()
print api.get_senders()

messages = [
    {
        "clientId": "1",
        "phone": "71234567890",
        "text": "first message",
        "sender": "TEST"
    },
    {
        "clientId": "2",
        "phone": "71234567891",
        "text": "second message",
        "sender": "TEST",
    },
    {
        "clientId": "3",
        "phone": "71234567892",
        "text": "third message",
        "sender": "TEST",
    }
]

# отправляем сообщения
print api.send_messages(messages, 'testQueue')

# получаем статусы для пакета сообщений
messages = [{"clientId": "1", "smscId": 11255142}, {"clientId": "2", "smscId": 11255143}, {"clientId": "3", "smscId": 11255144}]
print api.check_statuses(messages)

# получаем статусы из очереди 'testQueue'
print api.check_status_queue('testQueue', 10)

"""

import urllib
import json


class JsonSmsApi:
    def __init__(self, access_point, api_login, api_password):
        self.access_point = access_point
        self.login = api_login
        self.password = api_password

    def _send_request(self, uri, params=None):
        if not params:
            params = {}
        url = self._get_url(uri)
        data = self._form_packet(params)
        try:
            f = urllib.urlopen(url, data)
            result = f.read()
            return eval(result)
        except IOError, e:
            return dir(e)

    def _get_url(self, uri):
        return "%s/messages/v2/%s.json" % (self.access_point, uri)

    def _form_packet(self, params=None):
        if not params:
            params = {}
        params["login"] = self.login
        params["password"] = self.password
        for key, value in params.items():
            if value is None:
                del params[key]
        packet = json.dumps(params)
        return packet

    def send_messages(self, messages, check_status_queueName=None, scheduleTime=None):
        params = {
            'messages': messages,
            'check_status_queueName': check_status_queueName,
            'scheduleTime': scheduleTime,
        }
        return self._send_request('send', params)

    def check_statuses(self, messages):
        params = {"messages": messages}
        return self._send_request('status', params)

    def check_status_queue(self, check_status_queueName, limit=5):
        params = {'check_status_queueName': check_status_queueName, 'check_status_queueLimit': limit}
        return self._send_request('check_status_queue', params)

    def get_balance(self):
        return self._send_request('balance')

    def get_senders(self):
        return self._send_request('senders')

