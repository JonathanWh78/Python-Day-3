# Budget App
# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
# These objects should allow for depositing and withdrawing funds from each category, 
# as well computing category balances and transferring balance amounts between categories”

class Budget:
    def food(indep):
        Total = 100
        Total = Total + indep
        return Total
    
    def Fwithdraw(inwith):
        total = 100
        total = total - inwith
        return total



    #def clothing():


    #def entertainment():
print ("-----------------------")
print ("Current Budget is: £100")
money = 100
Menu = 0
while Menu != 4:
    print ("1: Food")
    print ("2: Clothing")
    print ("3: Entertainment")
    print ("4: Quit")
    Menu = int( input ("Which area would you like to go: "))
    if Menu == 1:
        print ("")
        print ("You are in the Food Area")
        print ("")
        print ("1: Deposit")
        print ("2: Withdraw")
        print ("3: Quit")
        FoodMenu = int( input ("Which area would you like to go: "))
        if FoodMenu == 1:
            print ("")
            print ("You are in the Deposit Area, Press 0 to quit")
            print ("")
            Deposit = int(input("How Much Would You Like To Deposit? "))
            if Deposit > 0:
                print ("")
                print ("You Deposited £" + str(Deposit))
                print ("You Have: £" + str(Budget.food(Deposit)))
                print ("")
            if Deposit == 0:
                print ("")
                print ("Returning")
                print ("")


        if FoodMenu == 2:
            print ("")
            print ("You are in the Withdraw Area, Press 0 to quit")
            print ("")
            print ("Your money is: £" + str(money))
            print ("")
            Withdraw = int(input("How Much Would You Like To Withdraw? "))
            if Withdraw > 0:
                print ("")
                print ("You Withdrew: £" + str(Withdraw))
                print ("You Have: £" + str(Budget.Fwithdraw(Withdraw)))
                print ("")
            if Withdraw == 0:
                print ("")
                print ("Returning")
                print ("")


        if FoodMenu == 3:
            print ("")
            print ("Returning")
            print ("")
        else:
            print ("Please Enter a number")


    elif Menu == 2:
        print ("")
        print ("You are in the Clothing Area")
        print ("")
        print ("1: Deposit")
        print ("2: Withdraw")
        print ("3: Quit")
        ClothingMenu = int( input ("Which area would you like to go: "))
        if ClothingMenu == 3:
            print ("")
            print ("Returning")
            print ("")
        else:
            print ("Please Enter a number")


    elif Menu == 3:
        print ("")
        print ("You are in the Entertainment Area")
        print ("")
        print ("1: Deposit")
        print ("2: Withdraw")
        print ("3: Quit")
        ClothingMenu = int( input ("Which area would you like to go: "))
        if ClothingMenu == 3:
            print ("")
            print ("Returning")
            print ("")
        else:
            print ("Please Enter a number")
    else:
        print ("")
        print ("Quitting")
        print ("--------")
