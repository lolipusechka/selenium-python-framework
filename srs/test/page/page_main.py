from selenium.webdriver.common.by import By

from srs.main.element.label import Label
from srs.main.element.button import Button
from srs.main.base.base_form import BaseForm


class PageMain(BaseForm):
    btn_alerts_frame_and_window = Button(
        By.XPATH, "//div[@class='card-body' and h5[contains(text(), 'Alerts, Frame & Windows')]]",
        "btn_alerts_frame_and_windows")
    btn_elements = Button(
        By.XPATH, "//div[@class='card-body' and h5[contains(text(), 'Elements')]]",
        "btn_elements")
    btn_widgets = Button(
        By.XPATH, "//div[@class='card-body' and h5[contains(text(), 'Widgets')]]",
        "btn_widgets")

    def __init__(self):
        super().__init__(Label(By.XPATH, "//div[@class='home-banner']", "MainPageUniqueElement"),
                         "Main Page")

    def click_on_btn_alerts_frame_and_windows(self):
        self.btn_alerts_frame_and_window.click_element()

    def click_on_btn_elements(self):
        self.btn_elements.click_element()

    def click_on_btn_widgets(self):
        self.btn_widgets.click_element()