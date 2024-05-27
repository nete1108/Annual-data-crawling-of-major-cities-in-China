from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Registered_residence_population_at_the_end_of_the_year():
    driver = start()
    treeZhiBiao(driver, 4)
    dtHead(driver)
    sequence(driver)
    Registered_residence_population_at_the_end_of_the_year = Get_data(driver, "年末户籍人口(万人)")
    driver.quit()
    return Registered_residence_population_at_the_end_of_the_year