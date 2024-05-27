from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Post_Office_at_the_end_of_the_year():
    driver = start()
    treeZhiBiao(driver, 7)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0503", "年末邮政局（所）(处)", "1")
    Post_Office_at_the_end_of_the_year = Get_data(driver, "年末邮政局")
    driver.quit()
    return Post_Office_at_the_end_of_the_year