import time
import requests
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from locators.locators_elements import LocatorsElements
from page_objects.base_page import BasePage


class BrokenLinksImagesPage(BasePage):
    def sidebar_broken_links_image(self):
        # scroll until you find menu element and click the menu
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*LocatorsElements.MENU_ELEMENTS))
        self.click(LocatorsElements.MENU_ELEMENTS)

        # click the broken links images on the sidebar
        self.click(LocatorsElements.SIDEBAR_BROKEN_LINKS_IMAGES)

    def find_broken_links_images(self, by_locator, attribute):
        # find elements links or images
        elems = self.driver.find_elements(*by_locator)
        count = 0

        for elem in elems:
            # try to get images/links with status code 200
            try:
                response = requests.get(elem.get_attribute(attribute), stream=True)
                print(elem.get_attribute(attribute), response.status_code)
                if (response.status_code != 200):
                    print(elem.get_attribute('outerHTML') + " is broken.")
                    count = (count + 1)
            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
        print('===================== The page has ' + str(count) + '/' + str(len(elems)) + ' broken links/images =====================')
        print(' ')