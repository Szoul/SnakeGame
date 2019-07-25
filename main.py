import random


x= 0
y= 0
player_position_x = random.randint(0,9)
player_position_y = random.randint(0,39)
snaaaaaaaake_x = random.randint(0,9)
snaaaaaaaake_y = random.randint(0,39)
coin_position_x = random.randint(0,9)
coin_position_y = random.randint(0,39)
goal_position_x = -1
goal_position_y = -1


while abs(player_position_x-snaaaaaaaake_x)<4 or abs(player_position_y-snaaaaaaaake_y)<4:
    player_position_x = random.randint(0,9)
    player_position_y = random.randint(0,39)

while coin_position_x == player_position_x or coin_position_x == snaaaaaaaake_x:
    while coin_position_y == player_position_y or coin_position_y == snaaaaaaaake_y:
        coin_position_y = random.randint (0,39)
    coin_position_x = random.randint(0,9)

print ("TO WIN THE GAME COLLECT THE MONEY AND REACH THE GOAL BEFORE THE SNAKE GETS YOU")

while True:
    if player_position_x == coin_position_x and player_position_y == coin_position_y:
        print ("REACH O")
        coin_position_x = -1
        goal_position_x = random.randint (0,9)
        goal_position_y = random.randint (0,39)
        while goal_position_x == player_position_x or goal_position_x == snaaaaaaaake_x:
            while goal_position_y == player_position_y or goal_position_x == snaaaaaaaake_y:
                goal_position_y = random.randint (0,39)
                goal_position_x = random.randint (0,9)
    
    if player_position_x == goal_position_x and player_position_y == goal_position_y:
        goal_position_x = -2

    while x< 10:
        while y< 40:
            if x==player_position_x and y==player_position_y:
                print ("@", end='')
                y += 1  
            elif x==goal_position_x and y==goal_position_y:
                print ("O", end='')
                y += 1
            elif x==snaaaaaaaake_x and y==snaaaaaaaake_y:
                print ("S", end='')
                y += 1
            elif x==coin_position_x and y==coin_position_y:
                print ("$", end='')
                y += 1
            else: 
                print (".", end='')
                y += 1
        print (".")
        x += 1
        y= 0
    x = 0
    y = 0

    if goal_position_x == -2:
        break
    if player_position_x == snaaaaaaaake_x and player_position_y == snaaaaaaaake_y:
        break

    navigate_player = input ("Use w-a-s-d keys to navigate")
    if navigate_player == "w":
        if player_position_x > 0:
            player_position_x -= 1
    elif navigate_player == "a":
        if player_position_y > 0:
            player_position_y -= 1
    elif navigate_player == "s":
        if player_position_x < 9:
            player_position_x += 1
    elif navigate_player == "d":
        if player_position_y < 40:
            player_position_y += 1
    else: 
        print("only w-a-s-d")

    if player_position_x != snaaaaaaaake_x or player_position_y != snaaaaaaaake_y:
        if (player_position_y - snaaaaaaaake_y) != 0:
            if (player_position_y - snaaaaaaaake_y) < 0:
                snaaaaaaaake_y -= 1
            elif (player_position_y - snaaaaaaaake_y) > 0:
                snaaaaaaaake_y += 1 
        elif (player_position_x - snaaaaaaaake_x) != 0:
            if (player_position_x - snaaaaaaaake_x) < 0:
                snaaaaaaaake_x -= 1
            elif (player_position_x - snaaaaaaaake_x) > 0:
                snaaaaaaaake_x += 1 
   

if goal_position_x == -2:
    print ("YOU WON!")
else:
    print ("YOU LOST")
