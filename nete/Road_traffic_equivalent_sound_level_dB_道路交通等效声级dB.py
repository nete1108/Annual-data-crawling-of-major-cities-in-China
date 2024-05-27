from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Road_traffic_equivalent_sound_level_dB():
    driver = start()
    treeZhiBiao(driver, 11)
    dtHead(driver)
    sequence(driver)
    Road_traffic_equivalent_sound_level_dB = Get_data(driver, "道路交通等效声级dB(A)")
    driver.quit()
    return Road_traffic_equivalent_sound_level_dB