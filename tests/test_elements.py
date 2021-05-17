import time
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_elements import LocatorsElements
from page_objects.elements.text_box_page import TextBoxPage
from test_base import EnvironmentSetup


class TestsElements(EnvironmentSetup):
    def test_text_box(self):
        self.TextBoxPage = TextBoxPage(self.driver)
        self.TextBoxPage.text_box()
