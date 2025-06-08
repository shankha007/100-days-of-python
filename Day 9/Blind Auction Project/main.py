from art import logo
print(logo)

print("Welcome to the secret auction program.")

bidders = {}

should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid

    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if any_other_bidders == 'no':
        should_continue = False
    else:
        print("\n" * 20)

highest_bid = 0
highest_bidder = ""

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = bidders[bidder]

print("\n" * 20)
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")