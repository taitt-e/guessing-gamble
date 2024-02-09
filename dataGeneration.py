# This python program will generate 100 random numbers within different ranges
# The ranges will be 1 - 10 1 - 100 1-1000 1- 10,000 1-100,000 1 - 1,000,000
# It will also take the jackpot amount

import random

upperBound = 10
lowerBound = 1
jackpotAmount = 3
f = open("input.txt", "w")

for i in range(0,7,1):
    for j in range (1,100,1):
        x = random.randint(lowerBound,upperBound)
        f.write(str(lowerBound) + " " + str(upperBound))
        f.write("\t" + str(x) + " " + str(jackpotAmount))
        f.write("\n")
    upperBound *= 10
    jackpotAmount *= 3
f.close()