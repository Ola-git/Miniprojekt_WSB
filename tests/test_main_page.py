from pages.main_page import MainPage


class TestMainPage:

    def test_main_page(self, driver):
        m_page = MainPage(driver)
        m_page.open()

        assert "program lojalnościowy dla osób często podróżujących" in driver.title # check page title

    def test_open_login_menu(self, driver):
        m_page = MainPage(driver)
        m_page.open()
        m_page.open_login_menu()

        assert m_page.login_selection_type().is_displayed()  # check if subpage for login is displayed

    def test_login_page(self, driver):
        m_page = MainPage(driver)
        m_page.open()
        m_page.open_login_menu()
        m_page.open_registration()

        assert "Przejdź do rejestracji" in driver.title  # check if you are moved to enrolment page
















