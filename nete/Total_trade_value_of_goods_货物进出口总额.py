from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Total_trade_value_of_goods():
    driver = start()
    treeZhiBiao(driver, 8)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0602", "货物进出口总额(百万美元)", "1")
    Total_trade_value_of_goods = Get_data(driver, "货物进出口总额")
    driver.quit()
    return Total_trade_value_of_goods