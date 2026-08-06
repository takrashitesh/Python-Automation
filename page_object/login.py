from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login():
   
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
     self.driver = driver

    def set_username(self, username):
     username_field = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, self.username_xpath))
    )
     username_field.clear()
     username_field.send_keys(username)

    def set_password(self, password):
     password_field = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, self.password_xpath))
    )
     password_field.clear()
     password_field.send_keys(password)

    def click_login(self):
      self.driver.find_element(By.XPATH, self.login_xpath).click()
      
      