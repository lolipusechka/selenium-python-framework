from selenium.webdriver.common.by import By
from srs.main.base.base_form import BaseForm
from srs.main.element.button import Button
from srs.main.element.label import Label
from srs.test.models.photo import Photo
from srs.test.models.post import Post
from srs.test.models.comment import Comment
from srs.main.browser.browser import Browser
from srs.main.utils.action_utils import pause
from srs.main.utils.json_parser import get_config


class MyProfilePage(BaseForm):
    __config = get_config("api_config.json")
    __owner_id = __config["owner_id"]
    __uniq_element = Label(By.XPATH, "//div[@id='profile_photos_module']", "Unique element")

    def __init__(self):
        super().__init__(self.__uniq_element, "My Profile Page")

    def __get_post_element(self, post: Post):
        return Label(By.XPATH, f"//div[@data-post-id='{self.__owner_id}_{post.id}']",
                     f"Post {post.id}")

    def __get_post_text_element(self, post: Post):
        return Label(By.XPATH,
                     f"//div[@data-post-id='{self.__owner_id}_{post.id}']//div[contains(@class, 'wall_post_text')]",
                     "Text from post")

    def __get_post_author_element(self, post: Post):
        return Label(By.XPATH, f"//div[@data-post-id='{self.__owner_id}_{post.id}']//a[@class='author']",
                     "Author of post")

    def __get_post_image_element(self, post: Post):
        return Label(By.XPATH, f"//div[@data-post-id='{self.__owner_id}_{post.id}']//a[@data-photo-id]",
                     "Image of post")

    def __get_post_comment_text_element(self, comment: Comment):
        return Label(By.XPATH, f"//div[@data-post-id='{self.__owner_id}_{comment.id}']//div[@class='wall_reply_text']",
                     "Text from comment")

    def __get_post_comment_author_element(self, comment: Comment):
        return Label(By.XPATH, f"//div[@data-post-id='{self.__owner_id}_{comment.id}']//a[@class='author']",
                     "Author of comment")

    def __get_post_reaction_button(self, post: Post):
        return Button(
            By.XPATH,
            f"//div[@data-post-id='{self.__owner_id}_{post.id}']//div[@data-section-ref='reactions-button-icon']",
            "Like Button")

    def __get_show_next_comments_btn(self, post: Post):
        return Button(By.XPATH,
                      f"//div[@data-post-id='{self.__owner_id}_{post.id}']//span[@class='js-replies_next_label']",
                      "Show Next Comments Button")

    def __scroll_to_img_from_post(self, post: Post):
        label = self.__get_post_image_element(post)
        Browser.scroll_to_element(label.get_web_element())

    def get_text_from_post(self, post: Post) -> str:
        label = self.__get_post_text_element(post)
        label.wait_for_displayed()
        return label.get_text()

    def get_author_from_post(self, post: Post) -> str:
        label = self.__get_post_author_element(post)
        label.wait_for_displayed()
        return label.get_text()

    def get_photo_from_post(self, post: Post) -> Photo:
        label = self.__get_post_image_element(post)
        label.wait_for_displayed()
        # Attribute returned string like ownerId_photoId, this did split string with
        # '_' and return second element of array
        return Photo(int(label.get_text_from_attribute("data-photo-id").split("_")[1]))

    def get_text_from_comment(self, comment: Comment, post: Post):
        self.__scroll_to_img_from_post(post)
        label = self.__get_post_comment_text_element(comment)
        if not label.is_visible():
            self.click_on_btn_show_next_comment()
        label.wait_for_displayed()
        return label.get_text()

    def click_on_btn_show_next_comment(self, post: Post):
        button = self.__get_show_next_comments_btn(post)
        button.wait_for_clickable()
        button.click_element()
        pause()

    def click_on_btn_reaction_post(self, post: Post):
        button = self.__get_post_reaction_button()
        button.wait_for_clickable()
        button.click_element()
        pause()

    def is_post_exist(self, post: Post):
        label = self.__get_post_element(post)
        label.wait_for_not_displayed()
        return not label.is_visible()
