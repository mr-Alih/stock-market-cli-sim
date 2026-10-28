import time

while True:

    with open("balance.bd") as f:
        print(f.read())
    time.sleep(2.5)