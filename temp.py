from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(r"C:\\Users\\pasho\\Desktop\\Education\\diploma\\chromedriver.exe")
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]').send_keys('zxfzf')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('asfa')
    browser.find_element_by_css_selector('[name="email"]').send_keys('asfasf')

    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('#file').send_keys(file_path)

    browser.find_element_by_css_selector('.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()