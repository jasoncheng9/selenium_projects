from selenium import webdriver
import time


def main():

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    count = 0

    driver.get("https://typing-speed-test.aoeu.eu/?lang=en")
    current = driver.find_element_by_id('currentword')
    bar = driver.find_element_by_id('input')


    while True and count < 300:
        word = driver.find_element_by_class_name("currentword").text
        bar.send_keys(word + ' ')
        count += 1

    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    main()
