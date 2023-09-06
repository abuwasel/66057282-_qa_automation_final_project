import pytest
from selenium_function import *
from selectors_dic import selector

@pytest.fixture
def url():
    return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

@pytest.fixture()
def selectors():
    return selector

@allure.title("Check the balance of the account is 250")
@allure.description("Log in to the system with one of the existing users,make a deposit of 250 and see that the account balance has changed accordingly.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_deposit_250_and_check_balance(url, selectors):
    """
    Log in to the system with one of the existing users,
    make a deposit of 250 and see that the account balance has changed accordingly.

    Expected: 250
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None),
        ('Deposit btn', None),
        ('amount input', 250),
        ('Deposit submit', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    expected_balance = 250
    actual_balance = get_items_as_number(driver, selectors['Balance'])
    try:
        assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check if deleting user is actually performed.")
@allure.description("Log in to the system with administrator privileges, click on the Users button, delete one of the users you like, write a test that verifies that the action was actually performed.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_manager_and_remove_one_customer(url, selectors):
    """
    Log in to the system with administrator privileges,
    click on the Users button, delete one of the users you like,
    write a test that verifies that the action was actually performed.

    Expected: remove customer E55555
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Bank Manager btn', None),
        ('Customers btn', None),
        ('Delete btn', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    expected = 'E55555'
    actual = driver.page_source
    try:
        assert expected not in actual, f'Expected remove customer: {expected}, but actually its not removed.'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check if adding new client is actually performed.")
@allure.description("Enter the system as an administrator, add a new client,return to the administrator's screen and check that the client you entered is indeed found")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_manager_and_adding_one_customer(url, selectors):
    """
    Enter the system as an administrator,
    add a new client,
    return to the administrator's screen and check that the client you entered is indeed found.

    Expected: adding customer POS8568
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Bank Manager btn', None),
        ('Add Customer btn', None),
        ('First Name input', 'Ibrahim'),
        ('Last Name input', 'Abu Wasel'),
        ('Post Code input', 'POS8568'),
        ('Add Customer submit', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    Alert(driver).accept()
    time.sleep(1)
    handle_element(driver, selectors['Customers btn'])
    time.sleep(2)

    expected_post_code = 'POS8568'
    actual_post_code = driver.page_source
    try:
        assert expected_post_code in actual_post_code, f'Expected adding customer: {expected_post_code}, but actually its not adding'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check the balance of the account is 750")
@allure.description("Enter the bank as a user, make a deposit of 1000 and a withdrawal of 250, check that the balance of the account is 750")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_deposit_1000_and_withdrawl_250_and_check_balance_is_750(url, selectors):
    """
    Enter the bank as a user,
    make a deposit of 1000,
    withdrawal of 250,
    check that the balance of the account is 750.

    Expected: the balance is 750
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None),
        ('Deposit btn', None),
        ('amount input', 1000),
        ('Deposit submit', None),
        ('Withdrawl btn', None),
        ('Withdrawl amount input', 250),
        ('Withdrawl submit', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    expected_balance = 750
    actual_balance = get_items_as_number(driver, selectors['Balance'])
    try:
        assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check if that you are at the appropriate url.")
@allure.description("Write a code that enters the system as an administrator, and add a new account,check that you are at the appropriate url.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_manager_and_adding_one_customer_and_check_url(url, selectors):
    """
    Write a code that enters the system as an administrator,
    and add a new account,
    check that you are at the appropriate url.

    Expected: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Bank Manager btn', None),
        ('Add Customer btn', None),
        ('First Name input', 'Ibrahim'),
        ('Last Name input', 'Abu Wasel'),
        ('Post Code input', 'POS8568'),
        ('Add Customer submit', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    Alert(driver).accept()
    time.sleep(1)
    expected_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    actual_url = driver.current_url
    try:
        assert actual_url == expected_url, f'Expected url: {expected_url}, but got: {actual_url}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check if the transfer has been made and appears in the transfer report.")
@allure.description("Write a code that enters the system as an administrator, and add a new account,check that you are at the appropriate url.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_customer_deposit_1500_and_check_is_in_transactions(url, selectors):
    """
    Enter the system as a user,
    and make a transfer of 1500.
    Make sure that the transfer has been made and appears in the transfer report.

    Expected: True
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None),
        ('Deposit btn', None),
        ('amount input', 1500),
        ('Deposit submit', None),
        ('Transactions btn', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    expected_transaction = True
    actual_transaction = check_items_in_table_list(driver, selectors['Transactions table'], 1500)
    try:
        assert actual_transaction == expected_transaction, f'Expected transaction 1500: {expected_transaction}, but got: {actual_transaction}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("Check if there that all 3 of Harry Potter accounts have only 1 transfer.")
@allure.description("Log in with the Harry Potter user and make sure that all 3 of his accounts have only 1 transfer")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_harry_potter_and_check_3_accounts_if_exist_one_deposit(url, selectors):
    """
    Log in with the Harry Potter user and make sure that all 3 of his accounts have only 1 transfer

    Expected: 1
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

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


@allure.title("Enter by administrator, and check if that you have exactly 5 customers in the system.")
@allure.description("Enter the system as an administrator, and check that you have exactly 5 customers in the system.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_manager_and_check_exist_5_customer(url, selectors):
    """
    Enter the system as an administrator,
    and check that you have exactly 5 customers in the system.

    Expected: 5
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Bank Manager btn', None),
        ('Customers btn', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
        time.sleep(1)

    time.sleep(2)
    expected = 5
    actual = return_len_rows_table_list(driver, selectors['Customers table'])
    try:
        assert actual == expected, f'Expected number of customers: {expected}, but got: {actual}'
    except AssertionError as e:
        # Capture a screenshot and save it if the assertion fails
        capture_a_screenshot_and_save_it(driver)
        raise e


@allure.title("System sanity test")
@allure.description("Do a system sanity test by title.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_sanity_testing(url):
    """
    Do a system sanity test.

    Expected: XYZ Bank
    """
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


@allure.title("Check that the system does not allow adding a new customer without a first name.")
@allure.description("Check that the system does not allow adding a new customer without a first name.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_manager_and_check_not_allow_adding_new_customer_without_a_first_name(url, selectors):
    """
    Check that the system does not allow adding a new customer without a first name.

    Expected: False
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Bank Manager btn', None),
        ('Add Customer btn', None),
        ('First Name input', ''),
        ('Last Name input', 'Abu Wasel'),
        ('Post Code input', 'POS8568'),
        ('Add Customer submit', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
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


@allure.title("Make 3 transfers and verify that the amounts are correct in the transfer report.")
@allure.description("Enter the system as an assistant, make 3 transfers and verify that the amounts are correct in the transfer report.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_customer_deposit_3_deposits_and_check_is_in_transactions(url, selectors):
    """
    Enter the system as an assistant,
    make 3 transfers and verify that the amounts are correct in the transfer report.

    Expected: True
    """
    driver = init_driver(url)
    ammounts = (100, 700, 350)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None),
        ('Deposit btn', None)
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
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


@allure.title("Check that the money deposit field does not accept textual values.")
@allure.description("Enter the system as a user. Check that the money deposit field does not accept textual values, only numbers.")
@allure.label("owner", "Ibrahim Abu Wasel")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
def test_login_customer_check_deposit_input_not_accept_textual_values(url, selectors):
    """
    Enter the system as a user.
    Check that the money deposit field does not accept textual values, only numbers.

    Expected: ''
    """
    driver = init_driver(url)
    time.sleep(2)
    # List of selector keys in the order of execution
    actions = [
        ('Customer Login btn', None),
        ('Harry Potter', None),
        ('Login btn', None),
        ('Deposit btn', None),
        ('amount input', 'hii')
    ]

    for action in actions:
        if action[1] is not None:
            handle_element(driver, selectors[action[0]], action[1])
        else:
            handle_element(driver, selectors[action[0]])
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