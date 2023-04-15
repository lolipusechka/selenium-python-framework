from selenium.webdriver.common.by import By

from srs.main.element.label import Label
from srs.main.base.base_form import BaseForm
from srs.test.page.form_left_panel import FormLeftPanel


class PageAlertsFrameAndWindows(BaseForm):
    def __init__(self):
        super().__init__(Label(By.XPATH, "//div[@class='main-header' and contains(text(), 'Alerts, Frame & Windows')]",
                               "page_alerts_frame_and_windows_unique_element"), "page_alerts_frame_and_windows")
        self.__form_left_panel = FormLeftPanel()

    def click_on_btn_alerts(self):
        self.__form_left_panel.click_on_btn_alerts()