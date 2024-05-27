import csv

city = ['北京', '天津', '石家庄', '太原',
                 '呼和浩特', '沈阳', '大连', '长春'
                 , '哈尔滨', '上海', '南京', '杭州'
                 , '宁波', '合肥', '福州', '厦门'
                 , '南昌', '济南', '青岛', '郑州'
                 , '武汉', '长沙', '广州', '深圳'
                 , '南宁', '海口', '重庆', '成都'
                 , '贵阳', '昆明', '拉萨', '西安'
                 , '兰州', '西宁', '银川', '乌鲁木齐']
city_id = [i for i in range(len(city))]

csv_file = "city.csv"

with open(csv_file,'w',newline="",encoding='utf-8') as f:
    writer = csv.writer(f)
    # writer.writerow(["Id","City"])
    for i,j in zip(city_id,city):
        row = [i,j]
        writer.writerow(row)