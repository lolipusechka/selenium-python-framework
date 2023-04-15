import random
import logging as log

from srs.test.page.page_main import PageMain
from srs.test.page.page_alerts import PageAlerts
from srs.main.base.base_test import BaseTest
from srs.main.utils.json_parser import get_config
from srs.main.utils.random_utils import randomword
from srs.main.browser.browser import Browser
from srs.test.page.page_alerts_frame_and_windows import PageAlertsFrameAndWindows

config = get_config("test_config.json")


class Test(BaseTest):
    page_main = PageMain()
    page_alerts = PageAlerts()
    page_alerts_frame_and_windows = PageAlertsFrameAndWindows()

    def test_alert(self, setup):
        expected_url = config["url"]
        log.getLogger().info("---- Step 1 -----")
        Browser.go_to(expected_url)
        assert self.page_main.is_displayed(), "The page_main was not displayed"

        log.getLogger().info("---- Step 2 -----")
        self.page_main.click_on_btn_alerts_frame_and_windows()
        self.page_alerts_frame_and_windows.click_on_btn_alerts()
        assert self.page_alerts.is_displayed(), "The page_alerts was not displayed"

        log.getLogger().info("---- Step 3 -----")
        self.page_alerts.click_on_btn_alert()
        log.getLogger().info("Check expected the alert with text 'You clicked a button' text with actual")
        assert self.page_alerts.get_text_from_alert() == "You clicked a button", "The alert was not displayed"

        log.getLogger().info("---- Step 4 -----")
        self.page_alerts.alert_accept()
        assert not self.page_alerts.is_alert_display(), "The alert is displaying"

        log.getLogger().info("---- Step 5 -----")
        self.page_alerts.click_on_btn_confirm_alert()
        log.getLogger().info("Check expected the alert with text 'Do you confirm action?' text with actual")
        assert self.page_alerts.get_text_from_alert() == "Do you confirm action?", \
            "The confirm alerts was not displayed"

        log.getLogger().info("---- Step 6 -----")
        self.page_alerts.alert_accept()
        log.getLogger().info("Check expected the alert with text 'You selected Ok' text with actual")
        assert self.page_alerts.get_confirm_text() == "You selected Ok", \
            "The confirm text 'You selected Ok' was not displayed"

        log.getLogger().info("---- Step 7 -----")
        self.page_alerts.click_on_btn_promt_alert()
        log.getLogger().info("Check expected the alert with text 'Please enter your name' text with actual")
        assert self.page_alerts.get_text_from_alert() == "Please enter your name", "The alert was not displayed"

        log.getLogger().info("---- Step 8 -----")
        text = randomword(random.randint(1, 10))
        self.page_alerts.send_keys_to_alert(text)
        self.page_alerts.alert_accept()
        assert not self.page_alerts.is_alert_display(), "The alert was displayed"
        log.getLogger().info(f"Check expected 'You entered {text}' text with actual")
        assert self.page_alerts.get_promt_text() == f"You entered {text}", \
            "The promt string was not equals sent string"
