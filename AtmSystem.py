
accounts = {
    "1001": ["Ranui", "1234", 5000],
    "1002": ["Minu", "5678", 7000],
    "1003": ["Riya", "1111", 3000]
}

print("===== ATM SYSTEM =====")

acc = input("Enter Account Number: ")
pin = input("Enter PIN: ")

if acc in accounts and accounts[acc][1] == pin:

    print("Welcome", accounts[acc][0])

    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance =", accounts[acc][2])

        elif choice == "2":
            amt = int(input("Enter amount: "))
            accounts[acc][2] += amt
            print("Money Deposited")

        elif choice == "3":
            amt = int(input("Enter amount: "))
            if amt <= accounts[acc][2]:
                accounts[acc][2] -= amt
                print("Please collect cash")
            else:
                print("Insufficient Balance")

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong Account or PIN")