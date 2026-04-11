from selenium import webdriver


def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser", "chrome").lower()

    if browser == "chrome":
        context.driver = webdriver.Chrome()

    elif browser == "headlesschrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        context.driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # context.driver.get("https://skleptest.pl/my-account/")
    context.driver.get("https://www.automationexercise.com/login")


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
