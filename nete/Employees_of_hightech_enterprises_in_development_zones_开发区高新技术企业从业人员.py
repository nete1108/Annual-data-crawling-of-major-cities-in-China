from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Employees_of_hightech_enterprises_in_development_zones():
    driver = start()
    treeZhiBiao(driver, 10)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0902", "开发区高新技术企业从业人员(人)", "1")
    Employees_of_hightech_enterprises_in_development_zones = Get_data(driver, "开发区高新技术企业从业人员")
    driver.quit()
    return Employees_of_hightech_enterprises_in_development_zones
    