from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Number_of_hightech_enterprises_in_the_development_zone():
    driver = start()
    treeZhiBiao(driver, 10)
    dtHead(driver)
    sequence(driver)
    Number_of_hightech_enterprises_in_the_development_zone = Get_data(driver, "开发区高新技术企业数")
    driver.quit()
    return Number_of_hightech_enterprises_in_the_development_zone