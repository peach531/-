from random import *
def lotto():
    lot = []

    while len(lot):
        a = randint(1,45)
        if lot.count(a) >= 1:
            i += 1
            continue
        else:
            lot.append(a)
        

    lot.sort()
    print(lot)

lotto()
