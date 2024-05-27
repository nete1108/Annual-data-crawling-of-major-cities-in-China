from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Real_estate_development_enterprises_purchase_land_area():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A030D", "房地产开发企业购置土地面积(万平方米)", "1")
    Real_estate_development_enterprises_purchase_land_area = Get_data(driver, "房地产开发企业购置土地面积")
    driver.quit()
    return Real_estate_development_enterprises_purchase_land_area