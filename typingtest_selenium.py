from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://typing-speed-test.aoeu.eu/?lang=en")
current = driver.find_element_by_id('currentword')
bar = driver.find_element_by_id('input')


while True:
    word = driver.find_element_by_class_name("currentword").text
    bar.send_keys(word + ' ')
