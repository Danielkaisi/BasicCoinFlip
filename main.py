import random

CoinFlipRNG = random.randrange(1,3,1)
UserCoinChoice = input("Please choose Heads or Tails " )

#if UserCoinChoice in ["Heads", "heads"] or UserCoinChoice in ["Tails", "tails"]:
#    print("Thanks for choosing")
#else:
#    print("Wrong input")

if CoinFlipRNG == 1:
    CoinFlipResult = "Heads"

if CoinFlipRNG == 2:
    CoinFlipResult = "Tails"

if CoinFlipResult == "Heads" and UserCoinChoice in ["Heads", "heads"]:
    print("It was Heads, you go first!")
elif CoinFlipResult == "Tails" and UserCoinChoice in ["Tails", "tails"]:
    print("It was Tails, you go first!")
elif CoinFlipResult == "Heads" and UserCoinChoice in ["Tails", "tails"]:
    print("It was Heads, you go last!")
elif CoinFlipResult == "Tails" and UserCoinChoice in ["Heads", "heads"]:
    print("It was Tails, you go last!")
