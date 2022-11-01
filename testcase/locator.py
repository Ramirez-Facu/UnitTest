from selenium.webdriver.common.by import By

class MainPageLocator(object):
    GO_BUTTON = (By.ID, "submit")
    MORE_NEWS_BUTTON =(By.CLASS_NAME, "give-me-more")

class SearchResultsPageLocator(object):
    pass