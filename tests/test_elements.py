import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators_elements import LocatorsElements
from page_objects.elements.buttons_page import ButtonsPage
from page_objects.elements.check_box_page import CheckBoxPage
from page_objects.elements.links_page import LinksPage
from page_objects.elements.radio_button_page import RadioButtonPage
from page_objects.elements.text_box_page import TextBoxPage
from page_objects.elements.web_tables import WebTablesPage
from test_base import EnvironmentSetup


class TestsElements(EnvironmentSetup):
    def test_text_box(self):
        self.TextBoxPage = TextBoxPage(self.driver)
        self.TextBoxPage.text_box()

    def test_check_box(self):
        self.CheckBoxPage = CheckBoxPage(self.driver)
        self.CheckBoxPage.expand_folder()
        self.CheckBoxPage.checklist_box(LocatorsElements.CHECKLIST_DESKTOP, "You have selected :\ndesktop\nnotes\ncommands")
        self.CheckBoxPage.checklist_box(LocatorsElements.CHECKLIST_DOCUMENTS,
                                        "You have selected :\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral")
        self.CheckBoxPage.checklist_box(LocatorsElements.CHECKLIST_DOWNLOADS,
                                        "You have selected :\ndownloads\nwordFile\nexcelFile")

    def test_radio_button(self):
        self.RadioButtonPage = RadioButtonPage(self.driver)
        self.RadioButtonPage.sidebar_radio_button()
        self.RadioButtonPage.select_radio_button(LocatorsElements.RADIO_BUTTON_YES, "You have selected Yes")
        self.RadioButtonPage.select_radio_button(LocatorsElements.RADIO_BUTTON_IMPRESSIVE, "You have selected Impressive")
        self.RadioButtonPage.select_radio_button(LocatorsElements.RADIO_BUTTON_NO, "You have selected No")

    def test_web_tables(self):
        self.WebTablesPage = WebTablesPage(self.driver)
        self.WebTablesPage.sidebar_web_tables()
        # assert data tables before add data
        self.WebTablesPage.assert_data_table("1", "Cierra", "Vega", "39", "cierra@example.com", "10000", "Insurance")
        self.WebTablesPage.assert_data_table("2", "Alden", "Cantrell", "45", "alden@example.com", "12000", "Compliance")
        self.WebTablesPage.assert_data_table("3", "Kierra", "Gentry", "29", "kierra@example.com", "2000", "Legal")
        # add data
        self.WebTablesPage.add_data_table("Afina", "Putri", "20", "afnpd03@gmail.com", "4000", "IT")
        # assert data tables after add data
        self.WebTablesPage.assert_data_table("1", "Cierra", "Vega", "39", "cierra@example.com", "10000", "Insurance")
        self.WebTablesPage.assert_data_table("2", "Alden", "Cantrell", "45", "alden@example.com", "12000", "Compliance")
        self.WebTablesPage.assert_data_table("3", "Kierra", "Gentry", "29", "kierra@example.com", "2000", "Legal")
        self.WebTablesPage.assert_data_table("4", "Afina", "Putri", "20", "afnpd03@gmail.com", "4000", "IT")
        # edit data
        self.WebTablesPage.edit_data_table("1", "Cierra", "Vega", "40", "cierra@example.com", "10000", "Insurance")
        self.WebTablesPage.edit_data_table("2", "Alden", "Cantrell", "45", "aldentest@example.com", "12000", "Compliance")
        self.WebTablesPage.edit_data_table("3", "Kierra", "Gentry", "29", "kierra@example.com", "20000", "Legal")
        self.WebTablesPage.edit_data_table("4", "Zayn", "Malik", "28", "zaynmalik@gmail.com", "2000000", "Singer")
        # assert data tables after edit data
        self.WebTablesPage.assert_data_table("1", "Cierra", "Vega", "40", "cierra@example.com", "10000", "Insurance")
        self.WebTablesPage.assert_data_table("2", "Alden", "Cantrell", "45", "aldentest@example.com", "12000",
                                           "Compliance")
        self.WebTablesPage.assert_data_table("3", "Kierra", "Gentry", "29", "kierra@example.com", "20000", "Legal")
        self.WebTablesPage.assert_data_table("4", "Zayn", "Malik", "28", "zaynmalik@gmail.com", "2000000", "Singer")
        # delete data
        self.WebTablesPage.delete_data_table("4", "Zayn", "Malik", "28", "zaynmalik@gmail.com", "2000000", "Singer")
        # search data
        self.WebTablesPage.search_data_table("Cierra")
        # assert data tables after search data
        self.WebTablesPage.assert_data_table("1", "Cierra", "Vega", "40", "cierra@example.com", "10000", "Insurance")
        self.WebTablesPage.assert_not_data_table("2", "Alden", "Cantrell", "45", "aldentest@example.com", "12000",
                                             "Compliance")
        self.WebTablesPage.assert_not_data_table("3", "Kierra", "Gentry", "29", "kierra@example.com", "20000", "Legal")

    def test_buttons(self):
        self.ButtonsPage = ButtonsPage(self.driver)
        self.ButtonsPage.buttons("You have done a double click", "You have done a right click", "You have done a dynamic click")

    def test_links(self):
        self.LinksPage = LinksPage(self.driver)
        self.LinksPage.sidebar_links()
        # click link "Home" will open new tab
        self.LinksPage.link_new_tab(LocatorsElements.LINK_SIMPLE, "ToolsQA")
        # click link "HomeXga6d" will open new tab
        self.LinksPage.link_new_tab(LocatorsElements.LINK_DYNAMIC, "ToolsQA")
        # link Created
        self.LinksPage.link_api_call(LocatorsElements.LINK_CREATED, "201", "Created")
        # link No Content
        self.LinksPage.link_api_call(LocatorsElements.LINK_NO_CONTENT, "204", "No Content")
        # link Moved
        self.LinksPage.link_api_call(LocatorsElements.LINK_MOVED, "301", "Moved Permanently")
        # link Bad Request
        self.LinksPage.link_api_call(LocatorsElements.LINK_BAD_REQUEST, "400", "Bad Request")
        # link Unauthorized
        self.LinksPage.link_api_call(LocatorsElements.LINK_UNAUTH, "401", "Unauthorized")
        # link Forbidden
        self.LinksPage.link_api_call(LocatorsElements.LINK_FORBIDDEN, "403", "Forbidden")
        # link Not Found
        self.LinksPage.link_api_call(LocatorsElements.LINK_INVALID_URL, "404", "Not Found")