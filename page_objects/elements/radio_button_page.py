import time

from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class RadioButtonPage(BasePage):
    def sidebar_radio_button(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the checkbox on the sidebar
        self.click(LocatorsElements.SIDEBAR_RADIOBUTTON)

    def select_radio_button(self, radiobutton, text):
        # select radio button x
        self.click(radiobutton)
        time.sleep(2)

        # get element radiobutton
        elem = self.driver.find_element(*radiobutton)

        # try to assert the element radio button
        try:
            self.assert_element_text(LocatorsElements.ASSERT_SELECTED, text)
            print("selected")
        except:
            assert elem.is_selected() is False
            print("not selected")
