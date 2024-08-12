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
        "user_name" : ("ID", "signup-username"),
        "password" : ("ID", "password-input"),
        "sign_up" : ("XPATH", '//button[normalize-space()="Sign Up"]')
    }

    def click_sign_up(self):
        self.sign_up.click_button()
    
    def register(self):
        self.user_name.set_text("USERNAME")
        self.password.set_text("PASSWORD")

class New_User(unittest.TestCase):
    success_keyword = "Join Twitch today"

    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://twitch.tv")
        wait = WebDriverWait(driver, 10)
        pgDriver = Homepage(driver)
        pgDriver.click_sign_up()
        element = wait.until(EC.element_to_be_clickable((By.ID, "signup-username")))
        pgDriver.register()
        self.assertTrue(self.success_keyword in driver.page_source)

        driver.close()


if __name__ == "__main__":
     unittest.main()          