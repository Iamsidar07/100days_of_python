# try:
#     # Try to do these thing error may occur
#     file = open("a_file.txt")
#     example_dict = {"key": "value"}
#     print(example_dict["key"])
# except FileNotFoundError:
#     # do this when this error occur
#     # execute this when FileNotFoundError occur
#     # can have multiple except
#     file = open("a_file.txt", "w")
#     file.write("I have something to write.")
# except KeyError as error_msg:
#     # do this when keyError error occur
#     print(f"Key {error_msg} does not exist.")
# else:
#     # do this only if try part succeeded
#     content = file.read()
#     print(content)
# finally:
#     # do this no matter what went wrong

#     file.close()
#     # raise KeyError("I have raised this error")
#     # if you want to raise an error use "raise" keyword

# height = float(input("Height: "))
# weight = float(input("Weight: "))

# # Height should not be greater than 3 meter
# if height > 3:
#     raise ValueError("Human height should not be greater than 3 meter.")

# bmi = weight/height ** 2
# print(bmi)


# Input
# ["Apple", "Pear", "Orange"]
# fruits = eval(input())
# # 🚨 Do not change the code above

# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# # 🚨 Do not change the code below
# make_pie(4)

# eval() function will create a list of dictionaries using the input
# [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass


print(total_likes)
