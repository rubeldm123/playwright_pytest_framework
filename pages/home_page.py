from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.logo = "img.custom-logo"
        self.my_account_menu = "text=My account"

    # Page Actions
    def open_home_page(self, url):
        self.navigate(url)

    def click_my_account(self):
        self.click(self.my_account_menu)

    def is_logo_visible(self):
        return self.is_visible(self.logo)
    
 