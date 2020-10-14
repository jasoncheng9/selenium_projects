from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
delay = 20
close_time = time.time()+delay

driver.get("https://cpstest.org/")

driver.maximize_window()


time.sleep(5)

#element = driver.find_element_by_id('clicker')
#actions = ActionChains(driver)
#actions.move_to_element(element).perform()

while True:
    python_button = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]")[0]
    python_button.click()
    if time.time()>close_time:
        break

time.sleep(5)

retry_button = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/button")[0]
driver.execute_script("arguments[0].click();", retry_button)

time.sleep(5)

driver.quit()
