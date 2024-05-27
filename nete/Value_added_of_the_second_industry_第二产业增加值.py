from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Value_added_of_the_second_industry():
    driver = start()
    treeZhiBiao(driver, 3)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver,"A0103", "第二产业增加值(亿元)", "1")
    Value_added_of_the_second_industry = Get_data(driver, "第二产业增加值(亿元)")
    driver.quit()
    return Value_added_of_the_second_industry