from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Resident_deposit_balance():
    driver = start()
    treeZhiBiao(driver, 6)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0403", "住户存款余额(亿元)", "1")
    Resident_deposit_balance = Get_data(driver, "住户存款余额")
    driver.quit()
    return Resident_deposit_balance