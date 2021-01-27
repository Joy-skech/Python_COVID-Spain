# The Course - PROG8420 (PROGRAMMING FOR BIG DATA)
# The assignment number - Assignment 02_Q1
# Creation date : 12th February 2020
# Author's Name: Joy Obisesan




import random

def roll(diceCount):
    return random.randint(1, diceCount*6) 


dice = {}

#get the input for number of dice from the user,validating the input.
diceCount= int(input("how many dice?"))
if diceCount < 1 and diceCount>8:
   print('Negative values not allowed!')
   diceCount= int(input("how many dice?"))


numberOfFaces = 6*diceCount

# Initalize the dictionary
for i in range(1,numberOfFaces+1):
    dice[i] = 0

# get the input from the user for number of rolls and validate the input
rollCount = int(input("How many rolls? "))
if rollCount< 1 :      
   print('Negative values not allowed!')
   rollCount = int(input("How many rolls? "))
   
   
# Simulate the rolls  
for i in range(1,rollCount+1):
    diceFaceValue = roll(diceCount)
    dice[diceFaceValue] = dice[diceFaceValue] + 1
   
   
# Calculate the probability for all values for 1-8 dice

Combinations = [6, 36, 216, 1296, 7776, 46656, 279936, 1679616]
NumberOfWays = []
NumberOfWays.append([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,1,2,3,4,5,6,5,4,3,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,0,1,3,6,10,15,21,25,27,27,25,21,15,10,6,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,0,0,1,4,10,20,35,56,80,104,125,140,146,140,125,104,80,56,35,20,10,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,0,0,0,1,5,15,35,70,126,205,305,420,540,651,735,780,780,735,651,540,420,305,205,126,70,35,15,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,0,0,0,0,1,6,21,56,126,252,456,756,1161,1666,2247,2856,3431,3906,4221,4332,4221,3906,3431,2856,2247,1666,1161,756,456,252,126,56,21,6,1,0,0,0,0,0,0,0,0,0,0,0,0])
NumberOfWays.append([0,0,0,0,0,0,1,7,28,84,210,462,917,1667,2807,4417,6538,9142,12117,15267,18327,20993,22967,24017,24017,22967,20993,18327,15267,12117,9142,6538,4417,2807,1667,917,462,210,84,28,7,1,0,0,0,0,0,0])
NumberOfWays.append([0,0,0,0,0,0,0,1,8,36,120,330,792,1708,3368,6147,10480,16808,25488,36688,50288,65808,82384,98813,113688,125588,133288,135954,133288,125588,113688,98813,82384,65808,50288,36688,25488,16808,10480,6147,3368,1708,792,330,120,36,8,1])


   
# simulating diceprobablility
DicePb = []
for i in range(0,8):
    temp = []
    for j in range(0,48):
        temp.append(NumberOfWays[i][j] / Combinations[i])
    DicePb.append(temp)

# To use the function, NumberOfDice are the number of dice in the sample,
# and TotalOnFaces is the sum of the values on the faces on a given roll
#
# Valid Number of dice is 1 to 8 inclusive;
# valid TotalOnFaces is 1 to 48 inclusive
#
# If any parameter is invalid, the returned value is 0
#
def GetDiceProbability(NumberOfDice, TotalOnFaces):
    result = 0
    if ((type(NumberOfDice) == int) and (type(TotalOnFaces) == int)):
        if ((NumberOfDice >= 1 and NumberOfDice <=8) and (TotalOnFaces >= 1 and TotalOnFaces <= 48)):
            result = DicePb[NumberOfDice-1][TotalOnFaces-1]
    return result

#simulating the dicecount to get the theoretical likelihood and the percentage error
for i in dice:
    if i < diceCount:
        continue
    likelihood  = GetDiceProbability(diceCount ,i )
    actual = dice[i] / rollCount
    error = abs(((actual - likelihood) / likelihood))
#the print function gives us the dice total,actual, theoretical likelihood and the percentage error.
    print(i,dice[i],actual,likelihood,error)
