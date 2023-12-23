import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()


driver.get("https://qauto.forstudy.space/")
driver.find_element(By.NAME, "name").send_keys("Home")
driver.find_element(By.NAME, "lastName").send_keys("Work")
driver.find_element(By.ID, "registerButton").click()


driver.get("https://qauto.forstudy.space/panel/garage")
profile_name = driver.find_element(By.ID, "Home").text
profile_lastName = driver.find_element(By.ID, "Work").text
assert profile_name == "Home", "Error: Name does not match"
assert profile_lastName == "Work", "Error: Last name does not match"


driver.get("")
driver.find_element(By.NAME, "carMake").send_keys("Audi")
driver.find_element(By.NAME, "carModel").send_keys("TT")
driver.find_element(By.ID, "addCarButton").click()


driver.get("")
driver.find_element(By.NAME, "expenseType").send_keys("")
driver.find_element(By.NAME, "expenseAmount").send_keys("100")
driver.find_element(By.ID, "addExpenseButton").click()


driver.get("https://qauto.forstudy.space/panel/settings")
driver.find_element(By.ID, "deleteAccountButton").click()


driver.quit()