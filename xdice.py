#Yash python class - mar27 2021
import random

print ("How many sides do you want? ")

sides=input("How many sides to the die do you want? ")

sidesint=int(sides)

randomnum=random.randrange(1,sides)


print ("the number you got is ..." + randomnum)