from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Passenger_transportation_volume():
    driver = start()
    treeZhiBiao(driver, 7)
    dtHead(driver)
    sequence(driver)
    Passenger_transportation_volume = Get_data(driver, "旅客运输量")
    driver.quit()
    return Passenger_transportation_volume