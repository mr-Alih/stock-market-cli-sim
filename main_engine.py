# imports
import time
import random
import os

# market variables
price = 250
market = .0000000001

Tshares = 50
market_cap = Tshares*price

# stauts just means if its on or not.

# calculation matrix
def randomcalc(name, maxchance):
    global price
    # chance to gain
    chance = random.randint(0, maxchance)
    if chance == 0:
        name = random.gauss(0, .000003)
    else:
        name = 0.00000001
    return name

def calc():
    global market
    global price


    # the market walks to the future calculated market
    market = randomcalc(market, 5)
    price = (1+market)*price

    with open("balance.bd", "w") as f:
        f.write(str(price))

# engine
while True:
    calc()
    market_cap = Tshares*price
    os.system("cls")
    print("Market of NODE : ", price, "Market Cap", round(int(market_cap)), "P/L", market)
    time.sleep(.01)
    