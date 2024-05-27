from Show_current_data import Show_current_data
def Get_data(driver, title):
    list_2003 = []
    list_2004 = []
    list_2005 = []
    list_2006 = []
    list_2007 = []
    list_2008 = []
    list_2009 = []
    list_2010 = []
    list_2011 = []
    list_2012 = []
    list_2013 = []
    list_2014 = []
    list_2015 = []
    list_2016 = []
    list_2017 = []
    list_2018 = []
    list_2019 = []
    list_2020 = []
    list_2021 = []
    list_2022 = []
    i = 1
    while (i < 37):
        data_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
        Show_current_data('2003', i, title, data_2003)
        data_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
        Show_current_data('2004', i, title, data_2004)
        data_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
        Show_current_data('2005', i, title, data_2005)
        data_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
        Show_current_data('2006', i, title, data_2006)
        data_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
        Show_current_data('2007', i, title, data_2007)
        data_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
        Show_current_data('2008', i, title, data_2008)
        data_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
        Show_current_data('2009', i, title, data_2009)
        data_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
        Show_current_data('2010', i, title, data_2010)
        data_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
        Show_current_data('2011', i, title, data_2011)
        data_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
        Show_current_data('2012', i, title, data_2012)
        data_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
        Show_current_data('2013', i, title, data_2013)
        data_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
        Show_current_data('2014', i, title, data_2014)
        data_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
        Show_current_data('2015', i, title, data_2015)
        data_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
        Show_current_data('2016', i, title, data_2016)
        data_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
        Show_current_data('2017', i, title, data_2017)
        data_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
        Show_current_data('2018', i, title, data_2018)
        data_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
        Show_current_data('2019', i, title, data_2019)
        data_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
        Show_current_data('2020', i, title, data_2020)
        data_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
        Show_current_data('2021', i, title, data_2021)
        data_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
        Show_current_data('2022', i, title, data_2022)
        print()
        list_2003.append(data_2003)
        list_2004.append(data_2004)
        list_2005.append(data_2005)
        list_2006.append(data_2006)
        list_2007.append(data_2007)
        list_2008.append(data_2008)
        list_2009.append(data_2009)
        list_2010.append(data_2010)
        list_2011.append(data_2011)
        list_2012.append(data_2012)
        list_2013.append(data_2013)
        list_2014.append(data_2014)
        list_2015.append(data_2015)
        list_2016.append(data_2016)
        list_2017.append(data_2017)
        list_2018.append(data_2018)
        list_2019.append(data_2019)
        list_2020.append(data_2020)
        list_2021.append(data_2021)
        list_2022.append(data_2022)
        i += 1
    print()
    print()
    print()

    # 数据整合
    years = ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
             '2019', '2020', '2021', '2022']
    # years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    data_from_2003_to_2022 = dict(zip(
        # years,
        # [
        #     list_2012,
        #     list_2013,
        #     list_2014,
        #     list_2015,
        #     list_2016,
        #     list_2017,
        #     list_2018,
        #     list_2019,
        #     list_2020,
        #     list_2021,
        #     list_2022
        # ]
        years,
        [
            list_2003,
            list_2004,
            list_2005,
            list_2006,
            list_2007,
            list_2008,
            list_2009,
            list_2010,
            list_2011,
            list_2012,
            list_2013,
            list_2014,
            list_2015,
            list_2016,
            list_2017,
            list_2018,
            list_2019,
            list_2020,
            list_2021,
            list_2022
        ]
    ))
    return data_from_2003_to_2022