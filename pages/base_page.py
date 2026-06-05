from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        self.page.locator(locator).wait_for(state="visible")

    def expect_element_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def expect_text_contains(self, locator: str, expected_text: str):
        expect(self.page.locator(locator)).to_contain_text(expected_text)

    def get_page_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url