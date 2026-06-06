from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        #Locators
        self.username_input="#username"
        self.password_input="#password"
        self.login_button="button[name='login']"
        self.error_message = ".woocommerce-error"


    #Page Actions
    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)
    def click_login_button(self):
        self.page.click(self.login_button)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
            return self.get_text(self.error_message)