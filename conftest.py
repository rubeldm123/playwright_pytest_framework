import pytest
import allure
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright


SCREENSHOT_FOLDER = Path(__file__).parent / "screenshots"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=5000
        )
        page = browser.new_page()

        yield page

        page.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page is not None:
            SCREENSHOT_FOLDER.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = SCREENSHOT_FOLDER / f"{item.name}_{timestamp}.png"

            page.screenshot(path=str(screenshot_path), full_page=True)

            allure.attach.file(
                str(screenshot_path),
                name=f"{item.name}_failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            print(f"\nScreenshot saved and attached to Allure: {screenshot_path}")