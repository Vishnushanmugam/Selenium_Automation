from selenium import webdriver
class driversetup:
    def get_driver():
        driver=webdriver.Chrome()
        driver.maximize_window()
        return driver