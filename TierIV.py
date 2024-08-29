import unittest
import time
from TestRunner import HTMLTestRunner
from TestRunner import SMTP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators = {
        "new_user" : ("XPATH", """//button[normalize-space()="Don't have an account? Sign up"]"""),
        "login" : ("XPATH", '//button[normalize-space()="Log In"]'),
        "user_name" : ("ID", "signup-username"),
        "password" : ("ID", "password-input"),
        "sign_up" : ("XPATH", '//button[normalize-space()="Sign Up"]')
    }

    def click_login(self):
        self.login.click_button()

    def click_new_user(self):
        self.new_user.click_button()

    def click_sign_up(self):
        self.sign_up.click_button()
    
    def register(self):
        self.user_name.set_text("USERNAME")
        self.password.set_text("PASSWORD")


class TestCases(unittest.TestCase):
    success_keyword = "Join Twitch today"
    start_url = "https://twitch.tv"
    
    def test_new_user(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") # for Chrome >= 109
        chrome_options.add_argument("--incognito");
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://twitch.tv")
        wait = WebDriverWait(driver, 60)
        pgDriver = Homepage(driver)
        pgDriver.click_login()
        pgDriver.click_new_user()
        element = wait.until(EC.element_to_be_clickable((By.ID, "signup-username")))
        self.assertTrue(self.success_keyword in driver.page_source)
        driver.close()

    def test_Login(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") # for Chrome >= 109
        chrome_options.add_argument("--incognito");
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://twitch.tv")
        wait = WebDriverWait(driver, 60)
        pgDriver = Homepage(driver)
        pgDriver.click_sign_up()
        element = wait.until(EC.element_to_be_clickable((By.ID, "signup-username")))
        pgDriver.register()
        self.assertTrue(self.success_keyword in driver.page_source)
        driver.close()

def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCases("test_Login"))
    suiteTest.addTest(TestCases("test_new_user"))

    return suiteTest

if __name__ == "__main__": 
    with open('./report.html', 'wb') as f: 
        # open have two parameters, the first is the file name, the second is the mode. 'w' means write, 'r' means read, 'a' means append, 'b' means binary
        runner = HTMLTestRunner( # type: ignore
            stream=f, # this means the test result will be written to the file
            title='TIERIV_TWITCH_TEST_AUTOMATION', # en: test report
            description='Login and Register button test') # en: test report
        unittest.main(testRunner=runner)