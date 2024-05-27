# # 方法一
# lables = ['排名', '学校名称', '学校地点', '办学总分', '办学层级']
# a = [1, 2, 3, 4, 5]
# b = ['qinghua', 'beida', 'zhangsan', 'lisi', 'wangwu']
# c = ['北京', '北京', '上海', '深圳', '杭州']
# d = ['100', '1000', '2000', '500', '400']
# e = ['1', '5', '3', '2', '4']
# aa = dict(zip(lables, [a, b, c, d, e]))
# print(aa)
#
# # 方法二
# k = {}
# for i in range(len(lables)):
#     k[lables[i]] = [a, b, c, d, e][i]
#
# print(k)

# from nete import *
# function_mapping = {
#         1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7,
#         8: data8,9: data9,10: data10,11: data11,12: data12,13: data13,14: data14,
#         15: data15, 16: data16, 17: data17, 18: data18, 19: data19, 20: data20, 21: data21,
#         22: data22, 23: data23, 24: data24, 25: data25, 26: data26, 27: data27, 28: data28,
#         29: data29, 30: data30, 31: data31, 32: data32, 33: data33, 34: data34, 35: data35,
#         36: data36, 37: data37, 38: data38
#     }
# Num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
# for i in Num_list:
#     if i in function_mapping:
#         func = function_mapping[i]
#         result = func()
#         print(result)

# import nete
# function_names = [name for name in dir(nete) if callable(getattr(nete, name))]
# print(function_names)
#
# for i in Num_list:
#     if i == 1:
#         data = data1()
#     elif i == 2:
#         data = data2()
#     elif i == 3:
#         data = data3()
#     elif i == 4:
#         data = data4()
#     elif i == 5:
#         data = data5()
#     elif i == 6:
#         data = data6()
#     elif i == 7:
#         data = data7()
#     elif i == 8:
#         data = data8()
#     elif i == 9:
#         data = data9()
#     elif i == 10:
#         data = data10()
#     elif i == 11:
#         data = data11()
#     elif i == 12:
#         data = data12()
#     elif i == 13:
#         data = data13()
#     elif i == 14:
#         data = data14()
#     elif i == 15:
#         data = data15()
#     elif i == 16:
#         data = data16()
#     elif i == 17:
#         data = data17()
#     elif i == 18:
#         data = data18()
#     elif i == 19:
#         data = data19()
#     elif i == 20:
#         data = data13()
#     elif i == 21:
#         data = data21()
#     elif i == 22:
#         data = data22()
#     elif i == 23:
#         data = data23()
#     elif i == 24:
#         data = data24()
#     elif i == 25:
#         data = data25()
#     elif i == 26:
#         data = data26()
#     elif i == 27:
#         data = data27()
#     elif i == 28:
#         data = data28()
#     elif i == 29:
#         data = data29()
#     elif i == 30:
#         data = data30()
#     elif i == 31:
#         data = data31()
#     elif i == 32:
#         data = data32()
#     elif i == 33:
#         data = data33()
#     elif i == 34:
#         data = data34()
#     elif i == 35:
#         data = data35()
#     elif i == 36:
#         data = data36()
#     elif i == 37:
#         data = data37()
#     elif i == 38:
#         data = data38()


# import time
#
# start_time = time.time()
#
# for i in range(50000):
#     print("Hello, World!")
#
# end_time = time.time()
#
# print(f"Execution time: {end_time - start_time} seconds")
