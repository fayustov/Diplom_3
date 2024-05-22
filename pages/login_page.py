import allure

from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):

    @allure.step('Проверка формы авторизации')
    def check_authorization_form(self):
        return self.check_element(AuthPageLocators.auth_form)

    @allure.step('Заполнение поля "Email"')
    def input_email_to_email_field(self, email):
        self.send_keys_to_field(AuthPageLocators.email_input, email)

    @allure.step('Заполнение поля "Password"')
    def input_password_to_password_field(self, password):
        self.send_keys_to_field(AuthPageLocators.password_input, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        self.move_to_element_and_click(AuthPageLocators.LOGIN_ENDPOINT_account_btn)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.input_email_to_email_field(email)
        self.input_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_btn(self):
        self.move_to_element_and_click(AuthPageLocators.recover_btn)

    @allure.step('Клик по кнопке "Зарегистрироваться"')
    def click_register_btn(self):
        self.move_to_element_and_click(AuthPageLocators.registration_btn)
        