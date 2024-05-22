import allure

from data.urls import URLS, MainUrl
from helpers.user_data import Person
from pages.main_page import MainPage
from pages.password_recovery_page import RecoveryPage
from pages.login_page import LoginPage


class TestRecoveryPage:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_follow_to_the_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        assert recovery_page.check_recovery_form() and recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_recovery)

    @allure.title('Тест ввода почты и клика по кнопке "Восстановить"')
    def test_input_password_and_click_recovery_btn(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.input_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_save_btn() and recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_reset_password)

    @allure.title('Проверка поля "Пароль"')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.input_email_to_email_field(person_data.get("email"))
        recovery_page.click_recovery_btn()
        assert recovery_page.check_active_password_field(person_data.get("password"))
