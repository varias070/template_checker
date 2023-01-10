import requests

url = 'http://127.0.0.1:5001/get_form'
params = [
    {'phone': 79211002030, 'date': '2022-10-12', 'email': '123@yandex.ru', 'text': '413rqdqrrqrdwT24'},
    {'phone': 79211002030, 'email': '123@yandex.ru'},
    {'phone': 79211002030, 'date': '2022-10-12', 'message': '413rqdqrrqrdwT24'},
    {'f_1': '123@yandex.ru', 'f_2': '2022-10-12', 'f_3': '413rqdqrrqrdwT24'},
    {'phone': 79211002030, 'date': '2022-10-12'},
    {'date': '2022-10-12', 'text': '413rqdqrrqrdwT24'},
    {'text': '202sbsbsbsb', 'f_2': '413rqdqrrqrdwT24', 'f_3': 'wrgwrgwgwfwef'},
    {'f_1': '2022-10-12', 'f_2': '413rqdqrrqrdwT24'},
    {'f_1': '202sbsbsbsb', 'f_2': '413rqdqrrqrdwT24', 'f_3': 'wrgwrgwgwfwef'}
]

for param in params:
    response = requests.post(url, params=param)
    print(response.text)
