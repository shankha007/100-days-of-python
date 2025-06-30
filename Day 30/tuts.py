# FileNotFound Error
# with open("a_file.txt") as file:
#     file.read()

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list = ["Apple", "Mango", "Guava"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["asdfd"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist. Please check.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)