import time

from selenium.webdriver.common.by import By

from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class CheckBoxPage(BasePage):
    def expand_folder(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the checkbox on the sidebar
        self.click(LocatorsElements.SIDEBAR_CHECKBOX)

        # expand folder
        self.click(LocatorsElements.EXPAND_HOME)
        self.click(LocatorsElements.EXPAND_DESKTOP)
        self.click(LocatorsElements.EXPAND_DOCUMENTS)
        self.click(LocatorsElements.EXPAND_DOWNLOADS)


    def checklist_box(self, folder, text):
        # checklist box x
        self.click(folder)
        time.sleep(3)

        # assert the result
        self.assert_element_text(LocatorsElements.ASSERT_CHECKLIS, text)

        # unchecklist box
        self.click(folder)


