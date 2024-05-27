from city import Get_city
from Regional_Gross_Domestic_Product_地区生产总值 import Get_Regional_Gross_Domestic_Product
from Value_added_of_the_primary_industry_第一产业增加值 import Get_Value_added_of_the_primary_industry
from Value_added_of_the_second_industry_第二产业增加值 import Get_Value_added_of_the_second_industry
from Value_added_of_the_third_industry_第三产业增加值 import Get_Value_added_of_the_third_industry
from Registered_residence_population_at_the_end_of_the_year_年末户籍人口 import Get_Registered_residence_population_at_the_end_of_the_year
from Average_salary_of_non_private_urban_employees_城镇非私营单位在岗职工平均工资 import Get_Average_salary_of_non_private_urban_employees
from Real_estate_development_investment_amount_房地产开发投资额 import Get_Real_estate_development_investment_amount
from Real_estate_development_residential_investment_amount_房地产开发住宅投资额 import Get_Real_estate_development_residential_investment_amount
from Investment_in_real_estate_development_office_buildings_房地产开发办公楼投资额 import Get_Investment_in_real_estate_development_office_buildings
from Investment_amount_in_commercial_properties_for_real_estate_development_房地产开发商业营业用房投资额 import Get_Investment_amount_in_commercial_properties_for_real_estate_development
from Construction_housing_area_of_real_estate_development_enterprises_房地产开发企业施工房屋面积 import Get_Construction_housing_area_of_real_estate_development_enterprises
from Completed_housing_area_of_real_estate_development_enterprises_房地产开发企业竣工房屋面积 import Get_Completed_housing_area_of_real_estate_development_enterprises
from Completed_residential_area_of_real_estate_development_enterprises_房地产开发企业住宅竣工房屋面积 import Get_Completed_residential_area_of_real_estate_development_enterprises
from Sales_area_of_commercial_housing_商品房销售面积 import Get_Sales_area_of_commercial_housing
from Sales_area_of_residential_commercial_housing_住宅商品房销售面积 import Get_Sales_area_of_residential_commercial_housing
from Average_selling_price_of_commercial_housing_商品房平均销售价格 import Get_Average_selling_price_of_commercial_housing
from Average_selling_price_of_residential_commercial_housing_住宅商品房平均销售价格 import Get_Average_selling_price_of_residential_commercial_housing
from Real_estate_development_enterprises_purchase_land_area_房地产开发企业购置土地面积 import Get_Real_estate_development_enterprises_purchase_land_area
from Local_general_public_budget_revenue_地方一般公共预算收入 import Get_Local_general_public_budget_revenue
from Local_general_public_budget_expenditures_地方一般公共预算支出 import Get_Local_general_public_budget_expenditures
from Resident_deposit_balance_住户存款余额 import Get_Resident_deposit_balance
from Passenger_transportation_volume_旅客运输量 import Get_Passenger_transportation_volume
from Freight_transportation_volume_货物运输量 import Get_Freight_transportation_volume
from Post_Office_at_the_end_of_the_year_年末邮政局 import Get_Post_Office_at_the_end_of_the_year
from End_of_year_fixed_telephone_users_年末固定电话用户 import Get_End_of_year_fixed_telephone_users
from Total_retail_sales_of_social_consumer_goods_社会消费品零售总额 import Get_Total_retail_sales_of_social_consumer_goods
from Total_trade_value_of_goods_货物进出口总额 import Get_Total_trade_value_of_goods
from Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges_普通本专科在校学生数 import Get_Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges
from Number_of_hospitals_医院数 import Get_Number_of_hospitals
from Number_of_practicing_physicians_执业医师数 import Get_Number_of_practicing_physicians
from Number_of_theaters_and_cinemas_剧场_影剧院数 import Get_Number_of_theaters_and_cinemas
from Number_of_hightech_enterprises_in_the_development_zone_开发区高新技术企业数 import Get_Number_of_hightech_enterprises_in_the_development_zone
from Employees_of_hightech_enterprises_in_development_zones_开发区高新技术企业从业人员 import Get_Employees_of_hightech_enterprises_in_development_zones
from The_total_output_value_of_hightech_enterprises_in_development_zones_开发区高新技术企业总产值 import Get_The_total_output_value_of_hightech_enterprises_in_development_zones
from Total_revenue_of_hightech_enterprises_in_development_zones_开发区高新技术企业总收入 import Get_Total_revenue_of_hightech_enterprises_in_development_zones
from Total_export_value_of_hightech_enterprises_in_development_zones_开发区高新技术企业出口总额 import Get_Total_export_value_of_hightech_enterprises_in_development_zones
from Road_traffic_equivalent_sound_level_dB_道路交通等效声级dB import Get_Road_traffic_equivalent_sound_level_dB
from Environmental_noise_equivalent_sound_level_dB_环境噪声等效声级dB import Get_Environmental_noise_equivalent_sound_level_dB


# 主要城市名称
def city():
    city = Get_city()
    print(city)


# 国民经济核算
# 1.地区生产总值（当年价格）(亿元)
def data1():
    Regional_Gross_Domestic_Product = Get_Regional_Gross_Domestic_Product()
    return Regional_Gross_Domestic_Product


# 2.第一产业增加值(亿元)
def data2():
    Value_added_of_the_primary_industry = Get_Value_added_of_the_primary_industry()
    return Value_added_of_the_primary_industry


# 3.第二产业增加值(亿元)
def data3():
    Value_added_of_the_second_industry = Get_Value_added_of_the_second_industry()
    return Value_added_of_the_second_industry


# 4.第三产业增加值(亿元)
def data4():
    Value_added_of_the_third_industry = Get_Value_added_of_the_third_industry()
    return Value_added_of_the_third_industry


# 人口和就业
# 1.年末户籍人口(万人)
def data5():
    Registered_residence_population_at_the_end_of_the_year = Get_Registered_residence_population_at_the_end_of_the_year()
    return Registered_residence_population_at_the_end_of_the_year


# 2.城镇非私营单位在岗职工平均工资(元)
def data6():
    Average_salary_of_non_private_urban_employees = Get_Average_salary_of_non_private_urban_employees()
    return Average_salary_of_non_private_urban_employees


# 房地产
# 1.房地产开发投资额(亿元)
def data7():
    Real_estate_development_investment_amount = Get_Real_estate_development_investment_amount()
    return Real_estate_development_investment_amount


# 2.房地产开发住宅投资额(亿元)
def data8():
    Real_estate_development_residential_investment_amount = Get_Real_estate_development_residential_investment_amount()
    return Real_estate_development_residential_investment_amount


# 3.房地产开发办公楼投资额(亿元)
def data9():
    Investment_in_real_estate_development_office_buildings = Get_Investment_in_real_estate_development_office_buildings()
    return Investment_in_real_estate_development_office_buildings


# 4.房地产开发商业营业用房投资额(亿元)
def data10():
    Investment_amount_in_commercial_properties_for_real_estate_development = Get_Investment_amount_in_commercial_properties_for_real_estate_development()
    return Investment_amount_in_commercial_properties_for_real_estate_development


# 5.房地产开发企业施工房屋面积(万平方米)
def data11():
    Construction_housing_area_of_real_estate_development_enterprises = Get_Construction_housing_area_of_real_estate_development_enterprises()
    return Construction_housing_area_of_real_estate_development_enterprises


# 6.房地产开发企业竣工房屋面积(万平方米)
def data12():
    Completed_housing_area_of_real_estate_development_enterprises = Get_Completed_housing_area_of_real_estate_development_enterprises()
    return Completed_housing_area_of_real_estate_development_enterprises


# 7.房地产开发企业住宅竣工房屋面积(万平方米)
def data13():
    Completed_residential_area_of_real_estate_development_enterprises = Get_Completed_residential_area_of_real_estate_development_enterprises()
    return Completed_residential_area_of_real_estate_development_enterprises


# 8.商品房销售面积(万平方米)
def data14():
    Sales_area_of_commercial_housing = Get_Sales_area_of_commercial_housing()
    return Sales_area_of_commercial_housing


# 9.住宅商品房销售面积(万平方米)
def data15():
    Sales_area_of_residential_commercial_housing = Get_Sales_area_of_residential_commercial_housing()
    return Sales_area_of_residential_commercial_housing


# 10.商品房平均销售价格(元/平方米)
def data16():
    Average_selling_price_of_commercial_housing = Get_Average_selling_price_of_commercial_housing()
    return Average_selling_price_of_commercial_housing


# 11.住宅商品房平均销售价格(元/平方米)
def data17():
    Average_selling_price_of_residential_commercial_housing = Get_Average_selling_price_of_residential_commercial_housing()
    return Average_selling_price_of_residential_commercial_housing


# 12.房地产开发企业购置土地面积(万平方米)
def data18():
    Real_estate_development_enterprises_purchase_land_area = Get_Real_estate_development_enterprises_purchase_land_area()
    return Real_estate_development_enterprises_purchase_land_area


# 财政和金融
# 1.地方一般公共预算收入(亿元)
def data19():
    Local_general_public_budget_revenue = Get_Local_general_public_budget_revenue()
    return Local_general_public_budget_revenue


# 2.地方一般公共预算支出(亿元)
def data20():
    Local_general_public_budget_expenditures = Get_Local_general_public_budget_expenditures()
    return Local_general_public_budget_expenditures


# 3.住户存款余额(亿元)
def data21():
    Resident_deposit_balance = Get_Resident_deposit_balance()
    return Resident_deposit_balance


# 运输和邮电
# 1.旅客运输量(万人)
def data22():
    Passenger_transportation_volume = Get_Passenger_transportation_volume()
    return Passenger_transportation_volume


# 2.货物运输量(万吨)
def data23():
    Freight_transportation_volume = Get_Freight_transportation_volume()
    return Freight_transportation_volume


# 3.年末邮政局（所）(处)
def data24():
    Post_Office_at_the_end_of_the_year = Get_Post_Office_at_the_end_of_the_year()
    return Post_Office_at_the_end_of_the_year


# 4.年末固定电话用户(万户)
def data25():
    End_of_year_fixed_telephone_users = Get_End_of_year_fixed_telephone_users()
    return End_of_year_fixed_telephone_users


# 贸易经济
# 1.社会消费品零售总额(亿元)
def data26():
    Total_retail_sales_of_social_consumer_goods = Get_Total_retail_sales_of_social_consumer_goods()
    return Total_retail_sales_of_social_consumer_goods


# 2.货物进出口总额(百万美元)
def data27():
    Total_trade_value_of_goods = Get_Total_trade_value_of_goods()
    return Total_trade_value_of_goods


# 教育、卫生、文化
# 1.普通本专科在校学生数(万人)
def data28():
    Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges = Get_Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges()
    return Number_of_students_enrolled_in_regular_undergraduate_and_vocational_colleges


# 2.医院数(个)
def data29():
    Number_of_hospitals = Get_Number_of_hospitals()
    return Number_of_hospitals


# 3.执业(助理)医师数(万人)
def data30():
    Number_of_practicing_physicians = Get_Number_of_practicing_physicians()
    return Number_of_practicing_physicians


# 4.剧场、影剧院数(个)
def data31():
    Number_of_theaters_and_cinemas = Get_Number_of_theaters_and_cinemas()
    return Number_of_theaters_and_cinemas


# 开发区高新技术企业主要经济指标
# 1.开发区高新技术企业数(个)
def data32():
    Number_of_hightech_enterprises_in_the_development_zone = Get_Number_of_hightech_enterprises_in_the_development_zone()
    return Number_of_hightech_enterprises_in_the_development_zone


# 2.开发区高新技术企业从业人员(人)
def data33():
    Employees_of_hightech_enterprises_in_development_zones = Get_Employees_of_hightech_enterprises_in_development_zones()
    return Employees_of_hightech_enterprises_in_development_zones


# 3.开发区高新技术企业总产值(万元)
def data34():
    The_total_output_value_of_hightech_enterprises_in_development_zones = Get_The_total_output_value_of_hightech_enterprises_in_development_zones()
    return The_total_output_value_of_hightech_enterprises_in_development_zones


# 4.开发区高新技术企业总收入(万元)
def data35():
    Total_revenue_of_hightech_enterprises_in_development_zones = Get_Total_revenue_of_hightech_enterprises_in_development_zones()
    return Total_revenue_of_hightech_enterprises_in_development_zones


# 5.开发区高新技术企业出口总额(万美元)
def data36():
    Total_export_value_of_hightech_enterprises_in_development_zones = Get_Total_export_value_of_hightech_enterprises_in_development_zones()
    return Total_export_value_of_hightech_enterprises_in_development_zones


# 噪声监测
# 1.道路交通等效声级dB(A)
def data37():
    Road_traffic_equivalent_sound_level_dB = Get_Road_traffic_equivalent_sound_level_dB()
    return Road_traffic_equivalent_sound_level_dB


# 2.环境噪声等效声级dB(A)
def data38():
    Environmental_noise_equivalent_sound_level_dB = Get_Environmental_noise_equivalent_sound_level_dB()
    return Environmental_noise_equivalent_sound_level_dB


    








