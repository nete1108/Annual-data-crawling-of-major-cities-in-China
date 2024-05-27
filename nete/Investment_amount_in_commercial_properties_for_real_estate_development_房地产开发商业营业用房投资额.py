from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Investment_amount_in_commercial_properties_for_real_estate_development():
    driver = start()
    treeZhiBiao(driver, 5)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0305", "房地产开发商业营业用房投资额(亿元)", "1")
    Investment_amount_in_commercial_properties_for_real_estate_development = Get_data(driver, "房地产开发商业营业用房投资额")
    driver.quit()
    return Investment_amount_in_commercial_properties_for_real_estate_development