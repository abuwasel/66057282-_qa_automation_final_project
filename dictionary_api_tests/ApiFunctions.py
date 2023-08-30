import requests
import time

def get_data(url, word, lang='en'):
    try:
        url = f'{url}/{lang}/{word}'
        res = requests.get(url)
        if res.status_code < 400:
            data = res.json()
            return data
        elif res.status_code == 429:
            res.status_code
        else:
            return res.status_code
    except ConnectionError as e:
        return 'ConnectionError'


def get_status_code(url, word, lang='en'):
    url = f'{url}/{lang}/{word}'
    res = requests.get(url)
    return res.status_code


def check_special_chars(url, word, lang='en'):
    url = f'{url}/{lang}/{word}'
    res = requests.get(url)
    return 'program' in res.text and res.status_code < 400

