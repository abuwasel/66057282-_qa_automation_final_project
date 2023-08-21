import requests
import concurrent.futures

url = "https://api.dictionaryapi.dev/api/v2/entries/en/word"
def send_request(url):
    res = requests.get(url)
    return res

def rate_limiting():
    num_requests = 500
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request, url) for i in range(num_requests)]

    for future in concurrent.futures.as_completed(futures):
        res = future.result()
        if res.status_code == 429:
            print(f'Status Code 429 - {res.text}')
            break


rate_limiting()
