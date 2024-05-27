from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Freight_transportation_volume():
    driver = start()
    treeZhiBiao(driver, 7)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0502", "货物运输量(万吨)", "1")
    Freight_transportation_volume = Get_data(driver, "货物运输量")
    driver.quit()
    return Freight_transportation_volume