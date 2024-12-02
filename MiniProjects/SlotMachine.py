# Python Slot Machine program

import random

n = 30

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*"*n)
    print(" | ".join(row))
    print("*"*n)


def get_payout(row,bet):

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100

    print("*"*n)
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*"*n)

    while balance > 0:
        print("*"*n)
        print()
        print(f"Current Balance: Rs {balance}/-")

        bet = input("Place your bet amount : ")

        if not bet.isdigit():
            print("Please Enter a Valid Number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        

        if bet <= 0:
            print("Bet must be greater than 0 ")
            continue

        balance -= bet 

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won Rs {payout}/-")
        else:
            print("Sorry you lost the bet")

        balance += payout 

        play_again = input("Do you want to place the bet again? (Y/N) : ").upper()

        if play_again != 'Y':
            break


    print("*"*n)
    print(f"Game Over! Your final balance is Rs {balance}/-")
    print("*"*n)


if __name__ == "__main__":
    main()