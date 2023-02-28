import random
n = random.randint(1,9)
print(n)
n= n+5
print(n)
coins = 3*n+1
turn = True 
print(coins)
while(coins > 0):
    pick = int(input("Enter 1 or 2 "))
    coins = coins - pick
    if(coins == 0):
        break 
    turn = False 
    if pick == 1:
        coins = coins - 2
    else:
        coins = coins - 1
    if(coins == 0):
        break
    turn = True
if turn:
    print("Customer loss")
else:
    print("Computer loss")

