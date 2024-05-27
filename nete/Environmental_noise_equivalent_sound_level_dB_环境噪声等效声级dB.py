from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data


def Get_Environmental_noise_equivalent_sound_level_dB():
    driver = start()
    treeZhiBiao(driver, 11)
    dtHead(driver)
    sequence(driver)
    dtHead(driver)
    code_name_sort(driver, "A0A02", "环境噪声等效声级dB(A)", "1")
    Environmental_noise_equivalent_sound_level_dB = Get_data(driver, "环境噪声等效声级dB")
    driver.quit()
    return Environmental_noise_equivalent_sound_level_dB
    