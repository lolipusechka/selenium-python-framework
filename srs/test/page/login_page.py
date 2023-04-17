from selenium.webdriver.common.by import By
from srs.main.base.base_form import BaseForm
from srs.main.element.text_box import Textbox
from srs.main.element.button import Button
from srs.main.utils.action_utils import pause


class LoginPage(BaseForm):
    __input_email = Textbox(By.XPATH, "//input[@id='index_email']", "Email")
    __input_pass = Textbox(By.XPATH, "//input[@id='index_pass']", "Password")
    __login_btn = Button(By.XPATH, "//button[@id='index_login_button']", "Login Button")

    def __init__(self):
        super().__init__(self.__input_email, "Login Page")

    def sing_in(self, email: str, password: str):
        self.__input_email.send_text(email)
        pause()
        self.__input_pass.send_text(password)
        pause()
        self.__login_btn.click_element()
        