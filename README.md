## Json SMS API

```
# примеры

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
```
