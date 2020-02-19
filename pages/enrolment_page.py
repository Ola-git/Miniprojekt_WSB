from enum import Enum
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class Title(Enum): # it helps me parametrize test data
    MR = 1
    MS = 2

class AcademicTitle(Enum):
    NOTITLE = 1
    DR = 2
    PROF = 3
    PROFDR = 4

class EnrolmentPage(BasePage):
    def open(self):  # open enrolment page and maximize window

        self.driver.get("https://www.miles-and-more.com/pl/pl/account/enrolment.html")
        self.driver.maximize_window()

    def choose_title(self, title: Title): # choose "Pan"/"Pani"
        if title == Title.MR:
            val = self.driver.find_element_by_xpath("//input[@value='mr']")
        elif title == Title.MS:
            val = self.driver.find_element_by_xpath("//input[@value='ms']")
        else:
            raise ValueError

        val.click()

    def choose_academic_title(self, academic_title: AcademicTitle): # choose "Bez tytułu", "dr", "prof", "prof.dr"
        if academic_title == AcademicTitle.NOTITLE:
            val = self.driver.find_element_by_id("radiogroup__notitle")
        elif academic_title == AcademicTitle.DR:
            val = self.driver.find_element_by_id("radiogroup__dr")
        elif academic_title == AcademicTitle.PROF:
            val = self.driver.find_element_by_id("radiogroup__prof")
        elif academic_title == AcademicTitle.PROFDR:
            val = self.driver.find_element_by_id("radiogroup__profdr")
        else:
            raise ValueError

        val.click()

    def input_name(self, name):
        self.driver.find_element_by_name("firstName").send_keys(name)

    def input_lastname(self, lastname):
        self.driver.find_element_by_name("lastName").send_keys(lastname)

    def select_birthday(self, day: int):
        self.driver.find_element_by_id("id-birthday-select-label").click()

        # xpath for birthday 21 --> //li[@data-name='21']
        birthday = "//li[@id='id-birthday-select-list-" + str(day-1) + "']"
        elem = self.driver.find_element_by_xpath(birthday)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, birthday)))

        elem.click()

    def select_birthmonth(self, month: int):
        self.driver.find_element_by_id("id-birthmonth-select-label").click()

        # xpath for birthmonth 7 --> //li[@data-name='7']
        birthmonth = "//li[@id='id-birthmonth-select-list-" + str(month-1) + "']"
        elem = self.driver.find_element_by_xpath(birthmonth)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, birthmonth)))

        elem.click()

    def input_birthyear(self, year: int):
        self.driver.find_element_by_name("birthyear").send_keys(year)

    def submit1(self):
        self.driver.find_element_by_name("birthyear").submit()

    # method that returned part2 of registration form
    def section_enrolmentform(self):
        return self.driver.find_element_by_xpath('//section[@class="form__stepContent enrolmentform__step enrolmentform__contactDetailsStep enrolmentform__formstep--is-active"]')

    def input_address(self, address):
        self.driver.find_element_by_name("address").send_keys(address)

    def input_zip(self, zip):
        self.driver.find_element_by_name("zip").send_keys(zip)

    def input_city(self, city):
        self.driver.find_element_by_name("city").send_keys(city)

    def input_email(self, email):
        self.driver.find_element_by_name("email").send_keys(email)

    def input_tel(self, tel1, tel2):
        self.driver.find_element_by_xpath('//input[@name="areacode"]').send_keys(tel1)
        self.driver.find_element_by_xpath('//input[@name="number"]').send_keys(tel2)

    def submit2(self):
        self.driver.find_element_by_name("email").submit()

    def errors(self):
        errors = self.driver.find_elements_by_xpath('//p[@tabindex="0"]')
        errors_displayed = []
        for i in errors:
            if i.is_displayed():
                errors_displayed.append(i)
        return errors_displayed




















