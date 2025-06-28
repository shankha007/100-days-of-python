# numbers = [1, 2, 3, 4]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
#
# name = "Shankha"
# new_name = [letter for letter in name]
# print(new_name)

# doubled_numbers = [num * 2 for num in range(1, 5)]
# print(doubled_numbers)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)