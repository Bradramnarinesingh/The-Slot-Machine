#ICS 201
#ICS 201

#Vasant Gobin & Brad Ramnarinesingh



import random


#this chooses the random items from the list
wheel1 = ["cherry","orange","apple","banana","grapes","bars"]
wheel2 = ["cherry","orange","apple","banana","grapes","bars"]
wheel3 = ["cherry","orange","apple","banana","grapes","bars"]










#the balance or the amount of money the player has
balance= 100






#instructions on how to play the game and the possible earnings
print("Welcome to the Slot Machine Simulator. You'll start with $100. You'll be asked if you want to play. Answer with yes/no. you can also use y/n No case sensitivity in your answer. For example you can answer with YEs, yEs, yes, nO, NO. To win you must get one of the following combinations:")

print("Here are the 3-reel combination payouts:")

print("3 Cherries: $20")

print("3 Oranges: $15")

print("3 Apples: $10")

print("3 Bananas: $5")

print("3 Grapes: $4")

print("3 Bars: $2.50")



#this loops the reels until the player either decides to quit or cannot play anymore due to insufficent balance
while True:

    reel1 = random.choice(wheel1)

    reel2 = random.choice(wheel2)

    reel3 = random.choice(wheel3)
#this input asks the user to play
    enter = input("Would You Like To play?:")


#if they say yes or y, they will be entered into the game and 3 random slots will be chosen
    if enter.casefold()== "yes" or enter.casefold()== "y":
        print(reel1, reel2, reel3)


#if the player gets matching reels, they will win $20 and will also be deducted $2 for the play cost
        if reel1 == "cherry" and reel2 == "cherry" and reel3 == "cherry":

            print("You Won $20!")
            balance= (balance+20)
            balance= (balance-2)
            print("Your Balance is:",balance)





#if the player gets matching reels, they will win $15 and will also be deducted $2 for the play cost
        elif reel1 == "orange" and reel2 == "orange" and reel3 == "orange":

            print("You Won $15!")
            balance= (balance+15)
            balance= (balance-2)
            print("Your Balance is:",balance)




#if the player gets matching reels, they will win $10 and will also be deducted $2 for the play cost
        elif reel1 == "apple" and reel2 == "apple" and reel3 == "apple":

            print("You Won $10!")
            balance= (balance+10)
            balance= (balance-2)
            print("Your Balance is:",balance)


#if the player gets matching reels, they will win $5 and will also be deducted $2 for the play cost
        elif reel1 == "banana" and reel2 == "banana" and reel3 == "banana":

            print("You Won $5!")
            balance= (balance+5)
            balance= (balance-2)
            print("Your Balance is:",balance)



#if the player gets matching reels, they will win $4 and will also be deducted $2 for the play cost
        elif reel1 == "grapes" and reel2 == "grapes" and reel3 == "grapes":

            print("You Won $4!")
            balance= (balance+4)
            balance= (balance-2)
            print("Your Balance is:",balance)


#if the player gets matching reels, they will win $2.50 and will also be deducted $2 for the play cost
        elif reel1 == "bars" and reel2 == "bars" and reel3 == "bars":

            print("You Won $2.50!")
            balance= (balance+2.50)
            balance= (balance-2)
            print("Your Balance is:",balance)


#if the player has an insuffient balance, they will automatically be exited from the game
        elif balance <2:

            print("Sorry you don't have enough credits!")
            break


#if the does not get 3 matching reels, they  they will
        else:

            print("Sorry You Did Not Win!")

            balance= (balance-2)

            print("Your Current Balance Is:","$",balance)
#if they say no or n, they will be exited from the game and will be shown their balance
    if enter.casefold() == "no" or enter.casefold()== "n" :

            print("You ended the game with","$", balance,"in your hand")
            break


