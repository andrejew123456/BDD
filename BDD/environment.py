from selenium import webdriver
# import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# chromedriver_autoinstaller.install()

def before_scenario(context, scenario):
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser = context.config.userdata.get('browser')
    if not browser:
        browser = 'chrome'
    if browser.lower()== 'chrome':
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.lower() =='headlesschrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    context.driver.get('https://skleptest.pl/my-account/')

def after_scenario(context, scenario):
    context.driver.quit()
