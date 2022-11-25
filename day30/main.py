# Day 30 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Errors, Exceptions and JSON Data: Improving the Password

#  FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existenct_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("day30/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfdfdf"])
except FileNotFoundError:
    file = open("day30/a_file.txt", "w")
    file.write("Something cool.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")