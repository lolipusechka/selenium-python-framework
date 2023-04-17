import logging as log
from srs.main.driver.driver_waits import explicit_wait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, by: str, locator: str, name: str):
        self.by = by
        self.locator = locator
        self.name = name

    def click_element(self):
        log.getLogger().info(f"Click on the element '{self.name}'")
        explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).click()

    def is_visible(self):
        log.getLogger().info(f"Check the visibility of element '{self.name}'")
        return len(explicit_wait().until(lambda d: d.find_elements(self.by, self.locator))) >= 1

    def wait_for_displayed(self):
        explicit_wait().wait().until(EC.visibility_of_element_located((self.by, self.locator)))

    def wait_for_not_displayed(self):
        explicit_wait().wait().until(EC.invisibility_of_element_located((self.by, self.locator)))

    def wait_for_clickable(self):
        explicit_wait().wait().until(EC.element_to_be_clickable((self.by, self.locator)))

    def get_text(self):
        log.getLogger().info(f"Get text from the element '{self.name}'")
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).text

    def get_text_from_attribute(self, attribute):
        log.getLogger().info(f"Get text by attribute '{attribute}' from the element '{self.name}'")
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).get_attribute(attribute)

    def get_web_element(self):
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator))
