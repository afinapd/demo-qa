from locators.locators_elements import LocatorsElements
from page_objects.elements.check_box_page import CheckBoxPage
from page_objects.elements.radio_button_page import RadioButtonPage
from page_objects.elements.text_box_page import TextBoxPage
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

