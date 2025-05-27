print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

price_of_ticket = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        price_of_ticket += 5
    elif age <= 18:
        price_of_ticket += 7
    else:
        price_of_ticket += 12

    is_photo_needed = input("Do you want to click photos? ")
    if is_photo_needed == "yes" or is_photo_needed == "Yes":
        price_of_ticket += 3

    print(f"Please pay {price_of_ticket}")
else:
    print("Sorry you have to grow taller before you can ride.")
