from selenium.webdriver.common.by import By


class LocatorsElements():
    MENU_ELEMENTS = (By.CSS_SELECTOR, ".card:nth-child(1) path")
    SIDEBAR_TEXTBOX = (By.ID, "item-0")
    SIDEBAR_CHECKBOX = (By.ID, "item-1")
    SIDEBAR_RADIOBUTTON = (By.ID, "item-2")

    FIELD_USERNAME = (By.ID, "userName")
    FIELD_USEREMAIL = (By.ID, "userEmail")
    FIELD_CURRENT_ADDRESS = (By.ID, "currentAddress")
    FIELD_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    BUTTON_SUBMIT = (By.ID, "submit")
    ASSERT_EMAIL = (By.ID, "email")
    ASSERT_NAME = (By.ID, "name")
    ASSERT_CURRENT_ADDRESS = (By.CSS_SELECTOR, ".border > #currentAddress")
    ASSERT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, ".border > #permanentAddress")

    EXPAND_HOME = (By.CSS_SELECTOR, ".rct-icon-expand-close")
    EXPAND_DESKTOP = (By.CSS_SELECTOR, ".rct-node-collapsed:nth-child(1) .rct-collapse > .rct-icon")
    EXPAND_DOCUMENTS = (By.CSS_SELECTOR, ".rct-node-collapsed:nth-child(2) .rct-collapse > .rct-icon")
    EXPAND_DOWNLOADS = (By.CSS_SELECTOR, ".rct-node-collapsed:nth-child(3) .rct-collapse > .rct-icon")
    CHECKLIST_DESKTOP = (By.CSS_SELECTOR, ".rct-node .rct-node-expanded:nth-child(1) > .rct-text .rct-title")
    CHECKLIST_DOCUMENTS = (By.CSS_SELECTOR, ".rct-node .rct-node-expanded:nth-child(2) > .rct-text .rct-title")
    CHECKLIST_DOWNLOADS = (By.CSS_SELECTOR, ".rct-node .rct-node-expanded:nth-child(3) > .rct-text .rct-title")
    ASSERT_CHECKLIS = (By.ID, "result")

    RADIO_BUTTON_YES = (By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, ".custom-control:nth-child(3) > .custom-control-label")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, ".disabled:nth-child(2)")
    ASSERT_SELECTED = (By.CSS_SELECTOR, ".mt-3")
