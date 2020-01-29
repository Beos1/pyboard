import random
playerCount = 0
while(0>=playerCount or playerCount>6):
    playerCount = int(input("How many Players(1-6): "))
print(playerCount)
print(random.randint(1,6))