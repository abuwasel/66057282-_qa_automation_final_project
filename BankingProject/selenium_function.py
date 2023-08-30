import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime


def init_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def handle_element(driver, selector, value=0):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    if value:
        element.send_keys(value)
    else:
        element.click()


def check_items_in_table_list(driver, selector, value=0):
    transactions_table = driver.find_element(By.CSS_SELECTOR, selector)
    transactions = transactions_table.find_elements(By.TAG_NAME, "tr")
    for transaction in transactions:
        if str(value) in transaction.text:
            return True
        break


def return_len_rows_table_list(driver, selector):
    transactions_table = driver.find_element(By.CSS_SELECTOR, selector)
    transactions = transactions_table.find_elements(By.TAG_NAME, "tr")
    return len(transactions)


def check_amount_in_transactions_table_list(driver, selector, *ammounts):
    transactions_table = driver.find_element(By.CSS_SELECTOR, selector)
    transactions = len(transactions_table.find_elements(By.TAG_NAME, "tr"))
    for i in range(transactions):
        Amount = driver.find_element(By.CSS_SELECTOR, f'#anchor{i} > td:nth-child(2)')
        if ammounts[i] == int(Amount.text):
            continue
        else:
            return False

    return True


def get_items_as_number(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector).text
    return float(element.replace("$", ""))


def capture_a_screenshot_and_save_it(driver):
    # Capture a screenshot and save it if the assertion fails
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('screenshots/screenshot-%s.png' % now)
    print("Test failed! Screenshot saved at:", 'screenshots/screenshot-%s.png' % now)
