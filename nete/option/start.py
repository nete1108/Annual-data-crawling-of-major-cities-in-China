from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def start():
    # 创建ChromeOptions对象
    chrome_options = Options()

    # 禁用SSL证书验证
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    url = "https://data.stats.gov.cn/easyquery.htm?cn=E0105"
    driver = webdriver.Chrome(options=chrome_options)
    # driver.minimize_window()
    driver.get(url)
    time.sleep(0.47)

    element = driver.find_element_by_xpath("//div[@class='dtHead' and @node='{\"code\":\"LAST5\",\"name\":\"最近5年\",\"sort\":\"4\"}']")
    element.click()
    input_box = driver.find_element_by_class_name("dtText")
    input_box.clear()
    input_box.send_keys("last21")
    confirm_button = driver.find_element_by_xpath("//div[@class='dtTextBtn']")
    confirm_button.click()
    time.sleep(0.47)
    print()

    return driver

