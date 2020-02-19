from time import sleep

from pages.enrolment_page import EnrolmentPage, Title, AcademicTitle


class TestEnrolment:

    # input correct data - private method to use in next tests
    def __correct_data_input_part1(self, driver):
        page = EnrolmentPage(driver)
        page.open()
        page.choose_title(Title.MS)
        page.choose_academic_title(AcademicTitle.DR)
        page.input_name("Aleksandra")
        page.input_lastname("Muzykolog")
        page.select_birthday(1)
        page.select_birthmonth(2)
        page.input_birthyear(1980)
        page.submit1()

    def test_correct_data_input_part1(self, driver):  # test if after putting correct data in part1, form part2  will display
        self.__correct_data_input_part1(driver)
        page = EnrolmentPage(driver)
        assert page.section_enrolmentform().is_displayed()

    def test_missing_data_part2(self, driver):  # test missing email in part2
        self.__correct_data_input_part1(driver)
        page = EnrolmentPage(driver)
        page.input_address("Testowa 102")
        page.input_zip("00-010")
        page.input_city("Katowice")
        page.input_tel("111", "11111")
        page.submit2()

        errors = page.errors()
        assert len(errors) == 1  # check if there is only one missing data
        assert "e-mail" in errors[0].get_attribute("innerText")  # check if error message contain "email"




















