from srs.main.base.base_form import BaseForm
from srs.main.utils.json_parser import get_config
from selenium.webdriver.common.action_chains import ActionChains
from srs.main.driver.driver import Driver

__config = get_config("general.json")
__actions = ActionChains(Driver.get_instance())


def pause():
    __actions.pause(__config["pause_in_seconds"]).perform()
