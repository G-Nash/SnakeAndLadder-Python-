import random

def die():
    return (random.randint(1,6))


player1=0
player2=0
switchTurn=True

snakes={22:2, 33:3, 44:4, 55:5, 66:6, 77:7, 88:8}
ladders={11:91, 21:92, 31:93, 41:94, 51:95, 61:96, 71:97, 81:98}


while True:
    currentRoll=die()

    if switchTurn==True:

        player1 += currentRoll if player1 + currentRoll <= 100 else 0

        if player1 in snakes:
            print(f'there is a snake at {player1}')
            player1=snakes[player1]
            print("player1 now at ",player1)
            print()

        if player1 in ladders:
            print(f'there is a ladder at {player1}')
            player1=ladders[player1]
            print("player1 now at ",player1)
            print()

        if currentRoll != 6:
            switchTurn = not switchTurn

        print("player1 is at",player1)
        print()


    else:

        player2 += currentRoll if player2 + currentRoll <= 100 else 0


        if player2 in snakes:
            print(f'there is a snake at {player2}')
            player2=snakes[player2]
            print("player2 now at",player2)
            print()

        if player2 in ladders:
            print(f'there is a ladder at {player2}')
            player2=ladders[player2]
            print("player2 now at ",player2)
            print()

        if currentRoll != 6:
            switchTurn = not switchTurn

        print("player2 is at",player2)
        print()
        
    

    if player1==100:
        print("player1's the winner")
        break

    if player2==100:
        print("player2's the winner")
        break
