import time

from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class LinksPage(BasePage):
    def sidebar_links(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the links on the sidebar
        self.click(LocatorsElements.SIDEBAR_LINKS)


    def link_new_tab(self, by_locator, titleTab):
        self.vars = {}
        # handle current window https://demoqa.com/links
        self.vars["root"] = self.driver.current_window_handle

        # click the link which will trigger to open a new tab
        self.click(by_locator)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # assert title new tab
        assert self.driver.title == titleTab

        # close new tab
        self.driver.close()

        # switch to window parent
        self.driver.switch_to.window(self.vars["root"])

    def link_api_call(self, by_locator, response, messageResponse):
        self.click(by_locator)
        time.sleep(2)
        self.assert_element_text(LocatorsElements.ASSERT_RESPONSE, "Link has responded with staus "+ response +" and status text " + messageResponse)