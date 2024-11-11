from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Logs import logging
import logging


logging.info("This is an info message with custom format")

x = 1
y = 1
assert x==y, logging.error("1 is not equal 2")
logging.info("assertion is pass")


def test_1():
    assert 1 == 2



