import time
def sequence(driver):
    element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
    element.click()
    time.sleep(0.47)