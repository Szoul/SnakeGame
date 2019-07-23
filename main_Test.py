import random


x= 0
y= 0
player_position_x = random.randint(0,9)
player_position_y = random.randint(0,39)
snaaaaaaaake_x = random.randint(0,9)
snaaaaaaaake_y = random.randint(0,39)
coin_position_x = random.randint(0,9)
coin_position_y = random.randint(0,39)


while True:
    navigate_player = input ("Use wasd keys to navigate")
    if navigate_player == "w":
      print ("1")
    elif navigate_player == "a":
       print ("2")
    elif navigate_player == "s":
      print ("3")
    elif navigate_player == "d":
     print ("4")
    else: 
        print("only wasd")





while abs(player_position_x-snaaaaaaaake_x)<4 or abs(player_position_y-snaaaaaaaake_y)<4:
    player_position_x = random.randint(0,9)
    player_position_y = random.randint(0,39)

while x< 10:
    while y< 40:
        if x==player_position_x and y==player_position_y:
            print ("@", end='')
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
