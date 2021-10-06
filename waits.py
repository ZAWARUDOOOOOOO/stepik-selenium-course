from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time,math
browser = webdriver.Chrome(r"C:\\Users\\pasho\\Desktop\\Education\\diploma\\chromedriver.exe")
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.CSS_SELECTOR, '#price'),'$100')
    )
    browser.find_element_by_css_selector('#book').click()
    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = math.log(abs(12 * math.sin(x)))
    browser.find_element_by_css_selector('.form-control').send_keys(f'{y}')
    browser.find_element_by_css_selector('#solve').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()