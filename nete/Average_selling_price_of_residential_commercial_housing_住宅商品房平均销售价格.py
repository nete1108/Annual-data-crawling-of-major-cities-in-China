from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Average_selling_price_of_residential_commercial_housing():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A030C", "住宅商品房平均销售价格(元/平方米)", "1")
    Average_selling_price_of_residential_commercial_housing = Get_data(driver, "住宅商品房平均销售价格")
    driver.quit()
    return Average_selling_price_of_residential_commercial_housing