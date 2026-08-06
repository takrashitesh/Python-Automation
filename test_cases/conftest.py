import pytest
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.read_properties import ReadConfigProperties
from page_object.login import Login



def pytest_addoption(parser):
    parser.addoption("--browser")



# ---------------------------
# Browser fixture
# ---------------------------

@pytest.fixture()
def set_up(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = uc.Chrome()

    elif browser == "firefox":
         driver = webdriver.Firefox()

    else:
        driver = uc.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# ---------------------------
    # Add Command Line Options
# ------------------------

def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )




# ---------------------
# Browser Setup Fixture
# ---------------------



@pytest.fixture()
def set_up(request):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    # Chrome Browser
    if browser == "chrome":

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

    # Firefox Browser (optional)
    elif browser == "firefox":

        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()



    else:
        print(f"'{browser}' is not a valid browser. Launching Chrome by default.")

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)


    yield driver

    driver.quit()



# ------------------------
# Login Fixture
# ----------------------------


@pytest.fixture()
def login_setup(set_up):

    driver = set_up

    driver.get(ReadConfigProperties.get_url())

    login = Login(driver)

    login.set_username(ReadConfigProperties.get_username())
    login.set_password(ReadConfigProperties.get_password())
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar"))
    )

    print("Login Successful")

    return driver