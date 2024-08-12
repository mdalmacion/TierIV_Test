import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators = {
        "new_user" : ("XPATH", """//button[normalize-space()="Don't have an account? Sign up"]"""),
        "login" : ("XPATH", '//button[normalize-space()="Log In"]')
    }

    def click_login(self):
        self.login.click_button()

    def click_new_user(self):
        self.new_user.click_button()


class NewUserTest(unittest.TestCase):
    success_keyword = "Join Twitch today"

    def test_new_user(self):
        driver = webdriver.Chrome()
        driver.get("https://twitch.tv")
        wait = WebDriverWait(driver, 10)
        pgDriver = Homepage(driver)
        pgDriver.click_login()
        pgDriver.click_new_user()
        element = wait.until(EC.element_to_be_clickable((By.ID, "signup-username")))
        self.assertTrue(self.success_keyword in driver.page_source)
        driver.close()

if __name__ == "__main__":
     unittest.main()          