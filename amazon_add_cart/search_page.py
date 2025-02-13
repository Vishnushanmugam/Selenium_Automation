from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class searchpage:
    def __init__(self,driver):
        self.driver=driver
        self.search_box=(By.ID,"twotabsearchtextbox")
        self.search_result=(By.CSS_SELECTOR,"div.s-main-slot div[data-component-type='s-search-result']")

    def web_open(self):
        self.driver.get("https://amazon.in")

    def search_product(self,product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_box).submit()

    def click_result(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located(self.search_result))
        search_result=self.driver.find_elements(*self.search_result)
        if search_result:
            search_result[2].find_element(By.TAG_NAME,'a').click()
        else:
            raise Exception ("No results found")