from driver import driversetup
from product_page import productpage
from search_page import searchpage
import time

driver=driversetup.get_driver()

try:
    search_page=searchpage(driver)
    search_page.web_open()
    search_page.search_product('Iphone')
    search_page.click_result()

    product_page=productpage(driver)
    product_page.switch_to_new_tab()
    product_page.click_add_to_cart()
    product_page.click_add_to_cart()
    print("pass")
except Exception as e:
    print(f"{e}")

finally:
    time.sleep(5)
    driver.quit()