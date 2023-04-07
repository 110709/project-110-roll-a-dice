import random

response = input("Do you want to roll the dice?")
roll = random.randint(1,6)

def roll_dice(num_dice):
    
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

if response=='yes':
     print(roll)
else:
    print(input("Are you sure?"))
    if input=='yes':
        print("Ok!Thanks")
    else:
        print(random.randint(1,6))

