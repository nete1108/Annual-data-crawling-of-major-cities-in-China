from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Local_general_public_budget_expenditures():
    driver = start()
    treeZhiBiao(driver, 6)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0402", "地方一般公共预算支出(亿元)", "1")
    Local_general_public_budget_expenditures = Get_data(driver, "地方一般公共预算支出")
    driver.quit()
    return Local_general_public_budget_expenditures