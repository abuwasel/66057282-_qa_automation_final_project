import pytest
from selenium_function import *

@pytest.fixture
def url():
    return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

@pytest.fixture()
def selectors():
    return {'Customer Login btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
            'Bank Manager Login btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
            'Harry Potter': '#userSelect > option:nth-child(3)',
            'Login btn': 'body > div > div > div.ng-scope > div > form > button',
            'Deposit btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
            'amount input': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
            'Deposit submit': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
            'Balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
            'Bank Manager btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
            'Customers btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
            'Delete btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button',
            'Add Customer btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
            'First Name input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
            'Last Name input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
            'Post Code input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
            'Add Customer submit': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
            'Withdrawl btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
            'Withdrawl amount input': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
            'Withdrawl submit': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
            'Transactions btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
            'Transactions table': 'body > div > div > div.ng-scope > div > div:nth-child(2) > table > tbody',
            'Transactions Back': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
            'Customers table': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody'
            }

def test_login_deposit_250_and_check_balance(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Deposit btn'])
    time.sleep(1)
    handle_element(driver, selectors['amount input'], 250)
    time.sleep(1)
    handle_element(driver, selectors['Deposit submit'])
    time.sleep(1)
    expected_balance = 5
    actual_balance = get_items_as_number(driver, selectors['Balance'])
    try:
        assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_manager_and_remove_one_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(1)
    handle_element(driver, selectors['Delete btn'])
    time.sleep(2)
    expected = 'E55555'
    actual = driver.page_source
    try:
        assert expected not in actual, f'Expected remove customer: {expected}, but actually its not removed.'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


def test_login_manager_and_adding_one_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Add Customer btn'])
    time.sleep(1)
    handle_element(driver, selectors['First Name input'], 'Ibrahim')
    time.sleep(1)
    handle_element(driver, selectors['Last Name input'], 'Abu Wasel')
    time.sleep(1)
    handle_element(driver, selectors['Post Code input'], 'POS8568')
    time.sleep(1)
    handle_element(driver, selectors['Add Customer submit'])
    time.sleep(1)
    Alert(driver).accept()
    time.sleep(2)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(3)
    expected_post_code = 'POS8568'
    actual_post_code = driver.page_source
    try:
        assert expected_post_code in actual_post_code, f'Expected adding customer: {expected_post_code}, but actually its not adding'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_deposit_1000_and_withdrawl_250_and_check_balance_is_750(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Deposit btn'])
    time.sleep(1)
    handle_element(driver, selectors['amount input'], 1000)
    time.sleep(1)
    handle_element(driver, selectors['Deposit submit'])
    time.sleep(2)
    handle_element(driver, selectors['Withdrawl btn'])
    time.sleep(1)
    handle_element(driver, selectors['Withdrawl amount input'], 250)
    time.sleep(1)
    handle_element(driver, selectors['Withdrawl submit'])
    time.sleep(2)
    expected_balance = 750
    actual_balance = get_items_as_number(driver, selectors['Balance'])
    try:
        assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


def test_login_manager_and_adding_one_customer_and_check_url(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Add Customer btn'])
    time.sleep(1)
    handle_element(driver, selectors['First Name input'], 'Ibrahim')
    time.sleep(1)
    handle_element(driver, selectors['Last Name input'], 'Abu Wasel')
    time.sleep(1)
    handle_element(driver, selectors['Post Code input'], 'POS8568')
    time.sleep(1)
    handle_element(driver, selectors['Add Customer submit'])
    time.sleep(1)
    Alert(driver).accept()
    time.sleep(2)
    expected_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    actual_url = driver.current_url
    try:
        assert actual_url == expected_url, f'Expected url: {expected_url}, but got: {actual_url}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_customer_deposit_1500_and_check_is_in_transactions(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Deposit btn'])
    time.sleep(1)
    handle_element(driver, selectors['amount input'], 1500)
    time.sleep(1)
    handle_element(driver, selectors['Deposit submit'])
    time.sleep(1)
    handle_element(driver, selectors['Transactions btn'])
    time.sleep(2)
    expected_transaction = True
    actual_transaction = check_items_in_table_list(driver, selectors['Transactions table'], 1500)
    try:
        assert actual_transaction == expected_transaction, f'Expected transaction 1500: {expected_transaction}, but got: {actual_transaction}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_harry_potter_and_check_3_accounts_if_exist_one_deposit(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(2)
    accountSelect = Select(driver.find_element(By.CSS_SELECTOR, '#accountSelect'))
    accounts_list = len(accountSelect.options)
    for item in range(accounts_list):
        accountSelect.select_by_index(item)
        handle_element(driver, selectors['Transactions btn'])
        time.sleep(2)
        actual = return_len_rows_table_list(driver, selectors['Transactions table'])
        handle_element(driver, selectors['Transactions Back'])
        time.sleep(1)
        accountSelect = Select(driver.find_element(By.CSS_SELECTOR, '#accountSelect'))

    expected_deposit = 1
    actual_deposit = actual
    try:
        assert actual_deposit > expected_deposit, f'Expected deposit: {expected_deposit}, but got: {actual_deposit}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_manager_and_check_exist_5_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(2)
    expected = 5
    actual = return_len_rows_table_list(driver, selectors['Customers table'])
    try:
        assert actual == expected, f'Expected number of customers: {expected}, but got: {actual}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_sanity_testing(url):
    driver = init_driver(url)
    time.sleep(2)
    expected_title = 'XYZ Bank'
    actual_title = driver.title
    try:
        assert actual_title == expected_title, f'Expected title: {expected_title}, but got: {actual_title}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_manager_and_check_not_allow_adding_new_customer_without_a_first_name(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Add Customer btn'])
    time.sleep(1)
    handle_element(driver, selectors['First Name input'], '')
    time.sleep(1)
    handle_element(driver, selectors['Last Name input'], 'Abu Wasel')
    time.sleep(1)
    handle_element(driver, selectors['Post Code input'], 'POS8568')
    time.sleep(1)
    handle_element(driver, selectors['Add Customer submit'])
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        actual = True
    except NoAlertPresentException:
        actual = False

    expected = False
    try:
        assert actual == expected, f'Expected title: {expected}, but got: {actual}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


def test_login_customer_deposit_3_deposits_and_check_is_in_transactions(url, selectors):
    driver = init_driver(url)
    ammounts = (100,700,350)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Deposit btn'])
    time.sleep(1)
    for i in range(len(ammounts)):
        time.sleep(2)
        handle_element(driver, selectors['amount input'], ammounts[i])
        time.sleep(2)
        handle_element(driver, selectors['Deposit submit'])
    time.sleep(1)
    handle_element(driver, selectors['Transactions btn'])
    time.sleep(2)
    expected_deposit = True
    actual_deposit = check_amount_in_transactions_table_list(driver, selectors['Transactions table'], *ammounts)
    try:
        assert actual_deposit == expected_deposit, f'Expected Deposit: {expected_deposit}, but got: {actual_deposit}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e

def test_login_customer_check_deposit_input_not_accept_textual_values(url, selectors):
    driver = init_driver(url)
    time.sleep(2)
    handle_element(driver, selectors['Customer Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Harry Potter'])
    time.sleep(1)
    handle_element(driver, selectors['Login btn'])
    time.sleep(1)
    handle_element(driver, selectors['Deposit btn'])
    time.sleep(2)
    handle_element(driver, selectors['amount input'], 'hii')
    time.sleep(1)
    amount_input = driver.find_element(By.CSS_SELECTOR, selectors['amount input'])
    amount_input_value = amount_input.get_attribute("value")
    time.sleep(1)
    expected_amount_input_value = ''
    actual_amount_input_value = amount_input_value
    try:
        assert actual_amount_input_value == expected_amount_input_value, f'Expected amount input value: {expected_amount_input_value}, but got: {actual_amount_input_value}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e
