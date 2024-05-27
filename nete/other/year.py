import csv

year = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
year_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

csv_file = "year.csv"

with open(csv_file,'w',newline="",encoding='utf-8') as f:
    writer = csv.writer(f)
    # writer.writerow(["Id","Year"])
    for i,j in zip(year_id,year):
        row = [i,j]
        writer.writerow(row)