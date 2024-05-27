import time
def dtHead(driver):
    element = driver.find_element_by_class_name('dtHead')
    element.click()
    time.sleep(0.47)