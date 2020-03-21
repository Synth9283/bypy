import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Query:
    def ff(link):
        driver = webdriver.Firefox()
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != link)
        time.sleep(6)
        skip = driver.find_element_by_xpath('//*[@id="skip_bu2tton"]').get_attribute('href')
        direct_link = ''
        for i in skip.split('.'):
            if i == skip.split('.')[0]:
                direct_link = 'https://www5'
            else:
                direct_link = f'{direct_link}.{i}'
        driver.get(direct_link)

    def ch(link):
        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != link)
        time.sleep(6)
        skip = driver.find_element_by_xpath('//*[@id="skip_bu2tton"]').get_attribute('href')
        direct_link = ''
        for i in skip.split('.'):
            if i == skip.split('.')[0]:
                direct_link = 'https://www5'
            else:
                direct_link = f'{direct_link}.{i}'
        driver.get(direct_link)
