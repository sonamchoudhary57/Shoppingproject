from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()


driver.find_element(By.LINK_TEXT,"Shop").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText
driver.close()

