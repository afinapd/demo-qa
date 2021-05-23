__author__ = 'Afina P'

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locators.constants import Constants

class EnvironmentSetup(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.driver.get(Constants.baseURL)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        # NOTE: In addCleanup, the first in, is executed last.
        # self.addCleanup(self.driver.quit)
        # self.addCleanup(self.screen_shot)

        self.wait = WebDriverWait(self.driver, timeout=30)
        self.vars = {}

    @classmethod
    def tearDown(self):
        self.driver.delete_all_cookies()
        # self.driver.quit()