from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class ButtonsPage(BasePage):
    def buttons(self, messageDoubleClick, messageRightClick, messageClick):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the buttons on the sidebar
        self.click(LocatorsElements.SIDEBAR_BUTTONS)

        # button double click
        self.double_click(LocatorsElements.BUTTON_DOUBLE_CLICK)
        self.assert_element_text(LocatorsElements.ASSERT_DOUBLE_CLICK, messageDoubleClick)

        # button right click
        self.right_click(LocatorsElements.BUTTON_RIGHT_CLICK)
        self.assert_element_text(LocatorsElements.ASSERT_RIGHT_CLICK, messageRightClick)

        # button click
        self.click(LocatorsElements.BUTTON_CLICK)
        self.assert_element_text(LocatorsElements.ASSERT_CLICK, messageClick)
