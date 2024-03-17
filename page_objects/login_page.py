import page_objects.base as base
from lookups.locator import Locator


class LoginPage(base.BasePage):
    """
    Buttons and methods used on Search Page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://skleptest.pl/my-account/"

        self.email_field = Locator(
            driver=self.driver,
            selector="[id='username']",
        )
        self.password_field = Locator(
            driver=self.driver,
            selector="[id='password']",
        )
        self.login_button = Locator(
            driver=self.driver,
            selector="[name='login']",
        )
        self.account_name = Locator(
            driver=self.driver,
            selector="[class='woocommerce-MyAccount-content']",
        )
        self.error_name = Locator(
            driver=self.driver,
            selector="[class='woocommerce-error'] li",
        )
        self.empty_password_error = Locator(
            driver=self.driver,
            selector="//div[@class = 'erreur']",
            by="xpath",
            many=True,
        )
        self.user_email = "hhheglgtvvtmkydmyw@cazlq.com"

        self.user_password = "Start123#111"

        self.user_name = "hhheglgtvvtmkydmyw"

    def get_car_by_model(self, car_model):
        return Locator(
            driver=self.driver,
            selector="//tr//td[contains(text(),'{}')]/following-sibling::td/a".format(car_model),
            by="xpath",
            many=True,
        )
