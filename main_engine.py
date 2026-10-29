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
s_weight = [90, 3, 3, 2, 2] #standard weights
l_weight = [90, 3, 3, 2, 2]
counters = [1, 1 , 1, 1, 1]
regime = "random"

# stauts just means if its on or not
def calculate_percentage(count, start=90, target=30, max_count=16):
    count = max(0, min(count, max_count))
    if  counters[regimes.index(regime)] >=15:
            counters[regimes.index(regime)] = 1
    return start + (target - start) * (count / max_count)
    
def changeregime(option):
    global l_weight, counters, s_weight, regimes, regime
    # option changes flikking
    match option:
        case 0:
            l_weight = [90, 3, 3, 2, 2]
        case 1:
            l_weight = [50, 5, 5, 5, 5]
        case 2:
            # abnormal. should percentually change from current regime to random (main) 
            l_weight[regimes.index(regime)] = calculate_percentage(counters[regimes.index(regime)], l_weight[regimes.index(regime)], s_weight[regimes.index(regime)], counters[regimes.index(regime)])
            counters[regimes.index(regime)] = s_weight[regimes.index(regime)] + 1
            l_weight = [90, 3, 3, 2, 2]
            
    # regime chance (sweep, control and etc..)
    regime = random.choices(
        regimes,
        weights=l_weight,
        k=1
    )[0]

def callregime(name):
    global l_weight, counters, s_weight, regimes, regime

    # change the regime randomly
    choice = random.randint(0,1)
    if regime != "random":
        # flik normal regime change (chance)
        changeregime(2)
    elif choice == 0:
        # flik abnormal regime change (random)
        changeregime(0)
    elif choice == 1:
        # flik abnormal regime change (flatten)
        changeregime(1)

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
    return name

# calculation matrix
def randomcalc(name, maxchance):
    global price
    # chance to gain and the chance to not.
    chance = random.randint(0, maxchance)

    if chance == 0:
        name = callregime(name)
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
    print("Market of NODE : ", price, "Market Cap", round(int(market_cap)), "P/L", market, regime, counters[regimes.index(regime)])
    time.sleep(.01)
    