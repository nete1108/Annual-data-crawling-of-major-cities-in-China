from option.sequence import sequence
from option.dtHead import dtHead
from option.treeZhiBiao import treeZhiBiao
from option.code_name_sort import code_name_sort
from option.start import start
from Get_data import Get_data

def Get_Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges():
    driver = start()
    treeZhiBiao(driver, 9)
    dtHead(driver)
    sequence(driver)
    Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges = Get_data(driver, "普通本专科在校学生数")
    driver.quit()
    return Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges