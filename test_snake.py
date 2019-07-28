import random

def rand_0_9(): 
    return random.randint(0,9)
def rand_0_39(): 
    return random.randint(0,39)

player_position_x = random.randint(0,9)
player_position_y = random.randint(0,39)
snaaaaaaaake_x = [rand_0_9()]
snaaaaaaaake_y = [rand_0_39()]
snaaaaaaaake_position_x = []
snaaaaaaaake_position_y = []

for snake_length in range (5):
    snaaaaaaaake_position_x.append(snaaaaaaaake_x)
    snaaaaaaaake_position_y.append(snaaaaaaaake_y)
    randomsnake = random.randint(0,3)
    if randomsnake == 0:
        snaaaaaaaake_x -= 1
    elif randomsnake == 1:
        snaaaaaaaake_x -= 1
    elif randomsnake == 2:
        snaaaaaaaake_y += 1 
    elif randomsnake == 3:
        snaaaaaaaake_y -= 1



coin_position_x = random.randint(0,9)
coin_position_y = random.randint(0,39)
goal_position_x = -1
goal_position_y = -1




for x in range(10):
    for y in range(40):
        if x==player_position_x and y==player_position_y:
            print ("@", end='')
        elif x==goal_position_x and y==goal_position_y:
            print ("O", end='')
        elif x==coin_position_x and y==coin_position_y:
            print ("$", end='')
        elif x in snaaaaaaaake_position_x and y in snaaaaaaaake_position_y:
            print ("S", end '')
        else: 
            print (".", end='')
        if y == 39:
            print ("")
print ("")