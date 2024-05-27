from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Total_export_value_of_hightech_enterprises_in_development_zones():
    driver = start()
    treeZhiBiao(driver, 10)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0905", "开发区高新技术企业出口总额(万美元)", "1")
    Total_export_value_of_hightech_enterprises_in_development_zones = Get_data(driver, "开发区高新技术企业出口总额")
    driver.quit()
    return Total_export_value_of_hightech_enterprises_in_development_zones