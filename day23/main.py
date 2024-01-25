import pandas

# import csv
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             new_temperature = int(row[1])
#             temperatures.append(new_temperature)
#         print(row)
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temperature = data["temp"]
# temperature_list = temperature.to_list()
# avg_temperature = sum(temperature_list) / len(temperature_list)
# print(temperature_list, avg_temperature)
# average = temperature.mean()
# max_temp = temperature.max()
# print(average, max_temp, temperature.tolist())
# print(data[data["temp"] == data.temp.max()])
# print(data[data.day == "Monday"])
# print(data[data.condition == "Sunny"])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Construct a Dataframe
# data_dict = {
#     "name": ["Manoj", "Monu", "Monika"],
#     "age": [21, 20, 20]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
data = pandas.read_csv("squirrel.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count],
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")
