#libraries
import random

#Initiation
def RandomWalker(r):
    x = 0
    y = 0

    while True:
        print("(" + str(x) + ", " + str(y) + ")")

        if abs(x) + abs(y) == r:
            break
        
        else:
            while True:
                move = random.randint(-1,1)
                if move == 0:
                    continue
                else:
                    a = random.randint(0,1)
                    if a == 0:
                        x += move
                    else:
                        y += move
                    break
        
#Debug
RandomWalker(5)
