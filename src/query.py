from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Query:
    def ff(link):
        driver = webdriver.Firefox()
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != link)
        skips = driver.find_elements_by_css_selector('#skip_bu2tton [href]')
        link = [skip.get_attribute('href') for skip in skips]
        print(link)

    
    def ch(link):
        driver = webdriver.Chrome()
        driver.get(link)
# the linK: http://maetrimal.com/1B3q
