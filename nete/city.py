from option.start import start

def Get_city():
    driver = start()
    city = []
    i = 1
    while(i<37):
        data = driver.find_elements_by_xpath(f'//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[{i}]/td[1]')[0].text
        city.append(data)
        i += 1
    driver.quit()
    return city