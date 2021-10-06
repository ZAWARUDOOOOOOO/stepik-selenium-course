from selenium import webdriver
import time,math
browser = webdriver.Chrome(r"C:\\Users\\pasho\\Desktop\\Education\\diploma\\chromedriver.exe")
browser.get("http://suninjuly.github.io/alert_accept.html")
try:

    input1 = browser.find_element_by_css_selector('.btn').click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = math.log(abs(12 * math.sin(x)))
    browser.find_element_by_css_selector('.form-control').send_keys(f'{y}')
    browser.find_element_by_css_selector('.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()