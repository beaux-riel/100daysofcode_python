# with open ('day25/weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open ('day25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('day25/weather_data.csv')
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(f"Average temp: {average:.0f}")

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("day25/new_data.csv")