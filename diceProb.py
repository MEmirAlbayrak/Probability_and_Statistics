import random

# This function simulates a single roll of a die.
def rollOneDie():
    m = 0
    for i in range(1, 100001):
        if  random.randint(1,6) == 4:
            m += 1
        
    print("Total four is ", m, " out of", i)
    print("Probability of four is ", m/i)
    print("error", ((m/i)-1/6)/(1/6))
    print("\n")

# roll two dice
def rollTwoDice():
    m = 0
    totalThrowedDice = 0
    for i in range(1, 100001):
        totalThrowedDice += 2
        if  random.randint(1,6) == 4 or random.randint(1,6) == 4: 
            m += 1
    print("All posibilitys ", )
    print("Total four is ", m, " out of", i)
    print("Probability of four is ", m/i)
    print("error", ((m/i)-1/36)/(1/36))
    print("Total throwed dice: ", totalThrowedDice)
    print("\n")
 


#calculate the probability of a die
def calculateProbability(n):
    m = 0
    for i in range(1, 100001):
        if  random.randint(1,6) == n:
            m += 1
    print("Total ", n, " is ", m, " out of", i)
    print("Probability of ", n, " is ", m/i)
    print("error", ((m/i)-1/6)/(1/6))
    print("\n")
    return m/i

# calculate the probability of two dice
def calculateTwoDiceProbability():
    m = 0
    totalThrowedDice = 0
    for i in range(1, 100001):
        totalThrowedDice += 2
        if  random.randint(1,6) == 4 or random.randint(1,6) == 4: 
            m += 1
    print("Total four is ", m, " out of", i)
    print("Probability of four is ", m/i)
    print("error", ((m/i)-1/36)/(1/36))
    print("Total throwed dice: ", totalThrowedDice)
    print("\n")
    return m/i   

# calculate all posibilities of a die
def calculateAllProbability():
    posibilities = 0
    for i in range(1, 7):
        posibilities += calculateProbability(i)
    print("All posibilities: ", posibilities)
