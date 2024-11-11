from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dynamic-link' and text()='Sign In']")))
sign_in = driver.find_element(By.XPATH, "//a[@class='dynamic-link' and text()='Sign In']")
sign_in.click()

email_field = driver.find_element(By.XPATH, "//input[@id='email' and @type='email']")
email_field.send_keys("anush.hayrapetyan@esterox.am")

pass_field = driver.find_element(By.XPATH, "//input[@id='login-password' and @type='password']")
pass_field.send_keys("Anush123,@")

login_field = driver.find_element(By.XPATH, "//button[@id='login' and @value='Login']")
login_field.click()
time.sleep(5)




print("hello")


