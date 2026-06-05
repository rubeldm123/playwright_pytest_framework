import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.json_reader import JsonReader
from utils.logger import Logger


login_data = JsonReader.read_json("login_data.json")


@pytest.mark.regression
@pytest.mark.parametrize("user", login_data["users"])
def test_login_with_multiple_users(page, user):

    logger = Logger.get_logger()
    logger.info(f"Starting test: {user['test_name']}")

    base_url = ConfigReader.get_base_url()
    page.goto(base_url)

    login_page = LoginPage(page)

    username = user["username"]
    password = user["password"]
    expected_result = user["expected_result"]

    login_page.login(username, password)

    if expected_result == "success":
        assert page.url != base_url
        logger.info("Login successful as expected")

    elif expected_result == "failure":
        error_text = login_page.get_error_message()
        assert error_text is not None
        logger.info("Login failed as expected")