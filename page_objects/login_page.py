import page_objects.base as base
from lookups.locator import Locator


class LoginPage(base.BasePage):
    """
    Buttons and methods used on Login Page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/login"

        # Visible after successful login: "Logged in as <username>"
        self.account_name = Locator(
            driver=self.driver,
            selector="a:has(i.fa-user)",
        )

        # Error shown after invalid login
        self.error_name = Locator(
            driver=self.driver,
            selector="form[action='/login'] p",
        )

        # Optional: empty-field validation / generic browser-side error fallback
        # Na tej stronie zwykle walidacja pustego maila/pola jest natywna przeglądarki,
        # więc ten locator może nie być potrzebny.
        self.empty_password_error = Locator(
            driver=self.driver,
            selector="form[action='/login'] input[required]",
            many=True,
        )

        self.user_email = "iwona123@wp.pl"
        self.user_password = "Start123"
        self.user_name = "iwona123"

        self.accept_cookies_button = Locator(
            driver=self.driver,
            selector="//button[@aria-label='Zgadzam się' or @aria-label='Agree']",
            by="xpath",
        )

        self.email_field = Locator(
            driver=self.driver,
            selector="input[data-qa='login-email']",
        )

        self.password_field = Locator(
            driver=self.driver,
            selector="input[data-qa='login-password']",
        )

        self.login_button = Locator(
            driver=self.driver,
            selector="button[data-qa='login-button']",
        )

        self.logged_in_as = Locator(
            driver=self.driver,
            selector="//a[contains(., 'Logged in as')]",
            by="xpath",
        )
