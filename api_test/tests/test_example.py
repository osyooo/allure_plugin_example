import allure


@allure.feature("Examples")
class TestUserAuth:

    @allure.title("first test with same start name")
    def test_user_auth_name(self):
        pass

    @allure.title("second test with same start name")
    def test_user_auth_name_and_surname(self):
        pass
