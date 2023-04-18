from selenium.webdriver.common.by import By
from srs.main.base.base_form import BaseForm
from srs.main.element.label import Label
from srs.test.page.side_bar import SideBar


class FeedPage(BaseForm):
    __uniq_element = Label(By.XPATH, "//div[@class='stories_feed_items_wrap']", "Unique Element")

    def __init__(self):
        super().__init__(self.__uniq_element, "Feed Page")
        self.__side_bar = SideBar()

    def go_to_my_profile(self):
        self.__side_bar.click_ob_btn_my_profile()
