from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class productpage:
    def __init__(self,driver):
        self.driver=driver
        self.add_to_cart_button=(By.ID,"add-to-cart-button")

    def switch_to_new_tab(self):
        tabs=self.driver.window_handles
        self.driver._switch_to.window(tabs[1])

    def click_add_to_cart(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_all_elements_located(self.add_to_cart_button))
        button=self.driver.find_elements(*self.add_to_cart_button)

        if len(button) >1:
            button[1].click()
        else:
            raise Exception("No button found")