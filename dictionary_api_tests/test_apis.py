from ApiFunctions import *
from rate_limiting_function import *
import pytest

class TestAPIS_Ibrahim:
    @pytest.fixture()
    def url(self):
        return 'https://api.dictionaryapi.dev/api/v2/entries'

    def test_valid_word_lookup(self, url):
        word = "apple"
        actual_data = get_data(url, word)[0]['meanings'][0]['definitions'][0]['definition']
        assert actual_data is not None, 'Invalid response data'

    def test_word_with_multiple_definitions(self, url):
        word = "run"
        actual_data = get_data(url, word)[0]['meanings'][1]['definitions']
        assert len(actual_data) > 1, 'Expected multiple definitions'

    def test_word_with_no_definitions(self, url):
        word = "asdfghjkl"
        actual_status_code = get_status_code(url, word)
        assert actual_status_code > 400, 'Word is not found'

    def test_case_insensitivity(self, url):
        word = "Hello"
        actual_data = get_data(url, word)[0]['word']
        assert actual_data == 'hello', 'Word is found'

    @pytest.mark.parametrize('word', [('c++'), ('++c'), ('+c+'), ('c+c')])
    def test_special_characters(self, url, word):
        actual_data = check_special_chars(url, word)
        assert actual_data, 'Do not supported special_chars'

    def test_uri_encoding(self, url):
        word = "space%20ba"
        actual_data = get_data(url, word)
        assert actual_data < 400, 'Do not supported uri encoding'

    def test_language_parameter(self, url):
        word = "book"
        lang = "es" #Spanish
        actual_data = get_data(url, word, lang)
        assert len(actual_data) > 0, 'Invalid response data,Do not supported language parameter'

    def test_empty_input(self, url):
        word = ""
        actual_status_code = get_status_code(url, word)
        assert actual_status_code == 200, 'Invalid error response'

    def test_rate_limiting(self, url):
        rate_limiter = RateLimiting()
        actual_status_code = rate_limiter.rate_limiting()
        assert actual_status_code == 429, 'Status Code 429 - Too many requests'

    def test_invalid_endpoint(self, url):
        word = "/invalid"
        actual_data = get_data(url, word)
        assert len(actual_data) > 0, 'Invalid response data'

    def test_network_errors(self, url):
        word = "book"
        actual_data = get_data(url, word)
        assert actual_data == 'ConnectionError', 'Network Connection Error'

    def test_long_word_input(self, url):
        word = "supercalifragilisticexpialidocious"
        actual_data = get_data(url, word)
        assert len(actual_data) > 0, 'Long input is supported'
