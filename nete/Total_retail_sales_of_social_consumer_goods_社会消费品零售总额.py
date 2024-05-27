from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Total_retail_sales_of_social_consumer_goods():
    driver = start()
    treeZhiBiao(driver, 8)
    dtHead(driver)
    sequence(driver)
    Total_retail_sales_of_social_consumer_goods = Get_data(driver, "社会消费品零售总额(")
    driver.quit()
    return Total_retail_sales_of_social_consumer_goods
    