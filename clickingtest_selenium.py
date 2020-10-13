from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://clickspeedtest.com/")

while True:
    python_button = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[5]/div/button[1]")[0]
    python_button.click()
