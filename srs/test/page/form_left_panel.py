from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from srs.main.element.label import Label
from srs.main.element.button import Button
from srs.main.base.base_form import BaseForm
from srs.main.utils.json_parser import get_config
from srs.main.driver.driver import Driver

actions = ActionChains(Driver.get_instance())
config = get_config("general.json")


class FormLeftPanel(BaseForm):
    btn_alerts = Button(By.XPATH, "//li[@id='item-1' and .='Alerts']", "btn_alerts")
    panel_collapsed_alerts_frame_and_windows_menu = Label(
        By.XPATH,
        "//div[@class='element-group' and span[@class='group-header' and div[@class='header-wrapper' and div["
        "contains(text(), 'Alerts, Frame & Windows')]]]]//div[contains(@class, 'show')]",
        "panel_collapsed_alerts_frame_and_windows_menu")
    btn_open_list_of_alerts_frame_and_windows = Button(
        By.XPATH,
        "//div[@class='header-wrapper' and div[contains(text(), 'Alerts, Frame & Windows')]]",
        "btn_open_list_of_alerts_frame_and_windows")

    def __init__(self):
        super().__init__(Label(By.XPATH, "//div[@class='left-pannel']", "left_panel_unique_element"),
                         "form_left_panel")

    def click_on_btn_alerts(self):
        self.__click_on_alerts_frame_and_windows_menu_if_is_collapsed()
        self.btn_alerts.click_element()

    def __click_on_alerts_frame_and_windows_menu_if_is_collapsed(self):
        if not self.panel_collapsed_alerts_frame_and_windows_menu.is_visible():
            self.btn_open_list_of_alerts_frame_and_windows.click_element()
            actions.pause(config["pauseInSeconds"]).perform()