import time
def treeZhiBiao(driver, num):
    element = driver.find_element_by_id(f'treeZhiBiao_{num}_span')
    element.click()
    time.sleep(0.47)
