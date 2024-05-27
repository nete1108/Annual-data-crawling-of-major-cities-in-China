from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Local_general_public_budget_revenue():
    driver = start()
    treeZhiBiao(driver, 6)
    dtHead(driver)
    sequence(driver)
    Local_general_public_budget_revenue = Get_data(driver, "地方一般公共预算收入")
    driver.quit()
    return Local_general_public_budget_revenue