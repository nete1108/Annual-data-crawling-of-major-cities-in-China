from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Sales_area_of_residential_commercial_housing():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A030A", "住宅商品房销售面积(万平方米)", "1")
    Sales_area_of_residential_commercial_housing = Get_data(driver, "住宅商品房销售面积")
    driver.quit()
    return Sales_area_of_residential_commercial_housing
