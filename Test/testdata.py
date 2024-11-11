from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='log_anush',
    datefmt='%Y-%m-%d %H:%M:%S'
)

driver = webdriver.Chrome()
driver.get("https://arm-church.esterox.org/login")
driver.maximize_window()

# Wait for the email field to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")
email_field.send_keys("admin@armchurch.am")
password_field.send_keys("n0d1Fv73YD1")
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and check the title
WebDriverWait(driver, 10).until(EC.title_contains("Գլխավոր"))  # Change to the actual expected title
print(driver.title)
time.sleep(3)
# Wait for the main topic element to be clickable
main_Tem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Թեմեր']")))
main_Tem.click()
time.sleep(3)

# Wait for the add button to be clickable
tem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+ Ավելացնել թեմ']")))
tem.click()
time.sleep(3)

# Wait for the input field to be present
add_tem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @placeholder='Թեմի անուն']")))
add_tem.send_keys("NewName896")
time.sleep(3)
print("Done")
logging.info("Anush152")
def test():
    assert 1 == 1

# save_tem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and normalize-space(text())='Պահպանել']")))
# save_tem.send_keys("Թեմ֊ձ")
# logging.info("Hello")
# search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Թեմեր']")))
# main_Tem.click()
# search = driver.find_element(By.XPATH, "//input[@name='search' and @type='text']")
# assert search == "Թեմ֊ձ"
# print("Done")




driver.quit()
