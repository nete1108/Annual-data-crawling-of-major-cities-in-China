from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Completed_housing_area_of_real_estate_development_enterprises():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0307", "房地产开发企业竣工房屋面积(万平方米)", "1")
    Completed_housing_area_of_real_estate_development_enterprises = Get_data(driver, "房地产开发企业竣工房屋面积")
    driver.quit()
    return Completed_housing_area_of_real_estate_development_enterprises