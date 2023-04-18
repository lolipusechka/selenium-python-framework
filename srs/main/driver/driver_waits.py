from srs.main.driver.driver import Driver
from srs.main.utils.json_parser import get_config
from selenium.webdriver.support.wait import WebDriverWait

config = get_config("general.json")


def explicit_wait():
    return WebDriverWait(Driver.get_instance(), timeout=int(config["time_out_in_seconds"]))
