#verwendete imports
import random

#verwendete Variablen
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
difficulty = 0

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
if difficulty == 1:
    print ("USE wa FOR MOVING TOP LEFT, wd FOR TOP RIGHT, sd FOR BOTTOM RIGHT AND as FOR BOTTOM LEFT")

#Spiel-Loop
while True:
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
        goal_position_x = -2

    #Das Spielfeld
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

    #Gewinnbedingung(2) und Verlier-Bedingung
    if goal_position_x == -2:
        break
    if player_position_x == snaaaaaaaake_x and player_position_y == snaaaaaaaake_y:
        break

    #Spieler Input für einfaches w-a-s-d (SPIELER KANN DERZEIT NICHT AUF DAS FELD GANZ RECHTS?)
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

    #Spieler Input für Diagonales bewegen (WIRD DERZEIT ÜBERSPRUNGEN?)
    elif difficulty == 1:
        if (navigate_player == "wa" or navigate_player == "aw"):
            if player_position_x > 0 and player_position_y > 0:
                player_position_x -= 1
                player_position_y -= 1
            elif player_position_x > 0 and player_position_y == 0:
                player_position_x -= 1
            elif player_position_x == 0 and player_position_y > 0:
                player_position_y -= 1
        if (navigate_player == "wd" or navigate_player == "dw"):
            if player_position_x > 0 and player_position_y < 40:
                player_position_x -= 1
                player_position_y += 1
            elif player_position_x > 0 and player_position_y == 39:
                player_position_x -= 1
            elif player_position_x == 0 and player_position_y > 40:
                player_position_y += 1
        if (navigate_player == "sd" or navigate_player == "ds"):
            if player_position_x > 10 and player_position_y > 40:
                player_position_x += 1
                player_position_y += 1
            elif player_position_x > 0 and player_position_y == 39:
                player_position_x += 1
            elif player_position_x == 0 and player_position_y > 40:
                player_position_y += 1
        if (navigate_player == "as" or navigate_player == "sa"):
            if player_position_x > 10 and player_position_y > 0:
                player_position_x += 1
                player_position_y -= 1
            elif player_position_x > 10 and player_position_y == 0:
                player_position_x += 1
            elif player_position_x == 0 and player_position_y > 0:
                player_position_y -= 1
    
    #Output bei falscher Eingabe (Schlange S bewegt sich trozdem derzeit)
    else: 
        if difficulty == 1:
            print("ONLY w-a-s-d AND DIAGONAL INPUTS")
        else:
            print ("ONLY w-a-s-d")

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
   
#Ende, Gewonnen oder Verloren
if goal_position_x == -2:
    print ("YOU WON!")
else:
    print ("YOU LOST")
