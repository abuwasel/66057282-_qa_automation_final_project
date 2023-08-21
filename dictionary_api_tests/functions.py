import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import concurrent.futures

url = 'https://api.dictionaryapi.dev/api/v2/entries/'
def get_data(url, word, lang='en'):
    try:
        if word != '':
            url = f'{url}{lang}/{word}'
            res = requests.get(url)
            if res.status_code < 400:
                data = res.json()
                return data
            elif res.status_code == 429:
                print(f'Status Code 429 - {res.text}')
            else:
                return 'No Definitions Found.'
        else:
            return 'The input value is empty.'
    except ConnectionError as e:
        return 'Remote end closed connection without response'


def get_status_code(url, word, lang='en'):
    url = f'{url}{lang}/{word}'
    res = requests.get(url)
    return res.status_code
