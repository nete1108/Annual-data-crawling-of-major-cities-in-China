from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Average_salary_of_non_private_urban_employees():
    driver = start()
    treeZhiBiao(driver, 4)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0202", "城镇非私营单位在岗职工平均工资(元)", "1")
    Average_salary_of_non_private_urban_employees = Get_data(driver, "城镇非私营单位在岗职工平均工资(元)")
    driver.quit()
    return Average_salary_of_non_private_urban_employees