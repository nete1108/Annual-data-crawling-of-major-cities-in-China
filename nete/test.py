# import csv
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# if __name__ == '__main__':
#     # 创建ChromeOptions对象
#     chrome_options = Options()
#
#     # 禁用SSL证书验证
#     chrome_options.add_argument('--ignore-ssl-errors=yes')
#     chrome_options.add_argument('--ignore-certificate-errors')
#
#     url = "https://data.stats.gov.cn/easyquery.htm?cn=E0105"
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     time.sleep(0.47)
#
#
#
#     element = driver.find_element_by_xpath("//div[@class='dtHead' and @node='{\"code\":\"LAST5\",\"name\":\"最近5年\",\"sort\":\"4\"}']")
#     element.click()
#     input_box = driver.find_element_by_class_name("dtText")
#     input_box.clear()
#     input_box.send_keys("last21")
#     confirm_button = driver.find_element_by_xpath("//div[@class='dtTextBtn']")
#     confirm_button.click()
#     time.sleep(0.47)
#     i = 1
#     print()
# #
#     # 城市名和国内地区生产总值
#     area = []
#     Regional_Gross_Domestic_Product_2003 = []
#     Regional_Gross_Domestic_Product_2004 = []
#     Regional_Gross_Domestic_Product_2005 = []
#     Regional_Gross_Domestic_Product_2006 = []
#     Regional_Gross_Domestic_Product_2007 = []
#     Regional_Gross_Domestic_Product_2008 = []
#     Regional_Gross_Domestic_Product_2009 = []
#     Regional_Gross_Domestic_Product_2010 = []
#     Regional_Gross_Domestic_Product_2011 = []
#     Regional_Gross_Domestic_Product_2012 = []
#     Regional_Gross_Domestic_Product_2013 = []
#     Regional_Gross_Domestic_Product_2014 = []
#     Regional_Gross_Domestic_Product_2015 = []
#     Regional_Gross_Domestic_Product_2016 = []
#     Regional_Gross_Domestic_Product_2017 = []
#     Regional_Gross_Domestic_Product_2018 = []
#     Regional_Gross_Domestic_Product_2019 = []
#     Regional_Gross_Domestic_Product_2020 = []
#     Regional_Gross_Domestic_Product_2021 = []
#     Regional_Gross_Domestic_Product_2022 = []
#     while(i < 37):
#         list0 = driver.find_elements_by_xpath(f'//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[{i}]/td[1]')[0].text
#         list2_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list2_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list2_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list2_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list2_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list2_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list2_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list2_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list2_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list2_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list2_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list2_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list2_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list2_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list2_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list2_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list2_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list2_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list2_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list2_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         area.append(list0)
#         Regional_Gross_Domestic_Product_2003.append(list2_2003)
#         Regional_Gross_Domestic_Product_2004.append(list2_2004)
#         Regional_Gross_Domestic_Product_2005.append(list2_2005)
#         Regional_Gross_Domestic_Product_2006.append(list2_2006)
#         Regional_Gross_Domestic_Product_2007.append(list2_2007)
#         Regional_Gross_Domestic_Product_2008.append(list2_2008)
#         Regional_Gross_Domestic_Product_2009.append(list2_2009)
#         Regional_Gross_Domestic_Product_2010.append(list2_2010)
#         Regional_Gross_Domestic_Product_2011.append(list2_2011)
#         Regional_Gross_Domestic_Product_2012.append(list2_2012)
#         Regional_Gross_Domestic_Product_2013.append(list2_2013)
#         Regional_Gross_Domestic_Product_2014.append(list2_2014)
#         Regional_Gross_Domestic_Product_2015.append(list2_2015)
#         Regional_Gross_Domestic_Product_2016.append(list2_2016)
#         Regional_Gross_Domestic_Product_2017.append(list2_2017)
#         Regional_Gross_Domestic_Product_2018.append(list2_2018)
#         Regional_Gross_Domestic_Product_2019.append(list2_2019)
#         Regional_Gross_Domestic_Product_2020.append(list2_2020)
#         Regional_Gross_Domestic_Product_2021.append(list2_2021)
#         Regional_Gross_Domestic_Product_2022.append(list2_2022)
#         print(f'第{i}项数据【地区：{list0}】：2003年国内生产总值：{list2_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2004年国内生产总值：{list2_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2005年国内生产总值：{list2_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2006年国内生产总值：{list2_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2007年国内生产总值：{list2_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2008年国内生产总值：{list2_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2009年国内生产总值：{list2_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2010年国内生产总值：{list2_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2011年国内生产总值：{list2_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2012年国内生产总值：{list2_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2013年国内生产总值：{list2_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2014年国内生产总值：{list2_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2015年国内生产总值：{list2_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2016年国内生产总值：{list2_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2017年国内生产总值：{list2_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2018年国内生产总值：{list2_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2019年国内生产总值：{list2_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2020年国内生产总值：{list2_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2021年国内生产总值：{list2_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{list0}】：2022年国内生产总值：{list2_2022} 已成功爬取\n')
#         i += 1
#     print("省市："+str(area))
#     print("2003年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2003))
#     print("2004年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2004))
#     print("2005年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2005))
#     print("2006年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2006))
#     print("2007年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2007))
#     print("2008年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2008))
#     print("2009年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2009))
#     print("2010年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2010))
#     print("2011年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2011))
#     print("2012年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2012))
#     print("2013年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2013))
#     print("2014年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2014))
#     print("2015年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2015))
#     print("2016年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2016))
#     print("2017年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2017))
#     print("2018年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2018))
#     print("2019年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2019))
#     print("2020年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2020))
#     print("2021年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2021))
#     print("2022年国内地区生产总值：" + str(Regional_Gross_Domestic_Product_2022))
#     time.sleep(0.47)
#
#
#
#
#
#     # 第一产业增加值
#     element = driver.find_element_by_class_name("dtHead")
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0102\",\"name\":\"第一产业增加值(亿元)\",\"sort\":\"1\"}']")
#     element.click()
#     Value_added_of_the_primary_industry_2003 = []
#     Value_added_of_the_primary_industry_2004 = []
#     Value_added_of_the_primary_industry_2005= []
#     Value_added_of_the_primary_industry_2006 = []
#     Value_added_of_the_primary_industry_2007 = []
#     Value_added_of_the_primary_industry_2008 = []
#     Value_added_of_the_primary_industry_2009 = []
#     Value_added_of_the_primary_industry_2010 = []
#     Value_added_of_the_primary_industry_2011 = []
#     Value_added_of_the_primary_industry_2012 = []
#     Value_added_of_the_primary_industry_2013 = []
#     Value_added_of_the_primary_industry_2014 = []
#     Value_added_of_the_primary_industry_2015 = []
#     Value_added_of_the_primary_industry_2016 = []
#     Value_added_of_the_primary_industry_2017 = []
#     Value_added_of_the_primary_industry_2018 = []
#     Value_added_of_the_primary_industry_2019 = []
#     Value_added_of_the_primary_industry_2020 = []
#     Value_added_of_the_primary_industry_2021 = []
#     Value_added_of_the_primary_industry_2022 = []
#     i = 1
#     while(i < 37):
#         list3_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list3_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list3_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list3_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list3_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list3_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list3_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list3_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list3_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list3_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list3_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list3_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list3_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list3_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list3_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list3_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list3_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list3_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list3_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list3_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Value_added_of_the_primary_industry_2003.append(list3_2003)
#         Value_added_of_the_primary_industry_2004.append(list3_2004)
#         Value_added_of_the_primary_industry_2005.append(list3_2005)
#         Value_added_of_the_primary_industry_2006.append(list3_2006)
#         Value_added_of_the_primary_industry_2007.append(list3_2007)
#         Value_added_of_the_primary_industry_2008.append(list3_2008)
#         Value_added_of_the_primary_industry_2009.append(list3_2009)
#         Value_added_of_the_primary_industry_2010.append(list3_2010)
#         Value_added_of_the_primary_industry_2011.append(list3_2011)
#         Value_added_of_the_primary_industry_2012.append(list3_2012)
#         Value_added_of_the_primary_industry_2013.append(list3_2013)
#         Value_added_of_the_primary_industry_2014.append(list3_2014)
#         Value_added_of_the_primary_industry_2015.append(list3_2015)
#         Value_added_of_the_primary_industry_2016.append(list3_2016)
#         Value_added_of_the_primary_industry_2017.append(list3_2017)
#         Value_added_of_the_primary_industry_2018.append(list3_2018)
#         Value_added_of_the_primary_industry_2019.append(list3_2019)
#         Value_added_of_the_primary_industry_2020.append(list3_2020)
#         Value_added_of_the_primary_industry_2021.append(list3_2021)
#         Value_added_of_the_primary_industry_2022.append(list3_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年第一产业增加值：{list3_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年第一产业增加值：{list3_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年第一产业增加值：{list3_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年第一产业增加值：{list3_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年第一产业增加值：{list3_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年第一产业增加值：{list3_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年第一产业增加值：{list3_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年第一产业增加值：{list3_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年第一产业增加值：{list3_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年第一产业增加值：{list3_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年第一产业增加值：{list3_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年第一产业增加值：{list3_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年第一产业增加值：{list3_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年第一产业增加值：{list3_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年第一产业增加值：{list3_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第一产业增加值：{list3_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第一产业增加值：{list3_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第一产业增加值：{list3_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第一产业增加值：{list3_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第一产业增加值：{list3_2022} 已成功爬取\n')
#         i += 1
#     print("2003年第一产业增加值：" + str(Value_added_of_the_primary_industry_2003))
#     print("2004年第一产业增加值：" + str(Value_added_of_the_primary_industry_2004))
#     print("2005年第一产业增加值：" + str(Value_added_of_the_primary_industry_2005))
#     print("2006年第一产业增加值：" + str(Value_added_of_the_primary_industry_2006))
#     print("2007年第一产业增加值：" + str(Value_added_of_the_primary_industry_2007))
#     print("2008年第一产业增加值：" + str(Value_added_of_the_primary_industry_2008))
#     print("2009年第一产业增加值：" + str(Value_added_of_the_primary_industry_2009))
#     print("2010年第一产业增加值：" + str(Value_added_of_the_primary_industry_2010))
#     print("2011年第一产业增加值：" + str(Value_added_of_the_primary_industry_2011))
#     print("2012年第一产业增加值：" + str(Value_added_of_the_primary_industry_2012))
#     print("2013年第一产业增加值：" + str(Value_added_of_the_primary_industry_2013))
#     print("2014年第一产业增加值：" + str(Value_added_of_the_primary_industry_2014))
#     print("2015年第一产业增加值：" + str(Value_added_of_the_primary_industry_2015))
#     print("2016年第一产业增加值：" + str(Value_added_of_the_primary_industry_2016))
#     print("2017年第一产业增加值：" + str(Value_added_of_the_primary_industry_2017))
#     print("2018年第一产业增加值：" + str(Value_added_of_the_primary_industry_2018))
#     print("2019年第一产业增加值：" + str(Value_added_of_the_primary_industry_2019))
#     print("2020年第一产业增加值：" + str(Value_added_of_the_primary_industry_2020))
#     print("2021年第一产业增加值：" + str(Value_added_of_the_primary_industry_2021))
#     print("2021年第一产业增加值：" + str(Value_added_of_the_primary_industry_2022))
#     time.sleep(0.47)
#
#     # 第二产业增加值
#     element = driver.find_element_by_class_name("dtHead")
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0103\",\"name\":\"第二产业增加值(亿元)\",\"sort\":\"1\"}']")
#     element.click()
#     Value_added_of_the_Second_industry_2003 = []
#     Value_added_of_the_Second_industry_2004 = []
#     Value_added_of_the_Second_industry_2005 = []
#     Value_added_of_the_Second_industry_2006 = []
#     Value_added_of_the_Second_industry_2007 = []
#     Value_added_of_the_Second_industry_2008 = []
#     Value_added_of_the_Second_industry_2009 = []
#     Value_added_of_the_Second_industry_2010 = []
#     Value_added_of_the_Second_industry_2011 = []
#     Value_added_of_the_Second_industry_2012 = []
#     Value_added_of_the_Second_industry_2013 = []
#     Value_added_of_the_Second_industry_2014 = []
#     Value_added_of_the_Second_industry_2015 = []
#     Value_added_of_the_Second_industry_2016 = []
#     Value_added_of_the_Second_industry_2017 = []
#     Value_added_of_the_Second_industry_2018 = []
#     Value_added_of_the_Second_industry_2019 = []
#     Value_added_of_the_Second_industry_2020 = []
#     Value_added_of_the_Second_industry_2021 = []
#     Value_added_of_the_Second_industry_2022 = []
#     i = 1
#     while (i < 37):
#         list4_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list4_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list4_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list4_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list4_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list4_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list4_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list4_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list4_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list4_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list4_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list4_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list4_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list4_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list4_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list4_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list4_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list4_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list4_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list4_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Value_added_of_the_Second_industry_2003.append(list4_2003)
#         Value_added_of_the_Second_industry_2004.append(list4_2004)
#         Value_added_of_the_Second_industry_2005.append(list4_2005)
#         Value_added_of_the_Second_industry_2006.append(list4_2006)
#         Value_added_of_the_Second_industry_2007.append(list4_2007)
#         Value_added_of_the_Second_industry_2008.append(list4_2008)
#         Value_added_of_the_Second_industry_2009.append(list4_2009)
#         Value_added_of_the_Second_industry_2010.append(list4_2010)
#         Value_added_of_the_Second_industry_2011.append(list4_2011)
#         Value_added_of_the_Second_industry_2012.append(list4_2012)
#         Value_added_of_the_Second_industry_2013.append(list4_2013)
#         Value_added_of_the_Second_industry_2014.append(list4_2014)
#         Value_added_of_the_Second_industry_2015.append(list4_2015)
#         Value_added_of_the_Second_industry_2016.append(list4_2016)
#         Value_added_of_the_Second_industry_2017.append(list4_2017)
#         Value_added_of_the_Second_industry_2018.append(list4_2018)
#         Value_added_of_the_Second_industry_2019.append(list4_2019)
#         Value_added_of_the_Second_industry_2020.append(list4_2020)
#         Value_added_of_the_Second_industry_2021.append(list4_2021)
#         Value_added_of_the_Second_industry_2022.append(list4_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第二产业增加值：{list4_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第二产业增加值：{list4_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第二产业增加值：{list4_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第二产业增加值：{list4_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第二产业增加值：{list4_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第二产业增加值：{list4_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第二产业增加值：{list4_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第二产业增加值：{list4_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第二产业增加值：{list4_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第二产业增加值：{list4_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第二产业增加值：{list4_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第二产业增加值：{list4_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第二产业增加值：{list4_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第二产业增加值：{list4_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第二产业增加值：{list4_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第二产业增加值：{list4_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第二产业增加值：{list4_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第二产业增加值：{list4_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第二产业增加值：{list4_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第二产业增加值：{list4_2022} 已成功爬取\n')
#         i += 1
#     print("2003年第二产业增加值：" + str(Value_added_of_the_Second_industry_2003))
#     print("2004年第二产业增加值：" + str(Value_added_of_the_Second_industry_2004))
#     print("2005年第二产业增加值：" + str(Value_added_of_the_Second_industry_2005))
#     print("2006年第二产业增加值：" + str(Value_added_of_the_Second_industry_2006))
#     print("2007年第二产业增加值：" + str(Value_added_of_the_Second_industry_2007))
#     print("2008年第二产业增加值：" + str(Value_added_of_the_Second_industry_2008))
#     print("2009年第二产业增加值：" + str(Value_added_of_the_Second_industry_2009))
#     print("2010年第二产业增加值：" + str(Value_added_of_the_Second_industry_2010))
#     print("2011年第二产业增加值：" + str(Value_added_of_the_Second_industry_2011))
#     print("2012年第二产业增加值：" + str(Value_added_of_the_Second_industry_2012))
#     print("2013年第二产业增加值：" + str(Value_added_of_the_Second_industry_2013))
#     print("2014年第二产业增加值：" + str(Value_added_of_the_Second_industry_2014))
#     print("2015年第二产业增加值：" + str(Value_added_of_the_Second_industry_2015))
#     print("2016年第二产业增加值：" + str(Value_added_of_the_Second_industry_2016))
#     print("2017年第二产业增加值：" + str(Value_added_of_the_Second_industry_2017))
#     print("2018年第二产业增加值：" + str(Value_added_of_the_Second_industry_2018))
#     print("2019年第二产业增加值：" + str(Value_added_of_the_Second_industry_2019))
#     print("2020年第二产业增加值：" + str(Value_added_of_the_Second_industry_2020))
#     print("2021年第二产业增加值：" + str(Value_added_of_the_Second_industry_2021))
#     print("2022年第二产业增加值：" + str(Value_added_of_the_Second_industry_2022))
#     time.sleep(0.47)
#
#
#
#     # 第三产业增加值
#     element = driver.find_element_by_class_name("dtHead")
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0104\",\"name\":\"第三产业增加值(亿元)\",\"sort\":\"1\"}']")
#     element.click()
#     Value_added_of_the_third_industry_2003 = []
#     Value_added_of_the_third_industry_2004 = []
#     Value_added_of_the_third_industry_2005 = []
#     Value_added_of_the_third_industry_2006 = []
#     Value_added_of_the_third_industry_2007 = []
#     Value_added_of_the_third_industry_2008 = []
#     Value_added_of_the_third_industry_2009 = []
#     Value_added_of_the_third_industry_2010 = []
#     Value_added_of_the_third_industry_2011 = []
#     Value_added_of_the_third_industry_2012 = []
#     Value_added_of_the_third_industry_2013 = []
#     Value_added_of_the_third_industry_2014 = []
#     Value_added_of_the_third_industry_2015 = []
#     Value_added_of_the_third_industry_2016 = []
#     Value_added_of_the_third_industry_2017 = []
#     Value_added_of_the_third_industry_2018 = []
#     Value_added_of_the_third_industry_2019 = []
#     Value_added_of_the_third_industry_2020 = []
#     Value_added_of_the_third_industry_2021 = []
#     Value_added_of_the_third_industry_2022 = []
#     i = 1
#     while (i < 37):
#         list5_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list5_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list5_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list5_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list5_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list5_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list5_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list5_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list5_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list5_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list5_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list5_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list5_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list5_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list5_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list5_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list5_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list5_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list5_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list5_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Value_added_of_the_third_industry_2003.append(list5_2018)
#         Value_added_of_the_third_industry_2004.append(list5_2019)
#         Value_added_of_the_third_industry_2005.append(list5_2020)
#         Value_added_of_the_third_industry_2006.append(list5_2021)
#         Value_added_of_the_third_industry_2007.append(list5_2022)
#         Value_added_of_the_third_industry_2008.append(list5_2018)
#         Value_added_of_the_third_industry_2009.append(list5_2019)
#         Value_added_of_the_third_industry_2010.append(list5_2020)
#         Value_added_of_the_third_industry_2011.append(list5_2021)
#         Value_added_of_the_third_industry_2012.append(list5_2022)
#         Value_added_of_the_third_industry_2013.append(list5_2018)
#         Value_added_of_the_third_industry_2014.append(list5_2019)
#         Value_added_of_the_third_industry_2015.append(list5_2020)
#         Value_added_of_the_third_industry_2016.append(list5_2021)
#         Value_added_of_the_third_industry_2017.append(list5_2022)
#         Value_added_of_the_third_industry_2018.append(list5_2018)
#         Value_added_of_the_third_industry_2019.append(list5_2019)
#         Value_added_of_the_third_industry_2020.append(list5_2020)
#         Value_added_of_the_third_industry_2021.append(list5_2021)
#         Value_added_of_the_third_industry_2022.append(list5_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第三产业增加值：{list5_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第三产业增加值：{list5_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第三产业增加值：{list5_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第三产业增加值：{list5_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第三产业增加值：{list5_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第三产业增加值：{list5_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第三产业增加值：{list5_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第三产业增加值：{list5_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第三产业增加值：{list5_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第三产业增加值：{list5_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第三产业增加值：{list5_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第三产业增加值：{list5_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第三产业增加值：{list5_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第三产业增加值：{list5_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第三产业增加值：{list5_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年第三产业增加值：{list5_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年第三产业增加值：{list5_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年第三产业增加值：{list5_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年第三产业增加值：{list5_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年第三产业增加值：{list5_2022} 已成功爬取\n')
#         i += 1
#     print("2003年第三产业增加值：" + str(Value_added_of_the_third_industry_2003))
#     print("2004年第三产业增加值：" + str(Value_added_of_the_third_industry_2004))
#     print("2005年第三产业增加值：" + str(Value_added_of_the_third_industry_2005))
#     print("2006年第三产业增加值：" + str(Value_added_of_the_third_industry_2006))
#     print("2007年第三产业增加值：" + str(Value_added_of_the_third_industry_2007))
#     print("2008年第三产业增加值：" + str(Value_added_of_the_third_industry_2008))
#     print("2009年第三产业增加值：" + str(Value_added_of_the_third_industry_2009))
#     print("2010年第三产业增加值：" + str(Value_added_of_the_third_industry_2010))
#     print("2011年第三产业增加值：" + str(Value_added_of_the_third_industry_2011))
#     print("2012年第三产业增加值：" + str(Value_added_of_the_third_industry_2012))
#     print("2013年第三产业增加值：" + str(Value_added_of_the_third_industry_2013))
#     print("2014年第三产业增加值：" + str(Value_added_of_the_third_industry_2014))
#     print("2015年第三产业增加值：" + str(Value_added_of_the_third_industry_2015))
#     print("2016年第三产业增加值：" + str(Value_added_of_the_third_industry_2016))
#     print("2017年第三产业增加值：" + str(Value_added_of_the_third_industry_2017))
#     print("2018年第三产业增加值：" + str(Value_added_of_the_third_industry_2018))
#     print("2019年第三产业增加值：" + str(Value_added_of_the_third_industry_2019))
#     print("2020年第三产业增加值：" + str(Value_added_of_the_third_industry_2020))
#     print("2021年第三产业增加值：" + str(Value_added_of_the_third_industry_2021))
#     print("2022年第三产业增加值：" + str(Value_added_of_the_third_industry_2022))
#     time.sleep(0.47)
#
#
#
#     # 社会商品零售总额
#     element = driver.find_element_by_id('treeZhiBiao_8_span')
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     Total_retail_sales_of_social_goods_2003 = []
#     Total_retail_sales_of_social_goods_2004 = []
#     Total_retail_sales_of_social_goods_2005 = []
#     Total_retail_sales_of_social_goods_2006 = []
#     Total_retail_sales_of_social_goods_2007 = []
#     Total_retail_sales_of_social_goods_2008 = []
#     Total_retail_sales_of_social_goods_2009 = []
#     Total_retail_sales_of_social_goods_2010 = []
#     Total_retail_sales_of_social_goods_2011 = []
#     Total_retail_sales_of_social_goods_2012 = []
#     Total_retail_sales_of_social_goods_2013 = []
#     Total_retail_sales_of_social_goods_2014 = []
#     Total_retail_sales_of_social_goods_2015 = []
#     Total_retail_sales_of_social_goods_2016 = []
#     Total_retail_sales_of_social_goods_2017 = []
#     Total_retail_sales_of_social_goods_2018 = []
#     Total_retail_sales_of_social_goods_2019 = []
#     Total_retail_sales_of_social_goods_2020 = []
#     Total_retail_sales_of_social_goods_2021 = []
#     Total_retail_sales_of_social_goods_2022 = []
#     i = 1
#     while(i < 37):
#         list6_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list6_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list6_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list6_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list6_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list6_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list6_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list6_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list6_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list6_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list6_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list6_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list6_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list6_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list6_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list6_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list6_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list6_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list6_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list6_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Total_retail_sales_of_social_goods_2003.append(list6_2003)
#         Total_retail_sales_of_social_goods_2004.append(list6_2004)
#         Total_retail_sales_of_social_goods_2005.append(list6_2005)
#         Total_retail_sales_of_social_goods_2006.append(list6_2006)
#         Total_retail_sales_of_social_goods_2007.append(list6_2007)
#         Total_retail_sales_of_social_goods_2008.append(list6_2008)
#         Total_retail_sales_of_social_goods_2009.append(list6_2009)
#         Total_retail_sales_of_social_goods_2010.append(list6_2010)
#         Total_retail_sales_of_social_goods_2011.append(list6_2011)
#         Total_retail_sales_of_social_goods_2012.append(list6_2012)
#         Total_retail_sales_of_social_goods_2013.append(list6_2013)
#         Total_retail_sales_of_social_goods_2014.append(list6_2014)
#         Total_retail_sales_of_social_goods_2015.append(list6_2015)
#         Total_retail_sales_of_social_goods_2016.append(list6_2016)
#         Total_retail_sales_of_social_goods_2017.append(list6_2017)
#         Total_retail_sales_of_social_goods_2018.append(list6_2018)
#         Total_retail_sales_of_social_goods_2019.append(list6_2019)
#         Total_retail_sales_of_social_goods_2020.append(list6_2020)
#         Total_retail_sales_of_social_goods_2021.append(list6_2021)
#         Total_retail_sales_of_social_goods_2022.append(list6_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年社会商品零售总额：{list6_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年社会商品零售总额：{list6_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年社会商品零售总额：{list6_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年社会商品零售总额：{list6_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年社会商品零售总额：{list6_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年社会商品零售总额：{list6_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年社会商品零售总额：{list6_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年社会商品零售总额：{list6_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年社会商品零售总额：{list6_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年社会商品零售总额：{list6_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年社会商品零售总额：{list6_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年社会商品零售总额：{list6_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年社会商品零售总额：{list6_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年社会商品零售总额：{list6_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年社会商品零售总额：{list6_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年社会商品零售总额：{list6_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年社会商品零售总额：{list6_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年社会商品零售总额：{list6_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年社会商品零售总额：{list6_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年社会商品零售总额：{list6_2022} 已成功爬取\n')
#         i += 1
#     print("2003年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2003))
#     print("2004年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2004))
#     print("2005年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2005))
#     print("2006年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2006))
#     print("2007年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2007))
#     print("2008年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2008))
#     print("2009年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2009))
#     print("2010年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2010))
#     print("2011年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2011))
#     print("2012年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2012))
#     print("2013年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2013))
#     print("2014年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2014))
#     print("2015年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2015))
#     print("2016年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2016))
#     print("2017年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2017))
#     print("2018年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2018))
#     print("2019年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2019))
#     print("2020年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2020))
#     print("2021年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2021))
#     print("2022年社会商品零售总额" + str(Total_retail_sales_of_social_goods_2022))
#     time.sleep(0.47)
#
#
#
#     # 货物进出口总额
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0602\",\"name\":\"货物进出口总额(百万美元)\",\"sort\":\"1\"}']")
#     element.click()
#     Total_import_and_export_value_of_goods_2003 = []
#     Total_import_and_export_value_of_goods_2004 = []
#     Total_import_and_export_value_of_goods_2005 = []
#     Total_import_and_export_value_of_goods_2006 = []
#     Total_import_and_export_value_of_goods_2007 = []
#     Total_import_and_export_value_of_goods_2008 = []
#     Total_import_and_export_value_of_goods_2009 = []
#     Total_import_and_export_value_of_goods_2010 = []
#     Total_import_and_export_value_of_goods_2011 = []
#     Total_import_and_export_value_of_goods_2012 = []
#     Total_import_and_export_value_of_goods_2013 = []
#     Total_import_and_export_value_of_goods_2014 = []
#     Total_import_and_export_value_of_goods_2015 = []
#     Total_import_and_export_value_of_goods_2016 = []
#     Total_import_and_export_value_of_goods_2017 = []
#     Total_import_and_export_value_of_goods_2018 = []
#     Total_import_and_export_value_of_goods_2019 = []
#     Total_import_and_export_value_of_goods_2020 = []
#     Total_import_and_export_value_of_goods_2021 = []
#     Total_import_and_export_value_of_goods_2022 = []
#     i = 1
#     while (i < 37):
#         list7_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list7_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list7_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list7_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list7_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list7_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list7_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list7_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list7_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list7_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list7_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list7_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list7_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list7_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list7_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list7_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list7_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list7_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list7_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list7_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Total_import_and_export_value_of_goods_2003.append(list7_2003)
#         Total_import_and_export_value_of_goods_2004.append(list7_2004)
#         Total_import_and_export_value_of_goods_2005.append(list7_2005)
#         Total_import_and_export_value_of_goods_2006.append(list7_2006)
#         Total_import_and_export_value_of_goods_2007.append(list7_2007)
#         Total_import_and_export_value_of_goods_2008.append(list7_2008)
#         Total_import_and_export_value_of_goods_2009.append(list7_2009)
#         Total_import_and_export_value_of_goods_2010.append(list7_2010)
#         Total_import_and_export_value_of_goods_2011.append(list7_2011)
#         Total_import_and_export_value_of_goods_2012.append(list7_2012)
#         Total_import_and_export_value_of_goods_2013.append(list7_2013)
#         Total_import_and_export_value_of_goods_2014.append(list7_2014)
#         Total_import_and_export_value_of_goods_2015.append(list7_2015)
#         Total_import_and_export_value_of_goods_2016.append(list7_2016)
#         Total_import_and_export_value_of_goods_2017.append(list7_2017)
#         Total_import_and_export_value_of_goods_2018.append(list7_2018)
#         Total_import_and_export_value_of_goods_2019.append(list7_2019)
#         Total_import_and_export_value_of_goods_2020.append(list7_2020)
#         Total_import_and_export_value_of_goods_2021.append(list7_2021)
#         Total_import_and_export_value_of_goods_2022.append(list7_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年货物进出口总额：{list7_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年货物进出口总额：{list7_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年货物进出口总额：{list7_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年货物进出口总额：{list7_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年货物进出口总额：{list7_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年货物进出口总额：{list7_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年货物进出口总额：{list7_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年货物进出口总额：{list7_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年货物进出口总额：{list7_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年货物进出口总额：{list7_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年货物进出口总额：{list7_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年货物进出口总额：{list7_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年货物进出口总额：{list7_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年货物进出口总额：{list7_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年货物进出口总额：{list7_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年货物进出口总额：{list7_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年货物进出口总额：{list7_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年货物进出口总额：{list7_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年货物进出口总额：{list7_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年货物进出口总额：{list7_2022} 已成功爬取\n')
#         i += 1
#     print("2003年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2003))
#     print("2004年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2004))
#     print("2005年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2005))
#     print("2006年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2006))
#     print("2007年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2007))
#     print("2008年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2008))
#     print("2009年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2009))
#     print("2010年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2010))
#     print("2011年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2011))
#     print("2012年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2012))
#     print("2013年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2013))
#     print("2014年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2014))
#     print("2015年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2015))
#     print("2016年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2016))
#     print("2017年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2017))
#     print("2018年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2018))
#     print("2019年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2019))
#     print("2020年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2020))
#     print("2021年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2021))
#     print("2022年货物进出口总额：" + str(Total_import_and_export_value_of_goods_2022))
#     time.sleep(0.47)
#
#
#     # 年末总人口
#     element = driver.find_element_by_id('treeZhiBiao_4_span')
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     Total_Population_2003 = []
#     Total_Population_2004 = []
#     Total_Population_2005 = []
#     Total_Population_2006 = []
#     Total_Population_2007 = []
#     Total_Population_2008 = []
#     Total_Population_2009 = []
#     Total_Population_2010 = []
#     Total_Population_2011 = []
#     Total_Population_2012 = []
#     Total_Population_2013 = []
#     Total_Population_2014 = []
#     Total_Population_2015 = []
#     Total_Population_2016 = []
#     Total_Population_2017 = []
#     Total_Population_2018 = []
#     Total_Population_2019 = []
#     Total_Population_2020 = []
#     Total_Population_2021 = []
#     Total_Population_2022 = []
#     i = 1
#     while (i < 37):
#         list8_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list8_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list8_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list8_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list8_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list8_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list8_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list8_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list8_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list8_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list8_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list8_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list8_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list8_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list8_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list8_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list8_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list8_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list8_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list8_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Total_Population_2003.append(list8_2003)
#         Total_Population_2004.append(list8_2004)
#         Total_Population_2005.append(list8_2005)
#         Total_Population_2006.append(list8_2006)
#         Total_Population_2007.append(list8_2007)
#         Total_Population_2008.append(list8_2008)
#         Total_Population_2009.append(list8_2009)
#         Total_Population_2010.append(list8_2010)
#         Total_Population_2011.append(list8_2011)
#         Total_Population_2012.append(list8_2012)
#         Total_Population_2013.append(list8_2013)
#         Total_Population_2014.append(list8_2014)
#         Total_Population_2015.append(list8_2015)
#         Total_Population_2016.append(list8_2016)
#         Total_Population_2017.append(list8_2017)
#         Total_Population_2018.append(list8_2018)
#         Total_Population_2019.append(list8_2019)
#         Total_Population_2020.append(list8_2020)
#         Total_Population_2021.append(list8_2021)
#         Total_Population_2022.append(list8_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年年末总人口：{list8_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年年末总人口：{list8_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年年末总人口：{list8_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年年末总人口：{list8_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年年末总人口：{list8_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年年末总人口：{list8_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年年末总人口：{list8_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年年末总人口：{list8_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年年末总人口：{list8_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年年末总人口：{list8_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年年末总人口：{list8_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年年末总人口：{list8_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年年末总人口：{list8_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年年末总人口：{list8_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年年末总人口：{list8_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年年末总人口：{list8_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年年末总人口：{list8_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年年末总人口：{list8_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年年末总人口：{list8_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年年末总人口：{list8_2022} 已成功爬取\n')
#         i += 1
#     print("2003年年末总人口：" + str(Total_Population_2003))
#     print("2004年年末总人口：" + str(Total_Population_2004))
#     print("2005年年末总人口：" + str(Total_Population_2005))
#     print("2006年年末总人口：" + str(Total_Population_2006))
#     print("2007年年末总人口：" + str(Total_Population_2007))
#     print("2008年年末总人口：" + str(Total_Population_2008))
#     print("2009年年末总人口：" + str(Total_Population_2009))
#     print("2010年年末总人口：" + str(Total_Population_2010))
#     print("2011年年末总人口：" + str(Total_Population_2011))
#     print("2012年年末总人口：" + str(Total_Population_2012))
#     print("2013年年末总人口：" + str(Total_Population_2013))
#     print("2014年年末总人口：" + str(Total_Population_2014))
#     print("2015年年末总人口：" + str(Total_Population_2015))
#     print("2016年年末总人口：" + str(Total_Population_2016))
#     print("2017年年末总人口：" + str(Total_Population_2017))
#     print("2018年年末总人口：" + str(Total_Population_2018))
#     print("2019年年末总人口：" + str(Total_Population_2019))
#     print("2020年年末总人口：" + str(Total_Population_2020))
#     print("2021年年末总人口：" + str(Total_Population_2021))
#     print("2022年年末总人口：" + str(Total_Population_2022))
#     time.sleep(0.47)
#
#     # 在岗职工平均工资
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0202\",\"name\":\"城镇非私营单位在岗职工平均工资(元)\",\"sort\":\"1\"}']")
#     element.click()
#     Average_salary_of_on_duty_employees_2003 = []
#     Average_salary_of_on_duty_employees_2004 = []
#     Average_salary_of_on_duty_employees_2005 = []
#     Average_salary_of_on_duty_employees_2006 = []
#     Average_salary_of_on_duty_employees_2007 = []
#     Average_salary_of_on_duty_employees_2008 = []
#     Average_salary_of_on_duty_employees_2009 = []
#     Average_salary_of_on_duty_employees_2010 = []
#     Average_salary_of_on_duty_employees_2011 = []
#     Average_salary_of_on_duty_employees_2012 = []
#     Average_salary_of_on_duty_employees_2013 = []
#     Average_salary_of_on_duty_employees_2014 = []
#     Average_salary_of_on_duty_employees_2015 = []
#     Average_salary_of_on_duty_employees_2016 = []
#     Average_salary_of_on_duty_employees_2017 = []
#     Average_salary_of_on_duty_employees_2018 = []
#     Average_salary_of_on_duty_employees_2019 = []
#     Average_salary_of_on_duty_employees_2020 = []
#     Average_salary_of_on_duty_employees_2021 = []
#     Average_salary_of_on_duty_employees_2022 = []
#     i = 1
#     while (i < 37):
#         list9_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list9_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list9_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list9_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list9_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list9_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list9_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list9_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list9_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list9_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list9_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list9_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list9_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list9_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list9_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list9_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list9_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list9_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list9_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list9_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Average_salary_of_on_duty_employees_2003.append(list9_2003)
#         Average_salary_of_on_duty_employees_2004.append(list9_2004)
#         Average_salary_of_on_duty_employees_2005.append(list9_2005)
#         Average_salary_of_on_duty_employees_2006.append(list9_2006)
#         Average_salary_of_on_duty_employees_2007.append(list9_2007)
#         Average_salary_of_on_duty_employees_2008.append(list9_2008)
#         Average_salary_of_on_duty_employees_2009.append(list9_2009)
#         Average_salary_of_on_duty_employees_2010.append(list9_2010)
#         Average_salary_of_on_duty_employees_2011.append(list9_2011)
#         Average_salary_of_on_duty_employees_2012.append(list9_2012)
#         Average_salary_of_on_duty_employees_2013.append(list9_2013)
#         Average_salary_of_on_duty_employees_2014.append(list9_2014)
#         Average_salary_of_on_duty_employees_2015.append(list9_2015)
#         Average_salary_of_on_duty_employees_2016.append(list9_2016)
#         Average_salary_of_on_duty_employees_2017.append(list9_2017)
#         Average_salary_of_on_duty_employees_2018.append(list9_2018)
#         Average_salary_of_on_duty_employees_2019.append(list9_2019)
#         Average_salary_of_on_duty_employees_2020.append(list9_2020)
#         Average_salary_of_on_duty_employees_2021.append(list9_2021)
#         Average_salary_of_on_duty_employees_2022.append(list9_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年在岗职工平均工资：{list9_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年在岗职工平均工资：{list9_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年在岗职工平均工资：{list9_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年在岗职工平均工资：{list9_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年在岗职工平均工资：{list9_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年在岗职工平均工资：{list9_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年在岗职工平均工资：{list9_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年在岗职工平均工资：{list9_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年在岗职工平均工资：{list9_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年在岗职工平均工资：{list9_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年在岗职工平均工资：{list9_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年在岗职工平均工资：{list9_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年在岗职工平均工资：{list9_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年在岗职工平均工资：{list9_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年在岗职工平均工资：{list9_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年在岗职工平均工资：{list9_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年在岗职工平均工资：{list9_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年在岗职工平均工资：{list9_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年在岗职工平均工资：{list9_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年在岗职工平均工资：{list9_2022} 已成功爬取\n')
#         i += 1
#     print("2003年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2003))
#     print("2004年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2004))
#     print("2005年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2005))
#     print("2006年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2006))
#     print("2007年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2007))
#     print("2008年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2008))
#     print("2009年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2009))
#     print("2010年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2010))
#     print("2011年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2011))
#     print("2012年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2012))
#     print("2013年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2013))
#     print("2014年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2014))
#     print("2015年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2015))
#     print("2016年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2016))
#     print("2017年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2017))
#     print("2018年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2018))
#     print("2019年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2019))
#     print("2020年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2020))
#     print("2021年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2021))
#     print("2022年在岗职工平均工资：" + str(Average_salary_of_on_duty_employees_2022))
#     time.sleep(0.47)
#
#
#     # 普通高等学校在校学生数
#     element = driver.find_element_by_id('treeZhiBiao_9_span')
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2003 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2004 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2005 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2006 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2007 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2008 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2009 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2010 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2011 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2012 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2013 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2014 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2015 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2016 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2017 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2018 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2019 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2020 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2021 = []
#     Number_of_students_enrolled_in_regular_higher_education_institutions_2022 = []
#     i = 1
#     while (i < 37):
#         list10_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list10_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list10_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list10_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list10_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list10_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list10_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list10_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list10_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list10_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list10_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list10_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list10_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list10_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list10_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list10_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list10_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list10_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list10_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list10_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2003.append(list10_2003)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2004.append(list10_2004)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2005.append(list10_2005)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2006.append(list10_2006)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2007.append(list10_2007)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2008.append(list10_2008)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2009.append(list10_2009)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2010.append(list10_2010)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2011.append(list10_2011)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2012.append(list10_2012)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2013.append(list10_2013)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2014.append(list10_2014)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2015.append(list10_2015)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2016.append(list10_2016)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2017.append(list10_2017)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2018.append(list10_2018)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2019.append(list10_2019)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2020.append(list10_2020)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2021.append(list10_2021)
#         Number_of_students_enrolled_in_regular_higher_education_institutions_2022.append(list10_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年普通高等学校在校学生数：{list10_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年普通高等学校在校学生数：{list10_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年普通高等学校在校学生数：{list10_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年普通高等学校在校学生数：{list10_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年普通高等学校在校学生数：{list10_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年普通高等学校在校学生数：{list10_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年普通高等学校在校学生数：{list10_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年普通高等学校在校学生数：{list10_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年普通高等学校在校学生数：{list10_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年普通高等学校在校学生数：{list10_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年普通高等学校在校学生数：{list10_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年普通高等学校在校学生数：{list10_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年普通高等学校在校学生数：{list10_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年普通高等学校在校学生数：{list10_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年普通高等学校在校学生数：{list10_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年普通高等学校在校学生数：{list10_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年普通高等学校在校学生数：{list10_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年普通高等学校在校学生数：{list10_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年普通高等学校在校学生数：{list10_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年普通高等学校在校学生数：{list10_2022} 已成功爬取\n')
#         i += 1
#     print("2003年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2003))
#     print("2004年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2004))
#     print("2005年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2005))
#     print("2006年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2006))
#     print("2007年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2007))
#     print("2008年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2008))
#     print("2009年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2009))
#     print("2010年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2010))
#     print("2011年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2011))
#     print("2012年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2012))
#     print("2013年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2013))
#     print("2014年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2014))
#     print("2015年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2015))
#     print("2016年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2016))
#     print("2017年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2017))
#     print("2018年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2018))
#     print("2019年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2019))
#     print("2020年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2020))
#     print("2021年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2021))
#     print("2022年普通高等学校在校学生数：" + str(Number_of_students_enrolled_in_regular_higher_education_institutions_2022))
#     time.sleep(0.47)
#
#
#
#
#     # 医院、卫生院数
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0802\",\"name\":\"医院数(个)\",\"sort\":\"1\"}']")
#     element.click()
#     Number_of_hospitals_and_health_centers_2003 = []
#     Number_of_hospitals_and_health_centers_2004 = []
#     Number_of_hospitals_and_health_centers_2005 = []
#     Number_of_hospitals_and_health_centers_2006 = []
#     Number_of_hospitals_and_health_centers_2007 = []
#     Number_of_hospitals_and_health_centers_2008 = []
#     Number_of_hospitals_and_health_centers_2009 = []
#     Number_of_hospitals_and_health_centers_2010 = []
#     Number_of_hospitals_and_health_centers_2011 = []
#     Number_of_hospitals_and_health_centers_2012 = []
#     Number_of_hospitals_and_health_centers_2013 = []
#     Number_of_hospitals_and_health_centers_2014 = []
#     Number_of_hospitals_and_health_centers_2015 = []
#     Number_of_hospitals_and_health_centers_2016 = []
#     Number_of_hospitals_and_health_centers_2017 = []
#     Number_of_hospitals_and_health_centers_2018 = []
#     Number_of_hospitals_and_health_centers_2019 = []
#     Number_of_hospitals_and_health_centers_2020 = []
#     Number_of_hospitals_and_health_centers_2021 = []
#     Number_of_hospitals_and_health_centers_2022 = []
#     i = 1
#     while (i < 37):
#         list11_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list11_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list11_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list11_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list11_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list11_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list11_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list11_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list11_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list11_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list11_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list11_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list11_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list11_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list11_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list11_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list11_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list11_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list11_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list11_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Number_of_hospitals_and_health_centers_2003.append(list11_2003)
#         Number_of_hospitals_and_health_centers_2004.append(list11_2004)
#         Number_of_hospitals_and_health_centers_2005.append(list11_2005)
#         Number_of_hospitals_and_health_centers_2006.append(list11_2006)
#         Number_of_hospitals_and_health_centers_2007.append(list11_2007)
#         Number_of_hospitals_and_health_centers_2008.append(list11_2008)
#         Number_of_hospitals_and_health_centers_2009.append(list11_2009)
#         Number_of_hospitals_and_health_centers_2010.append(list11_2010)
#         Number_of_hospitals_and_health_centers_2011.append(list11_2011)
#         Number_of_hospitals_and_health_centers_2012.append(list11_2012)
#         Number_of_hospitals_and_health_centers_2013.append(list11_2013)
#         Number_of_hospitals_and_health_centers_2014.append(list11_2014)
#         Number_of_hospitals_and_health_centers_2015.append(list11_2015)
#         Number_of_hospitals_and_health_centers_2016.append(list11_2016)
#         Number_of_hospitals_and_health_centers_2017.append(list11_2017)
#         Number_of_hospitals_and_health_centers_2018.append(list11_2018)
#         Number_of_hospitals_and_health_centers_2019.append(list11_2019)
#         Number_of_hospitals_and_health_centers_2020.append(list11_2020)
#         Number_of_hospitals_and_health_centers_2021.append(list11_2021)
#         Number_of_hospitals_and_health_centers_2022.append(list11_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年医院、卫生院数：{list11_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2004年医院、卫生院数：{list11_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年医院、卫生院数：{list11_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年医院、卫生院数：{list11_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年医院、卫生院数：{list11_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年医院、卫生院数：{list11_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年医院、卫生院数：{list11_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年医院、卫生院数：{list11_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年医院、卫生院数：{list11_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年医院、卫生院数：{list11_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年医院、卫生院数：{list11_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年医院、卫生院数：{list11_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年医院、卫生院数：{list11_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年医院、卫生院数：{list11_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年医院、卫生院数：{list11_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年医院、卫生院数：{list11_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年医院、卫生院数：{list11_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年医院、卫生院数：{list11_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年医院、卫生院数：{list11_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年医院、卫生院数：{list11_2022} 已成功爬取\n')
#         i += 1
#     print("2003年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2003))
#     print("2004年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2004))
#     print("2005年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2005))
#     print("2006年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2006))
#     print("2007年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2007))
#     print("2008年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2008))
#     print("2009年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2009))
#     print("2010年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2010))
#     print("2011年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2011))
#     print("2012年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2012))
#     print("2013年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2013))
#     print("2014年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2014))
#     print("2015年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2015))
#     print("2016年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2016))
#     print("2017年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2017))
#     print("2018年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2018))
#     print("2019年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2019))
#     print("2020年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2020))
#     print("2021年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2021))
#     print("2022年医院、卫生院数：" + str(Number_of_hospitals_and_health_centers_2022))
#     time.sleep(0.47)
#
#
#
#
#
#     # 房地产开发投资额
#     element = driver.find_element_by_id('treeZhiBiao_5_span')
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     Real_estate_development_investment_amount_2003 = []
#     Real_estate_development_investment_amount_2004 = []
#     Real_estate_development_investment_amount_2005 = []
#     Real_estate_development_investment_amount_2006 = []
#     Real_estate_development_investment_amount_2007 = []
#     Real_estate_development_investment_amount_2008 = []
#     Real_estate_development_investment_amount_2009 = []
#     Real_estate_development_investment_amount_2010 = []
#     Real_estate_development_investment_amount_2011 = []
#     Real_estate_development_investment_amount_2012 = []
#     Real_estate_development_investment_amount_2013 = []
#     Real_estate_development_investment_amount_2014 = []
#     Real_estate_development_investment_amount_2015 = []
#     Real_estate_development_investment_amount_2016 = []
#     Real_estate_development_investment_amount_2017 = []
#     Real_estate_development_investment_amount_2018 = []
#     Real_estate_development_investment_amount_2019 = []
#     Real_estate_development_investment_amount_2020 = []
#     Real_estate_development_investment_amount_2021 = []
#     Real_estate_development_investment_amount_2022 = []
#     i = 1
#     while (i < 37):
#         list12_2003 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[22]')[0].text
#         list12_2004 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[21]')[0].text
#         list12_2005 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[20]')[0].text
#         list12_2006 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[19]')[0].text
#         list12_2007 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[18]')[0].text
#         list12_2008 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[17]')[0].text
#         list12_2009 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[16]')[0].text
#         list12_2010 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[15]')[0].text
#         list12_2011 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[14]')[0].text
#         list12_2012 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[13]')[0].text
#         list12_2013 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[12]')[0].text
#         list12_2014 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[11]')[0].text
#         list12_2015 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[10]')[0].text
#         list12_2016 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[9]')[0].text
#         list12_2017 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[8]')[0].text
#         list12_2018 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[7]')[0].text
#         list12_2019 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[6]')[0].text
#         list12_2020 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[5]')[0].text
#         list12_2021 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[4]')[0].text
#         list12_2022 = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[{i}]/td[3]')[0].text
#         Real_estate_development_investment_amount_2003.append(list12_2003)
#         Real_estate_development_investment_amount_2004.append(list12_2004)
#         Real_estate_development_investment_amount_2005.append(list12_2005)
#         Real_estate_development_investment_amount_2006.append(list12_2006)
#         Real_estate_development_investment_amount_2007.append(list12_2007)
#         Real_estate_development_investment_amount_2008.append(list12_2008)
#         Real_estate_development_investment_amount_2009.append(list12_2009)
#         Real_estate_development_investment_amount_2010.append(list12_2010)
#         Real_estate_development_investment_amount_2011.append(list12_2011)
#         Real_estate_development_investment_amount_2012.append(list12_2012)
#         Real_estate_development_investment_amount_2013.append(list12_2013)
#         Real_estate_development_investment_amount_2014.append(list12_2014)
#         Real_estate_development_investment_amount_2015.append(list12_2015)
#         Real_estate_development_investment_amount_2016.append(list12_2016)
#         Real_estate_development_investment_amount_2017.append(list12_2017)
#         Real_estate_development_investment_amount_2018.append(list12_2018)
#         Real_estate_development_investment_amount_2019.append(list12_2019)
#         Real_estate_development_investment_amount_2020.append(list12_2020)
#         Real_estate_development_investment_amount_2021.append(list12_2021)
#         Real_estate_development_investment_amount_2022.append(list12_2022)
#         print(f'第{i}项数据【地区：{area[i-1]}】：2003年房地产开发投资额：{list12_2003} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年房地产开发投资额：{list12_2004} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2005年房地产开发投资额：{list12_2005} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2006年房地产开发投资额：{list12_2006} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2007年房地产开发投资额：{list12_2007} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2008年房地产开发投资额：{list12_2008} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2009年房地产开发投资额：{list12_2009} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2010年房地产开发投资额：{list12_2010} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2011年房地产开发投资额：{list12_2011} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2012年房地产开发投资额：{list12_2012} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2013年房地产开发投资额：{list12_2013} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2014年房地产开发投资额：{list12_2014} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2015年房地产开发投资额：{list12_2015} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2016年房地产开发投资额：{list12_2016} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2017年房地产开发投资额：{list12_2017} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2018年房地产开发投资额：{list12_2018} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2019年房地产开发投资额：{list12_2019} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2020年房地产开发投资额：{list12_2020} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2021年房地产开发投资额：{list12_2021} 已成功爬取\n')
#         print(f'第{i}项数据【地区：{area[i-1]}】：2022年房地产开发投资额：{list12_2022} 已成功爬取\n')
#         i += 1
#     print("2003年房地产开发投资额:" + str(Real_estate_development_investment_amount_2003))
#     print("2004年房地产开发投资额:" + str(Real_estate_development_investment_amount_2004))
#     print("2005年房地产开发投资额:" + str(Real_estate_development_investment_amount_2005))
#     print("2006年房地产开发投资额:" + str(Real_estate_development_investment_amount_2006))
#     print("2007年房地产开发投资额:" + str(Real_estate_development_investment_amount_2007))
#     print("2008年房地产开发投资额:" + str(Real_estate_development_investment_amount_2008))
#     print("2009年房地产开发投资额:" + str(Real_estate_development_investment_amount_2009))
#     print("2010年房地产开发投资额:" + str(Real_estate_development_investment_amount_2010))
#     print("2011年房地产开发投资额:" + str(Real_estate_development_investment_amount_2011))
#     print("2012年房地产开发投资额:" + str(Real_estate_development_investment_amount_2012))
#     print("2013年房地产开发投资额:" + str(Real_estate_development_investment_amount_2013))
#     print("2014年房地产开发投资额:" + str(Real_estate_development_investment_amount_2014))
#     print("2015年房地产开发投资额:" + str(Real_estate_development_investment_amount_2015))
#     print("2016年房地产开发投资额:" + str(Real_estate_development_investment_amount_2016))
#     print("2017年房地产开发投资额:" + str(Real_estate_development_investment_amount_2017))
#     print("2018年房地产开发投资额:" + str(Real_estate_development_investment_amount_2018))
#     print("2019年房地产开发投资额:" + str(Real_estate_development_investment_amount_2019))
#     print("2020年房地产开发投资额:" + str(Real_estate_development_investment_amount_2020))
#     print("2021年房地产开发投资额:" + str(Real_estate_development_investment_amount_2021))
#     print("2022年房地产开发投资额:" + str(Real_estate_development_investment_amount_2022))
#     time.sleep(0.47)
#
#     csv_file_2003 = "2003_data.csv"
#     csv_file_2004 = "2004_data.csv"
#     csv_file_2005 = "2005_data.csv"
#     csv_file_2006 = "2006_data.csv"
#     csv_file_2007 = "2007_data.csv"
#     csv_file_2008 = "2008_data.csv"
#     csv_file_2009 = "2009_data.csv"
#     csv_file_2010 = "2010_data.csv"
#     csv_file_2011 = "2011_data.csv"
#     csv_file_2012 = "2012_data.csv"
#     csv_file_2013 = "2013_data.csv"
#     csv_file_2014 = "2014_data.csv"
#     csv_file_2015 = "2015_data.csv"
#     csv_file_2016 = "2016_data.csv"
#     csv_file_2017 = "2017_data.csv"
#     csv_file_2018 = "2018_data.csv"
#     csv_file_2019 = "2019_data.csv"
#     csv_file_2020 = "2020_data.csv"
#     csv_file_2021 = "2021_data.csv"
#     csv_file_2022 = "2022_data.csv"
#
#     # 写入2003_data.csv
#     with open(csv_file_2003, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2003",
#                 Regional_Gross_Domestic_Product_2003[i],
#                 Value_added_of_the_primary_industry_2003[i],
#                 Value_added_of_the_Second_industry_2003[i],
#                 Value_added_of_the_third_industry_2003[i],
#                 Total_retail_sales_of_social_goods_2003[i],
#                 Total_import_and_export_value_of_goods_2003[i],
#                 Total_Population_2003[i],
#                 Average_salary_of_on_duty_employees_2003[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2003[i],
#                 Number_of_hospitals_and_health_centers_2003[i],
#                 Real_estate_development_investment_amount_2003[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2004_data.csv
#     with open(csv_file_2004, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2004",
#                 Regional_Gross_Domestic_Product_2004[i],
#                 Value_added_of_the_primary_industry_2004[i],
#                 Value_added_of_the_Second_industry_2004[i],
#                 Value_added_of_the_third_industry_2004[i],
#                 Total_retail_sales_of_social_goods_2004[i],
#                 Total_import_and_export_value_of_goods_2004[i],
#                 Total_Population_2004[i],
#                 Average_salary_of_on_duty_employees_2004[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2004[i],
#                 Number_of_hospitals_and_health_centers_2004[i],
#                 Real_estate_development_investment_amount_2004[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2005_data.csv
#     with open(csv_file_2005, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2005",
#                 Regional_Gross_Domestic_Product_2005[i],
#                 Value_added_of_the_primary_industry_2005[i],
#                 Value_added_of_the_Second_industry_2005[i],
#                 Value_added_of_the_third_industry_2005[i],
#                 Total_retail_sales_of_social_goods_2005[i],
#                 Total_import_and_export_value_of_goods_2005[i],
#                 Total_Population_2005[i],
#                 Average_salary_of_on_duty_employees_2005[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2005[i],
#                 Number_of_hospitals_and_health_centers_2005[i],
#                 Real_estate_development_investment_amount_2005[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2006_data.csv
#     with open(csv_file_2006, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2006",
#                 Regional_Gross_Domestic_Product_2006[i],
#                 Value_added_of_the_primary_industry_2006[i],
#                 Value_added_of_the_Second_industry_2006[i],
#                 Value_added_of_the_third_industry_2006[i],
#                 Total_retail_sales_of_social_goods_2006[i],
#                 Total_import_and_export_value_of_goods_2006[i],
#                 Total_Population_2006[i],
#                 Average_salary_of_on_duty_employees_2006[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2006[i],
#                 Number_of_hospitals_and_health_centers_2006[i],
#                 Real_estate_development_investment_amount_2006[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2007_data.csv
#     with open(csv_file_2007, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2007",
#                 Regional_Gross_Domestic_Product_2007[i],
#                 Value_added_of_the_primary_industry_2007[i],
#                 Value_added_of_the_Second_industry_2007[i],
#                 Value_added_of_the_third_industry_2007[i],
#                 Total_retail_sales_of_social_goods_2007[i],
#                 Total_import_and_export_value_of_goods_2007[i],
#                 Total_Population_2007[i],
#                 Average_salary_of_on_duty_employees_2007[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2007[i],
#                 Number_of_hospitals_and_health_centers_2007[i],
#                 Real_estate_development_investment_amount_2007[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2008_data.csv
#     with open(csv_file_2008, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2008",
#                 Regional_Gross_Domestic_Product_2008[i],
#                 Value_added_of_the_primary_industry_2008[i],
#                 Value_added_of_the_Second_industry_2008[i],
#                 Value_added_of_the_third_industry_2008[i],
#                 Total_retail_sales_of_social_goods_2008[i],
#                 Total_import_and_export_value_of_goods_2008[i],
#                 Total_Population_2008[i],
#                 Average_salary_of_on_duty_employees_2008[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2008[i],
#                 Number_of_hospitals_and_health_centers_2008[i],
#                 Real_estate_development_investment_amount_2008[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2009_data.csv
#     with open(csv_file_2009, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2009",
#                 Regional_Gross_Domestic_Product_2009[i],
#                 Value_added_of_the_primary_industry_2009[i],
#                 Value_added_of_the_Second_industry_2009[i],
#                 Value_added_of_the_third_industry_2009[i],
#                 Total_retail_sales_of_social_goods_2009[i],
#                 Total_import_and_export_value_of_goods_2009[i],
#                 Total_Population_2009[i],
#                 Average_salary_of_on_duty_employees_2009[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2009[i],
#                 Number_of_hospitals_and_health_centers_2009[i],
#                 Real_estate_development_investment_amount_2009[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2010_data.csv
#     with open(csv_file_2010, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2010",
#                 Regional_Gross_Domestic_Product_2010[i],
#                 Value_added_of_the_primary_industry_2010[i],
#                 Value_added_of_the_Second_industry_2010[i],
#                 Value_added_of_the_third_industry_2010[i],
#                 Total_retail_sales_of_social_goods_2010[i],
#                 Total_import_and_export_value_of_goods_2010[i],
#                 Total_Population_2010[i],
#                 Average_salary_of_on_duty_employees_2010[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2010[i],
#                 Number_of_hospitals_and_health_centers_2010[i],
#                 Real_estate_development_investment_amount_2010[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2011_data.csv
#     with open(csv_file_2011, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2011",
#                 Regional_Gross_Domestic_Product_2011[i],
#                 Value_added_of_the_primary_industry_2011[i],
#                 Value_added_of_the_Second_industry_2011[i],
#                 Value_added_of_the_third_industry_2011[i],
#                 Total_retail_sales_of_social_goods_2011[i],
#                 Total_import_and_export_value_of_goods_2011[i],
#                 Total_Population_2011[i],
#                 Average_salary_of_on_duty_employees_2011[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2011[i],
#                 Number_of_hospitals_and_health_centers_2011[i],
#                 Real_estate_development_investment_amount_2011[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2012_data.csv
#     with open(csv_file_2012, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2012",
#                 Regional_Gross_Domestic_Product_2012[i],
#                 Value_added_of_the_primary_industry_2012[i],
#                 Value_added_of_the_Second_industry_2012[i],
#                 Value_added_of_the_third_industry_2012[i],
#                 Total_retail_sales_of_social_goods_2012[i],
#                 Total_import_and_export_value_of_goods_2012[i],
#                 Total_Population_2012[i],
#                 Average_salary_of_on_duty_employees_2012[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2012[i],
#                 Number_of_hospitals_and_health_centers_2012[i],
#                 Real_estate_development_investment_amount_2012[i]
#             ]
#             writer.writerow(row)
#
#
#     # 写入2013_data.csv
#     with open(csv_file_2013, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2013",
#                 Regional_Gross_Domestic_Product_2013[i],
#                 Value_added_of_the_primary_industry_2013[i],
#                 Value_added_of_the_Second_industry_2013[i],
#                 Value_added_of_the_third_industry_2013[i],
#                 Total_retail_sales_of_social_goods_2013[i],
#                 Total_import_and_export_value_of_goods_2013[i],
#                 Total_Population_2013[i],
#                 Average_salary_of_on_duty_employees_2013[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2013[i],
#                 Number_of_hospitals_and_health_centers_2013[i],
#                 Real_estate_development_investment_amount_2013[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2014_data.csv
#     with open(csv_file_2014, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2014",
#                 Regional_Gross_Domestic_Product_2014[i],
#                 Value_added_of_the_primary_industry_2014[i],
#                 Value_added_of_the_Second_industry_2014[i],
#                 Value_added_of_the_third_industry_2014[i],
#                 Total_retail_sales_of_social_goods_2014[i],
#                 Total_import_and_export_value_of_goods_2014[i],
#                 Total_Population_2014[i],
#                 Average_salary_of_on_duty_employees_2014[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2014[i],
#                 Number_of_hospitals_and_health_centers_2014[i],
#                 Real_estate_development_investment_amount_2014[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2015_data.csv
#     with open(csv_file_2015, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2015",
#                 Regional_Gross_Domestic_Product_2015[i],
#                 Value_added_of_the_primary_industry_2015[i],
#                 Value_added_of_the_Second_industry_2015[i],
#                 Value_added_of_the_third_industry_2015[i],
#                 Total_retail_sales_of_social_goods_2015[i],
#                 Total_import_and_export_value_of_goods_2015[i],
#                 Total_Population_2015[i],
#                 Average_salary_of_on_duty_employees_2015[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2015[i],
#                 Number_of_hospitals_and_health_centers_2015[i],
#                 Real_estate_development_investment_amount_2015[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2016_data.csv
#     with open(csv_file_2016, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2016",
#                 Regional_Gross_Domestic_Product_2016[i],
#                 Value_added_of_the_primary_industry_2016[i],
#                 Value_added_of_the_Second_industry_2016[i],
#                 Value_added_of_the_third_industry_2016[i],
#                 Total_retail_sales_of_social_goods_2016[i],
#                 Total_import_and_export_value_of_goods_2016[i],
#                 Total_Population_2016[i],
#                 Average_salary_of_on_duty_employees_2016[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2016[i],
#                 Number_of_hospitals_and_health_centers_2016[i],
#                 Real_estate_development_investment_amount_2016[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2017_data.csv
#     with open(csv_file_2017, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(
#             ['地区', '年份', '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值', '社会商品零售总额',
#              '货物进出口总额', '年末总人口', '在岗职工平均工资', '普通高等学校在校学生数', '医院、卫生院数',
#              '房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2017",
#                 Regional_Gross_Domestic_Product_2017[i],
#                 Value_added_of_the_primary_industry_2017[i],
#                 Value_added_of_the_Second_industry_2017[i],
#                 Value_added_of_the_third_industry_2017[i],
#                 Total_retail_sales_of_social_goods_2017[i],
#                 Total_import_and_export_value_of_goods_2017[i],
#                 Total_Population_2017[i],
#                 Average_salary_of_on_duty_employees_2017[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2017[i],
#                 Number_of_hospitals_and_health_centers_2017[i],
#                 Real_estate_development_investment_amount_2017[i]
#             ]
#             writer.writerow(row)
#
#
#     # 写入2018_data.csv
#     with open(csv_file_2018,'w',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['地区','年份','国内生产总值','第一产业增加值','第二产业增加值','第三产业增加值','社会商品零售总额','货物进出口总额','年末总人口','在岗职工平均工资','普通高等学校在校学生数','医院、卫生院数','房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2018",
#                 Regional_Gross_Domestic_Product_2018[i],
#                 Value_added_of_the_primary_industry_2018[i],
#                 Value_added_of_the_Second_industry_2018[i],
#                 Value_added_of_the_third_industry_2018[i],
#                 Total_retail_sales_of_social_goods_2018[i],
#                 Total_import_and_export_value_of_goods_2018[i],
#                 Total_Population_2018[i],
#                 Average_salary_of_on_duty_employees_2018[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2018[i],
#                 Number_of_hospitals_and_health_centers_2018[i],
#                 Real_estate_development_investment_amount_2018[i]
#             ]
#             writer.writerow(row)
#
#
#     # 写入2019_data.csv
#     with open(csv_file_2019,'w',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['地区','年份','国内生产总值','第一产业增加值','第二产业增加值','第三产业增加值','社会商品零售总额','货物进出口总额','年末总人口','在岗职工平均工资','普通高等学校在校学生数','医院、卫生院数','房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2019",
#                 Regional_Gross_Domestic_Product_2019[i],
#                 Value_added_of_the_primary_industry_2019[i],
#                 Value_added_of_the_Second_industry_2019[i],
#                 Value_added_of_the_third_industry_2019[i],
#                 Total_retail_sales_of_social_goods_2019[i],
#                 Total_import_and_export_value_of_goods_2019[i],
#                 Total_Population_2019[i],
#                 Average_salary_of_on_duty_employees_2019[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2019[i],
#                 Number_of_hospitals_and_health_centers_2019[i],
#                 Real_estate_development_investment_amount_2019[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2020_data.csv
#     with open(csv_file_2020,'w',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['地区','年份','国内生产总值','第一产业增加值','第二产业增加值','第三产业增加值','社会商品零售总额','货物进出口总额','年末总人口','在岗职工平均工资','普通高等学校在校学生数','医院、卫生院数','房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2020",
#                 Regional_Gross_Domestic_Product_2020[i],
#                 Value_added_of_the_primary_industry_2020[i],
#                 Value_added_of_the_Second_industry_2020[i],
#                 Value_added_of_the_third_industry_2020[i],
#                 Total_retail_sales_of_social_goods_2020[i],
#                 Total_import_and_export_value_of_goods_2020[i],
#                 Total_Population_2020[i],
#                 Average_salary_of_on_duty_employees_2020[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2020[i],
#                 Number_of_hospitals_and_health_centers_2020[i],
#                 Real_estate_development_investment_amount_2020[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2021_data.csv
#     with open(csv_file_2021,'w',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['地区','年份','国内生产总值','第一产业增加值','第二产业增加值','第三产业增加值','社会商品零售总额','货物进出口总额','年末总人口','在岗职工平均工资','普通高等学校在校学生数','医院、卫生院数','房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2021",
#                 Regional_Gross_Domestic_Product_2021[i],
#                 Value_added_of_the_primary_industry_2021[i],
#                 Value_added_of_the_Second_industry_2021[i],
#                 Value_added_of_the_third_industry_2021[i],
#                 Total_retail_sales_of_social_goods_2021[i],
#                 Total_import_and_export_value_of_goods_2021[i],
#                 Total_Population_2021[i],
#                 Average_salary_of_on_duty_employees_2021[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2021[i],
#                 Number_of_hospitals_and_health_centers_2021[i],
#                 Real_estate_development_investment_amount_2021[i]
#             ]
#             writer.writerow(row)
#
#     # 写入2022_data.csv
#     with open(csv_file_2022,'w',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['地区','年份','国内生产总值','第一产业增加值','第二产业增加值','第三产业增加值','社会商品零售总额','货物进出口总额','年末总人口','在岗职工平均工资','普通高等学校在校学生数','医院、卫生院数','房地产开发投资额'])
#         for i in range(len(area)):
#             row = [
#                 area[i],
#                 "2022",
#                 Regional_Gross_Domestic_Product_2022[i],
#                 Value_added_of_the_primary_industry_2022[i],
#                 Value_added_of_the_Second_industry_2022[i],
#                 Value_added_of_the_third_industry_2022[i],
#                 Total_retail_sales_of_social_goods_2022[i],
#                 Total_import_and_export_value_of_goods_2022[i],
#                 Total_Population_2022[i],
#                 Average_salary_of_on_duty_employees_2022[i],
#                 Number_of_students_enrolled_in_regular_higher_education_institutions_2022[i],
#                 Number_of_hospitals_and_health_centers_2022[i],
#                 Real_estate_development_investment_amount_2022[i]
#             ]
#             writer.writerow(row)
#
#     driver.quit()
#


# data = {'2003': ['84.10', '89.90', '', '', '', '', '', '', '', '79.00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '332.90', '', '', '', '6.40', '', '', '', '', ''], '2004': ['85.40', '105.30', '', '', '', '', '', '', '', '81.40', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '420.40', '', '', '', '', '', '', '', '', ''], '2005': ['86.90', '112.40', '', '', '', '', '', '', '', '88.10', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '455.10', '', '', '', '', '', '', '', '', ''], '2006': ['87.20', '103.40', '', '', '', '', '', '', '', '91.60', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '379.70', '', '', '', '', '', '', '', '', ''], '2007': ['99.40', '107.50', '275.74', '19.64', '62.14', '166.15', '249.29', '200.03', '347.68', '99.40', '86.44', '163.47', '151.28', '77.28', '204.24', '18.51', '86.73', '150.30', '203.59', '79.38', '129.15', '138.80', '149.87', '6.94', '157.94', '26.81', '469.40', '235.10', '45.58', '93.95', '7.42', '82.51', '26.09', '14.93', '24.44', '16.27'], '2008': ['111.40', '116.60', '309.69', '21.04', '75.16', '183.68', '289.15', '217.82', '390.25', '109.40', '93.00', '178.64', '167.36', '105.20', '234.90', '21.50', '101.48', '175.01', '223.40', '94.70', '144.70', '172.38', '167.72', '6.66', '203.19', '31.40', '555.10', '270.15', '47.21', '104.90', '8.12', '103.45', '28.10', '19.21', '30.23', '17.90'], '2009': ['116.80', '119.50', '308.31', '28.56', '78.09', '207.07', '313.44', '223.93', '384.87', '112.40', '129.18', '190.51', '183.54', '108.70', '242.00', '20.49', '111.90', '187.07', '230.25', '103.09', '149.06', '179.40', '172.28', '6.69', '212.38', '34.09', '581.10', '267.77', '50.08', '114.09', '9.14', '110.38', '30.55', '19.18', '32.33', '16.37'], '2010': ['122.80', '131.70', '369.60', '30.30', '91.30', '232.70', '345.10', '252.80', '412.70', '114.50', '142.30', '208.40', '219.10', '132.70', '282.70', '23.10', '120.60', '215.20', '277.00', '124.60', '170.00', '202.00', '188.60', '6.50', '244.40', '38.20', '649.50', '285.10', '57.10', '120.30', '', '140.10', '33.80', '24.50', '40.50', '19.90'], '2011': ['134.50', '141.10', '415.00', '33.85', '109.44', '279.06', '395.72', '290.12', '447.21', '126.40', '164.28', '236.77', '255.23', '208.20', '325.09', '24.68', '134.92', '237.86', '306.38', '131.66', '198.70', '243.38', '204.54', '6.55', '305.50', '47.70', '794.10', '327.34', '62.55', '133.83', '9.99', '173.14', '40.00', '27.41', '47.05', '22.06'], '2012': ['148.40', '147.90', '452.20', '36.00', '120.50', '315.20', '451.40', '317.10', '506.80', '129.30', '185.10', '255.10', '268.50', '229.10', '367.60', '25.20', '147.20', '252.90', '324.40', '142.40', '301.20', '272.30', '213.80', '6.30', '323.00', '55.90', '879.70', '348.10', '72.30', '159.20', '10.80', '195.60', '44.60', '31.20', '51.00', '25.00'], '2013': ['159.80', '154.80', '488.71', '38.61', '134.72', '321.61', '477.59', '332.05', '587.12', '131.60', '204.64', '265.42', '276.35', '247.21', '402.26', '25.99', '157.24', '284.71', '352.41', '147.00', '335.40', '294.55', '228.87', '5.25', '349.93', '58.10', '941.20', '353.17', '81.52', '169.68', '11.73', '217.76', '49.12', '36.10', '55.42', '26.31'], '2014': ['159.20', '158.80', '487.51', '38.86', '125.46', '325.29', '441.83', '332.03', '626.51', '132.00', '214.25', '274.35', '275.70', '257.63', '415.91', '23.73', '162.72', '290.29', '349.62', '147.15', '350.06', '311.90', '218.70', '5.58', '369.57', '57.07', '990.80', '357.07', '108.02', '181.56', '12.94', '214.55', '52.44', '37.37', '52.80', '27.43'], '2015': ['140.40', '162.30', '494.44', '37.40', '126.23', '341.43', '453.25', '343.24', '672.52', '125.50', '232.39', '287.95', '284.68', '263.43', '434.69', '23.93', '171.26', '305.39', '363.98', '150.92', '359.81', '341.78', '226.84', '6.65', '370.35', '57.09', '1067.70', '373.15', '129.89', '188.10', '13.80', '220.20', '56.22', '37.46', '58.62', '31.64'], '2016': ['129.80', '168.50', '480.74', '38.72', '113.61', '266.23', '463.09', '323.27', '691.31', '114.30', '252.07', '304.34', '302.29', '270.43', '492.09', '23.08', '181.60', '317.00', '371.42', '156.60', '390.73', '370.53', '238.48', '7.80', '395.89', '63.89', '1237.00', '474.64', '137.04', '200.38', '15.13', '232.14', '60.45', '39.19', '58.56', '28.03'], '2017': ['121.90', '169.00', '480.53', '40.82', '107.74', '268.22', '477.10', '315.07', '688.79', '110.80', '263.01', '311.08', '305.80', '272.75', '461.20', '23.50', '192.13', '317.40', '380.97', '158.60', '408.20', '379.45', '233.49', '19.57', '404.18', '62.51', '1276.10', '500.87', '147.33', '210.13', '17.54', '281.12', '61.47', '41.80', '61.37', '29.62'], '2018': ['120.60', '175.30', '420.45', '41.05', '108.40', '260.11', '442.70', '301.90', '525.49', '104.80', '273.42', '305.51', '305.96', '277.59', '494.66', '24.40', '190.68', '272.42', '386.91', '147.05', '362.00', '318.73', '223.44', '22.09', '421.31', '63.96', '1378.70', '522.59', '153.10', '222.16', '18.29', '258.82', '42.98', '46.08', '67.31', '25.32'], '2019': ['114.38', '185.41', '449.50', '42.48', '114.21', '284.03', '458.52', '348.07', '569.54', '107.06', '287.85', '325.70', '322.27', '291.86', '526.47', '26.49', '212.89', '343.06', '409.98', '140.88', '378.99', '359.69', '251.37', '25.20', '507.27', '71.18', '1551.59', '612.18', '161.34', '270.29', '20.10', '279.13', '51.67', '51.34', '64.71', '27.69'], '2020': ['108.28', '210.34', '499.00', '32.00', '127.00', '304.00', '459.00', '534.00', '616.00', '107.68', '297.00', '326.00', '339.00', '332.00', '561.00', '29.00', '235.00', '362.00', '425.00', '157.00', '402.00', '424.00', '288.00', '26.00', '534.00', '80.00', '1803.54', '655.00', '178.00', '312.00', '23.00', '313.00', '57.00', '57.00', '75.00', '27.00'], '2021': ['111.41', '265.90', '504.78', '44.80', '137.14', '326.00', '513.33', '523.70', '628.18', '96.09', '304.00', '333.49', '356.16', '351.05', '637.03', '29.06', '238.31', '408.77', '470.00', '181.69', '444.21', '425.56', '306.41', '26.59', '606.76', '85.43', '1921.91', '582.79', '193.44', '333.12', '24.45', '308.82', '62.52', '58.93', '83.83', '28.10'], '2022': ['111.50', '273.20', '558.29', '48.07', '160.55', '335.19', '562.97', '551.32', '672.13', '100.00', '315.56', '345.97', '381.99', '379.20', '683.38', '29.27', '248.60', '420.52', '478.05', '185.60', '475.79', '451.30', '318.31', '25.64', '601.51', '99.19', '2012.60', '588.42', '203.60', '326.96', '26.74', '323.58', '64.97', '62.96', '91.80', '30.98']}
# print(data['2003'])

# import nete
# function_names = [name for name in dir(nete) if callable(getattr(nete, name))]
# print(function_names)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# def start():
#     # 创建ChromeOptions对象
#     chrome_options = Options()
#
#     # 禁用SSL证书验证
#     chrome_options.add_argument('--ignore-ssl-errors=yes')
#     chrome_options.add_argument('--ignore-certificate-errors')
#
#     url = "https://data.stats.gov.cn/easyquery.htm?cn=E0105"
#     driver = webdriver.Chrome(options=chrome_options)
#     # driver.minimize_window()
#     driver.get(url)
#
#     element = driver.find_element_by_id('treeZhiBiao_3_span')
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#
#     # 点击小类指标标签
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"A0102\",\"name\":\"第一产业增加值(亿元)\",\"sort\":\"1\"}']")
#     element.click()
#     time.sleep(2.5)
#
# if __name__ == "__main__":
#     start()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# def start():
#     # 创建ChromeOptions对象
#     chrome_options = Options()
#
#     # 禁用SSL证书验证
#     chrome_options.add_argument('--ignore-ssl-errors=yes')
#     chrome_options.add_argument('--ignore-certificate-errors')
#
#     url = "https://data.stats.gov.cn/easyquery.htm?cn=E0105"
#     driver = webdriver.Chrome(options=chrome_options)
#     # driver.minimize_window()
#     driver.get(url)
#
#     element = driver.find_element_by_class_name('dtHead')
#     element.click()
#
#     # 点击序列标签
#     element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
#     element.click()
#     time.sleep(2.5)
#
# if __name__ == "__main__":
#     start()
#


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def start():
    # 创建ChromeOptions对象
    chrome_options = Options()

    # 禁用SSL证书验证
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    url = "https://data.stats.gov.cn/easyquery.htm?cn=E0105"
    driver = webdriver.Chrome(options=chrome_options)
    # driver.minimize_window()
    driver.get(url)

    element = driver.find_element_by_id('treeZhiBiao_3_span')
    element.click()
    element = driver.find_element_by_class_name('dtHead')
    element.click()
    element = driver.find_element_by_xpath("//li[@node='{\"code\":\"\",\"name\":\"序列\",\"sort\":\"4\"}']")
    element.click()


    data = driver.find_elements_by_xpath(f'//*[@id="table_main"]/tbody/tr[1]/td[3]')[0].text
    print(data)


if __name__ == "__main__":
    start()