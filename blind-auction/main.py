from art import logo
import sys

print(logo)
print("Welcome to the secret auction program.")
logs = []


def start_bid():
    name = input("What is your name? ")
    bid_amount = int(input("What's your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bid_log = {}
    bid_log["name"] = name
    bid_log["amount"] = bid_amount
    logs.append(bid_log)
    if other_bidders == "yes":
        # clear console
        sys.stdout.write("\033[H\033[J")
        start_bid()
    elif other_bidders == "no":
        show_winner()
    else:
        print("Invalid option")


def show_winner():
    max_bid = logs[0]["amount"]
    name = ""
    for log in logs:
        if max_bid < log["amount"]:
            max_bid = log["amount"]
            name = log["name"]
    print(f"The winner is {name} with a bid of ${max_bid}")


start_bid()
