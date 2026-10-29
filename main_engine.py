# imports
import time
import random
import os

# market variables
price = 250
market = .0000000001

Tshares = 50
market_cap = Tshares*price

savecount = 0
regimes = ["random", "bull", "bear", "sideway", "volatility"]

# stauts just means if its on or not.

# calculation matrix
def randomcalc(name, maxchance):
    global price
    global regime
    global regimes
    
    # chance to gain and the chance to not.
    chance = random.randint(0, maxchance)

    # regime chance (sweep, control and etc..)
    regime = random.choices(
        regimes,
        weights=[90, 3, 3, 2, 2],
        k=1
    )[0]
    if chance == 0:
        if regime == "random":
            name = random.gauss(0, .01)
        elif regime == "bull":
            name = random.gauss(2, .01)
        elif regime == "bear":
            name = random.gauss(-2,.01)
        elif regime == "sideway":
            name = random.gauss (0, 0.000000000000001)
        elif regime == "volatility":
            name = random.gauss(0,40)

    else:
        name = 0
    return name

def calc():
    global market
    global price
    global savecount


    # the market walks to the future calculated market
    market = randomcalc(market, 5)
    price = (1+market)*price

    # the amount of ticks for a save
    if savecount >= 60:
        with open("balance.bd", "w") as f:
            f.write(str(price))
        savecount = 0
    else:
        savecount +=1

# engine
while True:
    calc()
    market_cap = Tshares*price
    os.system("cls")
    print("Market of NODE : ", price, "Market Cap", round(int(market_cap)), "P/L", market, regime)
    time.sleep(.01)
    