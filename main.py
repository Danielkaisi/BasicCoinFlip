import random

#After importing random, creating a stored value that either outputs 1 or 2
CoinFlipRNG = random.randrange(1,3,1)
UserCoinChoice = input("Please choose Heads or Tails " )

#This is just something to test out wether your choice is valid or not, mostly for testing

#if UserCoinChoice in ["Heads", "heads"] or UserCoinChoice in ["Tails", "tails"]:
#    print("Thanks for choosing")
#else:
#    print("Wrong input")

#Setting up the outputs for the coinflip result
if CoinFlipRNG == 1:
    CoinFlipResult = "Heads"

if CoinFlipRNG == 2:
    CoinFlipResult = "Tails"

#Outputs based on user input and coinflip RNG
if CoinFlipResult == "Heads" and UserCoinChoice in ["Heads", "heads"]:
    print("It was Heads, you go first!")
elif CoinFlipResult == "Tails" and UserCoinChoice in ["Tails", "tails"]:
    print("It was Tails, you go first!")
elif CoinFlipResult == "Heads" and UserCoinChoice in ["Tails", "tails"]:
    print("It was Heads, you go last!")
elif CoinFlipResult == "Tails" and UserCoinChoice in ["Heads", "heads"]:
    print("It was Tails, you go last!")

    
