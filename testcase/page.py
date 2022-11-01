from locator import *
from element import BasePageElement
import time

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()
    
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
        element.click()

    def recover_titles(self):
        element = self.driver.find_element(*MainPageLocator.MORE_NEWS_BUTTON)
        element.click()
        time.sleep(5)
        matches = self.driver.find_elements(By.TAG_NAME,'h3')
        return matches
        
class SerchResultPage(BasePage):
    def is_result_found(self):
        return "No results found." not in self.driver.page_source