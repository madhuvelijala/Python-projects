balance = 11000

while True:
    print("\n1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. pin change")
    print("5. exit")
    
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        print(f"balance: {balance}")
    
    elif choice == 2:
        amount = int(input("Enter your deposit amount: "))
        balance += amount
        print("Amount deposited successfully")
        
    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")
            
    elif choice == 4:
        pinchange = int(input("Enter new pin: "))
        print("Pin changed successfully")
        
    elif choice == 5:
        print("Thank you")
        break
        
    else:
        print("Invalid choice")