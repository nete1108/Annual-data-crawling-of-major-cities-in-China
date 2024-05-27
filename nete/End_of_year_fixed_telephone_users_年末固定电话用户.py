from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_End_of_year_fixed_telephone_users():
    driver = start()
    treeZhiBiao(driver, 7)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0504", "年末固定电话用户(万户)", "1")
    End_of_year_fixed_telephone_users = Get_data(driver, "年末固定电话用户")
    driver.quit()
    return End_of_year_fixed_telephone_users