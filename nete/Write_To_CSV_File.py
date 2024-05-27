import nete
from nete import *
import csv
import os
import sys


def Write_To_CSV_File(DirName,Name_List,Num_list):
    columns_list = ["城市","年份"]
    for i in Num_list:
        columns_list.append(Name_List[i-1])


    city_name = ['北京', '天津', '石家庄', '太原'
                ,'呼和浩特', '沈阳', '大连', '长春'
                , '哈尔滨', '上海', '南京', '杭州'
                , '宁波', '合肥', '福州', '厦门'
                , '南昌', '济南', '青岛', '郑州'
                , '武汉', '长沙', '广州', '深圳'
                , '南宁', '海口', '重庆', '成都'
                , '贵阳', '昆明', '拉萨', '西安'
                , '兰州', '西宁', '银川', '乌鲁木齐']

    all_data_2003 = []
    all_data_2004 = []
    all_data_2005 = []
    all_data_2006 = []
    all_data_2007 = []
    all_data_2008 = []
    all_data_2009 = []
    all_data_2010 = []
    all_data_2011 = []
    all_data_2012 = []
    all_data_2013 = []
    all_data_2014 = []
    all_data_2015 = []
    all_data_2016 = []
    all_data_2017 = []
    all_data_2018 = []
    all_data_2019 = []
    all_data_2020 = []
    all_data_2021 = []
    all_data_2022 = []
    for i in Num_list:
        func_name = f"data{i}"
        func = getattr(nete, func_name)
        data = func()
        all_data_2003.append(data['2003'])
        all_data_2004.append(data['2004'])
        all_data_2005.append(data['2005'])
        all_data_2006.append(data['2006'])
        all_data_2007.append(data['2007'])
        all_data_2008.append(data['2008'])
        all_data_2009.append(data['2009'])
        all_data_2010.append(data['2010'])
        all_data_2011.append(data['2011'])
        all_data_2012.append(data['2012'])
        all_data_2013.append(data['2013'])
        all_data_2014.append(data['2014'])
        all_data_2015.append(data['2015'])
        all_data_2016.append(data['2016'])
        all_data_2017.append(data['2017'])
        all_data_2018.append(data['2018'])
        all_data_2019.append(data['2019'])
        all_data_2020.append(data['2020'])
        all_data_2021.append(data['2021'])
        all_data_2022.append(data['2022'])

    dir = "../data/" + DirName
    os.mkdir(dir)
    csv_file = dir + "/" + DirName

    i = 0
    while i < 20:
        csv_file += f'_{i+2003}.data'
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns_list)
            if i == 0:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2003")
                    for k in all_data_2003:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 1:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2004")
                    for k in all_data_2004:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 2:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2005")
                    for k in all_data_2005:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 3:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2006")
                    for k in all_data_2006:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 4:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2007")
                    for k in all_data_2007:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 5:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2008")
                    for k in all_data_2008:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 6:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2009")
                    for k in all_data_2009:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            if i == 7:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2010")
                    for k in all_data_2010:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 8:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2011")
                    for k in all_data_2011:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            if i == 9:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2012")
                    for k in all_data_2012:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 10:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2013")
                    for k in all_data_2013:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 11:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2014")
                    for k in all_data_2014:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 12:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2015")
                    for k in all_data_2015:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 13:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2016")
                    for k in all_data_2016:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 14:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2017")
                    for k in all_data_2017:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 15:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2018")
                    for k in all_data_2018:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 16:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2019")
                    for k in all_data_2019:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 17:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2020")
                    for k in all_data_2020:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 18:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2021")
                    for k in all_data_2021:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
            elif i == 19:
                for j in range(len(city_name)):
                    One_Line_data = []
                    One_Line_data.append(city_name[j])
                    One_Line_data.append("2022")
                    for k in all_data_2022:
                        One_Line_data.append(k[j])
                    writer.writerow(One_Line_data)
                csv_file = dir + "/" + DirName
        i += 1
