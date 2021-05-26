from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class UploadDownloadPage(BasePage):
    def upload_download(self, by_locator, assertText):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the upload & download on the sidebar
        self.click(LocatorsElements.SIDEBAR_UPLOAD_DOWNLOAD)

        # download file
        self.click(LocatorsElements.BUTTON_DOWNLOAD)

        # upload file
        self.enter_text(LocatorsElements.BUTTON_UPLOAD, by_locator)

        # assert uploaded file
        self.assert_element_text(LocatorsElements.ASSERT_UPLOADED, assertText)