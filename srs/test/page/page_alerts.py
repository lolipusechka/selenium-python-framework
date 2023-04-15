from selenium.webdriver.common.by import By

from srs.main.element.alert import Alert
from srs.main.element.label import Label
from srs.main.element.button import Button
from srs.main.base.base_form import BaseForm


class PageAlerts(BaseForm):
    btn_alert = Button(By.XPATH, "//button[@id='alertButton']", "btn_alert")
    btn_confirm_alert = Button(By.XPATH, "//button[@id='confirmButton']", "btn_confirm_alert")
    btn_promt_alert = Button(By.XPATH, "//button[@id='promtButton']", "btn_promt_alert")
    text_confirm_element = Label(By.XPATH, "//span[@id='confirmResult']", "text_confirm_element")
    text_promt_element = Label(By.XPATH, "//span[@id='promptResult']", "text_promt_element")

    def __init__(self):
        super().__init__(self.btn_alert, "page_alerts")
        self.__alerts = Alert()

    def click_on_btn_alert(self):
        self.btn_alert.click_element()

    def click_on_btn_confirm_alert(self):
        self.btn_confirm_alert.click_element()

    def click_on_btn_promt_alert(self):
        self.btn_promt_alert.click_element()

    def get_confirm_text(self) -> str:
        return self.text_confirm_element.get_text()

    def get_promt_text(self) -> str:
        return self.text_promt_element.get_text()

    def get_text_from_alert(self) -> str:
        return self.__alerts.get_text_from_alert()

    def alert_accept(self):
        self.__alerts.alert_accept()

    def is_alert_display(self):
        return self.__alerts.is_alert_display()

    def send_keys_to_alert(self, string: str):
        self.__alerts.alert_send_keys(string)