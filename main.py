import random

rand_0_9 = random.randint(0,9)

rand_0_39 = random.randint(0,39)

player_position_x = random.randint(0,9)
player_position_y = random.randint(0,39)
snaaaaaaaake_x = random.randint(0,9)
snaaaaaaaake_y = random.randint(0,39)
coin_position_x = random.randint(0,9)
coin_position_y = random.randint(0,39)
goal_position_x = -1
goal_position_y = -1
difficulty = 0
movement_correct_regular = False
movement_correct_diagonal = False


# Figuren sollen weit genug auseinander stehen/sich nicht überschneiden
while abs(player_position_x-snaaaaaaaake_x)<4 or abs(player_position_y-snaaaaaaaake_y)<4:
    player_position_x = random.randint(0,9)
    player_position_y = random.randint(0,39)
while coin_position_x == player_position_x or coin_position_x == snaaaaaaaake_x:
    while coin_position_y == player_position_y or coin_position_y == snaaaaaaaake_y:
        coin_position_y = random.randint (0,39)
    coin_position_x = random.randint(0,9)

#Start-Text Anweisung und Schwierigkeitsgrad auswählen 
print ("TO WIN THE GAME COLLECT THE MONEY AND REACH THE GOAL BEFORE THE SNAKE GETS YOU")
print ("CHOOSE A DIFFICULTY")
difficulty = input ("PRESS 1 TO BE ABLE TO MOVE DIAGONALLY, OTHERWISE PRESS ANY OTHER BUTTON")
if difficulty.isdigit():
    difficulty = int(difficulty)
if difficulty == 1:
    print ("USE wa FOR MOVING TOP LEFT, wd FOR TOP RIGHT, sd FOR BOTTOM RIGHT AND as FOR BOTTOM LEFT")

print ("Use w-a-s-d keys to navigate")



#Spiel-Loop
while True:
    movement_correct_regular = False
    movement_correct_diagonal = False
    #wenn Spieler das Geld $ erreicht wird das Ende O erstellt (AB UND ZU WENN MAN DEN BEFEHL GIBT AUF DAS $ FELD ZU GEHEN PASSIERT NICHTS MEHR; UNTERSTE MELDUNG IST: DAS FELD;"Use w-a-s-d keys to navigate";"REACH O" - O wird nicht angezeigt auf dem Feld, kein INput möglich (scheint in einem while loop zu stecken, passiert nur wenn difficulty=1))
    if player_position_x == coin_position_x and player_position_y == coin_position_y:
        print ("REACH O")
        coin_position_x = -1
        goal_position_x = random.randint (0,9)
        goal_position_y = random.randint (0,39)
        while goal_position_x == player_position_x or goal_position_x == snaaaaaaaake_x:
            while goal_position_y == player_position_y or goal_position_x == snaaaaaaaake_y:
                goal_position_y = random.randint (0,39)
                goal_position_x = random.randint (0,9)
    
    #Gewinnbedingung erfüllt (1)
    if player_position_x == goal_position_x and player_position_y == goal_position_y:
        goal_position_x = "out of playing field"

    #Das Spielfeld
    for x in range(10):
        for y in range(40):
            if x==player_position_x and y==player_position_y:
                print ("@", end='')
            elif x==goal_position_x and y==goal_position_y:
                print ("O", end='')
            elif x==snaaaaaaaake_x and y==snaaaaaaaake_y:
                print ("S", end='')
            elif x==coin_position_x and y==coin_position_y:
                print ("$", end='')
            else: 
                print (".", end='')
            if y == 39:
                print ("")
    print ("")


    #Gewinnbedingung(2) und Verlier-Bedingung
    if goal_position_x == "out of playing field":
        break
    if player_position_x == snaaaaaaaake_x and player_position_y == snaaaaaaaake_y:
        break

    #Bewegung der Schlange S
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


    #Spieler Input für einfaches w-a-s-d 
    navigate_player = input ("")
    if navigate_player == "w":
        movement_correct_regular = True
        if player_position_x > 0:
            player_position_x -= 1
    elif navigate_player == "a":
        movement_correct_regular = True
        if player_position_y > 0:
            player_position_y -= 1
    elif navigate_player == "s":
        movement_correct_regular = True
        if player_position_x < 9:
            player_position_x += 1
    elif navigate_player == "d":
        movement_correct_regular = True
        if player_position_y < 39:
            player_position_y += 1

    #Spieler Input für Diagonales bewegen 
    elif difficulty == 1:
        if (navigate_player == "wa" or navigate_player == "aw"):
            movement_correct_diagonal = True
            if player_position_x > 0 and player_position_y > 0:
                player_position_x -= 1
                player_position_y -= 1
            elif player_position_x > 0 and player_position_y == 0:
                player_position_x -= 1
            elif player_position_x == 0 and player_position_y > 0:
                player_position_y -= 1
        if (navigate_player == "wd" or navigate_player == "dw"):
            movement_correct_diagonal = True
            if player_position_x > 0 and player_position_y < 39:
                player_position_x -= 1
                player_position_y += 1
            elif player_position_x > 0 and player_position_y == 39:
                player_position_x -= 1
            elif player_position_x == 0 and player_position_y < 39:
                player_position_y += 1
        if (navigate_player == "sd" or navigate_player == "ds"):
            movement_correct_diagonal = True
            if player_position_x < 9 and player_position_y < 39:
                player_position_x += 1
                player_position_y += 1
            elif player_position_x < 9 and player_position_y == 39:
                player_position_x += 1
            elif player_position_x == 9 and player_position_y < 39:
                player_position_y += 1
        if (navigate_player == "as" or navigate_player == "sa"):
            movement_correct_diagonal = True
            if player_position_x < 9 and player_position_y > 0:
                player_position_x += 1
                player_position_y -= 1
            elif player_position_x < 9 and player_position_y == 0:
                player_position_x += 1
            elif player_position_x == 9 and player_position_y > 0:
                player_position_y -= 1
    
    #Output bei falscher Eingabe 
    if difficulty != 1 and movement_correct_regular == False:
        print ("ONLY w-a-s-d")
    elif movement_correct_diagonal == False:
        print("ONLY w-a-s-d AND DIAGONAL INPUTS")

    #Spiel frühzeitig abbrechen
    if navigate_player == "break":
        break




#Ende, Gewonnen oder Verloren
if goal_position_x == "out of playing field":
    print ("YOU WON!")
else:
    print ("YOU LOST")

