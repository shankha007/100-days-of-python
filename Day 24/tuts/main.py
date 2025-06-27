# file = open("my_file.txt")
#
# contents = file.read()
# print(contents)
#
# file.close() # to release the resources

## Another Way
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write operation
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")
#
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNewest text.")
#
# with open("new_file.txt", mode="w") as file:
#     file.write("There is nothing special about me.")

# Absolute Paths
with open("C:/Users/shank/Downloads/new_file.txt") as file:
    contents = file.read()
    print(contents)

# Relative Paths
with open("./new_file.txt") as file:
    contents = file.read()
    print(contents)