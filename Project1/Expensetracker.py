# Expense Tracker 
ExpensesList = []
print("Welcome to Expense Tracker")
while True :
    print("====Menu====")
    print("1. for Add Expense")
    print("2. for View all expense")
    print("3. for View Total Kharcha")
    print("4. for Exit ")

    choice = input("Please Enter your choice :---     ")

    if(choice == "1"):
        date = input("kis date pr kharch kia :- ")
        category = input("kis type ka Kharcha kia (food, travel , Makeup , Books) :- ")
        description = input("batao q khareeda :- ")
        amount = float(input("kitna kharch kia :- "))

        Expense = {
            "date" : date,
            "category": category,
            "description" : description,
            "amount" : amount
        }
        ExpensesList.append(Expense)
        print("\n Done! Expense is added Sucessfully!")

# View All Expenses
    elif(choice == "2"):
        if ((len(ExpensesList)) == 0):
            print("No Expense is added. Jao phle Expense add kro")
        else:
            count = 1
            print("===yeh hai apke Expense===")
            for kharcha in ExpensesList:
                print(f"kharcha number {count} -> {kharcha["date"] , {kharcha["category"]} , {kharcha["description"]}, {kharcha["amount"]}}")
                count = count + 1
# View total kharcha
    elif (choice == "3"):
        if (len(ExpensesList)==0):
            print("Abhi apka koi kharcha nhi hua hai")
        else:
            total = 0
            for kharcha in ExpensesList:
                total = total + kharcha["amount"]
        
            print(f"ye hai apka Total khracha : {total}")

# Exit

    elif(choice == "4"):
        print("Dhanyawaad")
        break

    else:
        print("Invalid choice !! , Try Again")




    
