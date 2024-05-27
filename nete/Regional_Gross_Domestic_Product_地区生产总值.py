from option.start import start
from Get_data import Get_data

def Get_Regional_Gross_Domestic_Product():
    driver = start()
    Regional_Gross_Domestic_Product = Get_data(driver, "地区生产总值(亿元)")
    driver.quit()
    return Regional_Gross_Domestic_Product
