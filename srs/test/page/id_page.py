from srs.main.element.text_box import Textbox
from srs.main.element.button import Button
from srs.main.base.base_form import BaseForm
from selenium.webdriver.common.by import By


class IdPage(BaseForm):
    __password_box = Textbox(By.XPATH, "//input[@name='password']", "Password Box")
    __continue_btn = Button(By.XPATH, "(//span[@class='vkuiButton__in'])[1]", "Continue")

    def __init__(self):
        super().__init__(self.__password_box, "ID Page")

    def input_password(self, password):
        self.__password_box.wait_for_displayed()
        self.__password_box.send_text(password)
        self.__continue_btn.wait_for_clickable()
        self.__continue_btn.click_element()
