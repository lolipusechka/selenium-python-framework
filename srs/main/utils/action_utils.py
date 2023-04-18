from srs.main.utils.json_parser import get_config
from selenium.webdriver.common.action_chains import ActionChains
from srs.main.driver.driver import Driver

__config = get_config("general.json")


def pause():
    actions = ActionChains(Driver.get_instance())
    actions.pause(int(__config["pause_in_seconds"]))
    actions.perform()

