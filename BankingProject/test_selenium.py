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
    time.sleep(1)
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
    actual = get_items_as_number(driver, selectors['Balance'])
    time.sleep(1)
    assert actual == 250, 'Depositing 250 and the Balance yes is 250'

def test_login_manager_and_remove_one_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(1)
    handle_element(driver, selectors['Delete btn'])
    time.sleep(2)
    assert "E55555" not in driver.page_source


def test_login_manager_and_adding_one_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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
    assert "POS8568" in driver.page_source

def test_login_deposit_1000_and_withdrawl_250_and_check_balance_is_750(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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
    time.sleep(1)
    balance = get_items_as_number(driver, selectors['Balance'])
    time.sleep(2)
    assert balance == 750, 'Current Balance is 750'

def test_login_manager_and_adding_one_customer_and_check_url(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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
    actual = driver.current_url
    assert actual != url

def test_login_customer_deposit_1500_and_check_is_in_transactions(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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
    actual = check_items_in_table_list(driver, selectors['Transactions table'], 1500)
    assert actual

def test_login_harry_potter_and_check_3_accounts_if_exist_one_deposit(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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

    assert actual > 0

def test_login_manager_and_check_exist_5_customer(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
    handle_element(driver, selectors['Bank Manager btn'])
    time.sleep(1)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(2)
    actual = return_len_rows_table_list(driver, selectors['Customers table'])
    time.sleep(1)
    assert actual == 5

def test_login_manager_and_check_not_allow_adding_new_customer_without_a_first_name(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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

    assert actual == False

def test_login_customer_deposit_3_deposits_and_check_is_in_transactions(url, selectors):
    driver = init_driver(url)
    ammounts = (100,700,350)
    time.sleep(1)
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
    actual = check_amount_in_transactions_table_list(driver, selectors['Transactions table'], *ammounts)
    time.sleep(1)

    assert actual == True

def test_login_customer_check_deposit_input_not_accept_textual_values(url, selectors):
    driver = init_driver(url)
    time.sleep(1)
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

    assert amount_input_value == ''
