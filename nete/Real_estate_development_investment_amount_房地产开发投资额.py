from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Real_estate_development_investment_amount():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    Real_estate_development_investment_amount = Get_data(driver, "房地产开发投资额")
    driver.quit()
    return Real_estate_development_investment_amount