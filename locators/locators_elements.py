from selenium.webdriver.common.by import By


class LocatorsElements():
    MENU_ELEMENTS = (By.CSS_SELECTOR, ".card:nth-child(1) path")
    SIDEBAR_TEXTBOX = (By.CSS_SELECTOR, ".show #item-0 > .text")

    FIELD_USERNAME = (By.ID, "userName")
    FIELD_USEREMAIL = (By.ID, "userEmail")
    FIELD_CURRENT_ADDRESS = (By.ID, "currentAddress")
    FIELD_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    BUTTON_SUBMIT = (By.ID, "submit")
    ASSERT_EMAIL = (By.ID, "email")
    ASSERT_NAME = (By.ID, "name")
    ASSERT_CURRENT_ADDRESS = (By.CSS_SELECTOR, ".border > #currentAddress")
    ASSERT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, ".border > #permanentAddress")