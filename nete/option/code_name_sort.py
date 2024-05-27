import time
def code_name_sort(driver, code, name, sort):
    element = driver.find_element_by_xpath(f"//li[@node='{{\"code\":\"{code}\",\"name\":\"{name}\",\"sort\":\"{sort}\"}}']")
    element.click()
    time.sleep(0.47)