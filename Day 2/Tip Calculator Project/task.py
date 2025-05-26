print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

per_head_bill = bill / people
total_payable = per_head_bill * (1 + tip / 100)
rounded_value = round(total_payable , 2)

print(f"${rounded_value}")