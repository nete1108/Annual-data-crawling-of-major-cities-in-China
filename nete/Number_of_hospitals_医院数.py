from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Number_of_hospitals():
    driver = start()
    treeZhiBiao(driver, 9)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0802", "医院数(个)", "1")
    Number_of_hospitals = Get_data(driver, "医院数")
    driver.quit()
    return Number_of_hospitals