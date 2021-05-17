from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class TextBoxPage(BasePage):
    def text_box(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the textbox on the sidebar
        self.click(LocatorsElements.SIDEBAR_TEXTBOX)

        # input name, email, current address, and permanent address
        self.enter_text(LocatorsElements.FIELD_USERNAME, "Afina Putri Dayanti")
        self.enter_text(LocatorsElements.FIELD_USEREMAIL, "afnpd03@gmail.com")
        self.enter_text(LocatorsElements.FIELD_CURRENT_ADDRESS, "Jalan Mawar No 30")
        self.enter_text(LocatorsElements.FIELD_PERMANENT_ADDRESS, "Jalan Melati No 10")

        # scroll until you find button submit and click the button
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.BUTTON_SUBMIT))
        self.click(LocatorsElements.BUTTON_SUBMIT)

        # assert the results with your input
        self.assert_element_text(LocatorsElements.ASSERT_EMAIL, "Email:afnpd03@gmail.com")
        self.assert_element_text(LocatorsElements.ASSERT_NAME, "Name:Afina Putri Dayanti")
        self.assert_element_text(LocatorsElements.ASSERT_CURRENT_ADDRESS, "Current Address :Jalan Mawar No 30")
        self.assert_element_text(LocatorsElements.ASSERT_PERMANENT_ADDRESS, "Permananet Address :Jalan Melati No 10")