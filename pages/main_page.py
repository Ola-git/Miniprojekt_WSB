from pages.base_page import BasePage
from pages.enrolment_page import EnrolmentPage


class MainPage(BasePage):
    def open(self):   # open main page and maximize window

        self.driver.get("https://www.miles-and-more.com/pl/pl.html")
        self.driver.maximize_window()

    def open_login_menu(self):   # click button "Zaloguj"
        self.driver.find_element_by_class_name("is-hidden-loggedIn").click()

    def login_selection_type(self):  # return subpage for login and registration
        return self.driver.find_element_by_class_name("login__selectLoginType")

    def open_registration(self):  # click on registration option and move to another page for registration
        self.driver.find_element_by_link_text("Nie jesteś jeszcze uczestnikiem programu Miles & More? Zarejestruj się bezpłatnie!").click()
        return EnrolmentPage(self.driver)


