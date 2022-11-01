from operator import ne
import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome("C:\\Users\\rfacu\\Desktop\\UnitTest\\testcase\\chromedriver.exe")
        self.driver.get("http://www.python.org")
     
    def test_post_table(self):
        MainPage = page.MainPage(self.driver)
        Newstitles=MainPage.recover_titles()
        print("News:")
        for match in Newstitles:
            print(match.text)
        print("*************************")
        assert Newstitles

    def test_search_python(self):
        MainPage =page.MainPage(self.driver)
        assert MainPage.is_title_matches()
        MainPage.search_text_element = "pycon"
        MainPage.click_go_button()
        search_result_page = page.SerchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()