import requests
import concurrent.futures

class RateLimiting:
    def __init__(self):
        self.url_rate = "https://api.dictionaryapi.dev/api/v2/entries/en/word"

    def send_request(self):
        response = requests.get(self.url_rate)
        return response

    def rate_limiting(self):
        num_requests = 500
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.send_request) for _ in range(num_requests)]

        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            if response.status_code == 429:
                #print(f'Status Code 429 - {response.text}')
                return response.status_code
                break


# rate_limiter = RateLimiting()
# rate_limiter.rate_limiting()

