import random
import time

player1, player2 =0,0
switchThrow=True
snakes={22:2, 33:3, 44:4, 55:5, 66:6, 77:7, 88:8, 99:1}
ladders={11:51, 21:62, 31:73, 41:84, 51:95, 61:96, 71:97, 81:98}

def dice():
    return (random.randint(1,6))

def gameMove(player, currentRoll):
    player += currentRoll if player + currentRoll <= 100 else 0

    if player in snakes:
        print(f'there is a snake at {player}')
        player=snakes[player]
        print("player now at ",player)
        print()

    if player in ladders:
        print(f'there is a ladder at {player}')
        player=ladders[player]
        print("player now at ",player)
        print()
    
    time.sleep(0.4)

    return player


while True:
    currentRoll=dice()

    if switchThrow==True:
        player1=gameMove(player1,currentRoll)
        print("player1's at", player1)
        print()

        if player1==100:
            print("player1's the winner")
            break

    else:
        player2=gameMove(player2,currentRoll)
        print("player2's at", player2)
        print()

        if player2==100:
            print("player2's the winner")
            break
        
    if currentRoll != 6:
        switchThrow = not switchThrow