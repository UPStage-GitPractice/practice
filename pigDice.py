# pig dice program

import random

User_Total = 0
Computer_Total = 0
Total_Turn = 10
Number_Of_Turns = 0
Computer_Turns = 0


def UserTurn():
    roll = random.randint(1,10)
    return roll

def ComputerTurn():
    roll = random.randint(1,10)
    return roll

  
while Number_of_Turns <= Total_turn:
    UserScore = UserTurn()
    if UserScore !=1:
        User_Total = User_Total + UserScore
        Number_Of_Turns = Number_Of_Turns + 1
    elif UserScore == 1:
        while(Coputer_Turns <= Total_Turn):
            CoputerScore = ComputerTurn()
            if ComputerScore != 1:
                Computer_Total = Computer_Total + ComputerScore
                Computer_Turns = Computer_Turns + 1
            else:
                break

