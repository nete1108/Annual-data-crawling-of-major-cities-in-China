from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Investment_in_real_estate_development_office_buildings():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0304", "房地产开发办公楼投资额(亿元)", "1")
    Investment_in_real_estate_development_office_buildings = Get_data(driver, "房地产开发办公楼投资额")
    driver.quit()
    return Investment_in_real_estate_development_office_buildings