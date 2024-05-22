from faker import Faker
import allure


class Person:

    @staticmethod
    @allure.step('Генерация фейковых данных пользователя')
    def create_data_correct_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data
    