def check_balance(total_money):
    print(f"Your account has Rs.{total_money}")

def deposit(total_money):
    deposit_money = int(input("Enter the amount to be deposited: "))
    total_money += deposit_money
    print(f"Your account is deposited with Rs.{deposit_money}")
    return total_money

def withdraw(total_money):
    withdraw_money = int(input("Enter the amount to withdraw: "))
    if total_money < withdraw_money:
        print("Insufficient Balance")
    else:
        total_money -= withdraw_money
        print(f"Successfully withdrew Rs.{withdraw_money}")
    return total_money

def main():
    total_money = 0
    while True:
        print("\n***WELCOME***")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        try:
            choice = int(input("Select your activity: "))
            if choice == 1:
                check_balance(total_money)
            elif choice == 2:
                total_money = deposit(total_money)
            elif choice == 3:
                total_money = withdraw(total_money)
            elif choice == 4:
                print("Thanks for using the ATM...")
                break
            else:
                print("Invalid input. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

main()