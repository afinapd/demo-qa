import time

from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage

class DynamicPropertiesPage(BasePage):
    def dynamic_properties(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the dynamic properties on the sidebar
        self.click(LocatorsElements.SIDEBAR_DYNAMIC_PROPERTIES)

        # assert 5 seconds before
        self.is_present(LocatorsElements.ASSERT_COLOR_BEFORE)
        time.sleep(5)

        # assert 5 seconds after
        self.is_present(LocatorsElements.ASSERT_COLOR_AFTER)
        self.is_enabled(LocatorsElements.ASSERT_ENABLE_AFTER)
        self.is_visible(LocatorsElements.ASSERT_VISIBLE_AFTER)