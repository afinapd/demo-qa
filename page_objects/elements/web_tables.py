from selenium.webdriver.common.by import By

from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class WebTablesPage(BasePage):
    def sidebar_web_tables(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the web tables on the sidebar
        self.click(LocatorsElements.SIDEBAR_WEBTABLES)


    def assert_data_table(self, id, firstName, lastName, age, email, salary, department):
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(1)").text == firstName
        assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(2)").text == lastName
        assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(3)").text == age
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(4)").text == email
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(5)").text == salary
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".rt-tr-group:nth-child("+ id + ") .rt-td:nth-child(6)").text == department


    def assert_not_data_table(self, id, firstName, lastName, age, email, salary, department):
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(1)").text == firstName
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(2)").text == lastName
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(3)").text == age
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(4)").text == email
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(5)").text == salary
        assert not self.driver.find_element(By.CSS_SELECTOR,
                                            ".rt-tr-group:nth-child(" + id + ") .rt-td:nth-child(6)").text == department

    def add_data_table(self, firstName, lastName, age, email, salary, department):
        # click button add
        self.click(LocatorsElements.BUTTON_ADD)

        # input data
        self.enter_text(LocatorsElements.FIELD_FIRST_NAME, firstName)
        self.enter_text(LocatorsElements.FIELD_LAST_NAME, lastName)
        self.enter_text(LocatorsElements.FIELD_AGE, age)
        self.enter_text(LocatorsElements.FIELD_USEREMAIL, email)
        self.enter_text(LocatorsElements.FIELD_SALARY, salary)
        self.enter_text(LocatorsElements.FIELD_DEPARTMENT, department)

        # click button submit
        self.click(LocatorsElements.BUTTON_SUBMIT)


    def edit_data_table(self, id, firstName, lastName, age, email, salary, department):
        # click button edit
        self.driver.find_element(By.CSS_SELECTOR, "#edit-record-"+ id +" path").click()

        # edit data
        self.edit_text(LocatorsElements.FIELD_FIRST_NAME, firstName)
        self.edit_text(LocatorsElements.FIELD_LAST_NAME, lastName)
        self.edit_text(LocatorsElements.FIELD_AGE, age)
        self.edit_text(LocatorsElements.FIELD_USEREMAIL, email)
        self.edit_text(LocatorsElements.FIELD_SALARY, salary)
        self.edit_text(LocatorsElements.FIELD_DEPARTMENT, department)

        # click button submit
        self.click(LocatorsElements.BUTTON_SUBMIT)

    def delete_data_table(self, id, firstName, lastName, age, email, salary, department):
        self.WebTablesPage = WebTablesPage(self.driver)
        # click button delete with id
        self.driver.find_element(By.CSS_SELECTOR, "#delete-record-"+ id +" path").click()

        # check that the data that has been deleted is no longer in the table
        self.WebTablesPage.assert_not_data_table(id, firstName, lastName, age, email, salary, department)


    def search_data_table(self, search):
        # search data
        self.enter_text(LocatorsElements.FIELD_SEARCH, search)