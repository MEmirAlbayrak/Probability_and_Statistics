import random

# Throw a coin
def throwACoin():
    m = 0
    for i in range(1, 10001):
        if random.randint(1,2) == 1:
            m += 1
    print("Total heads is ", m, " out of", i)
    print("Probability of heads is ", m/i)
    print("error", ((m/i)-1/2)/(1/2))
    print("\n")

# Throw a coin two times
def throwACoin2():
    m = 0
    for i in range(1, 10001):
        if random.randint(1,2) == 1:
            m += 1
        if random.randint(1,2) == 1:
            m += 1
    print("Total heads is ", m, " out of", i)
    print("Probability of heads is ", m/i)
    print("error", ((m/i)-1/2)/(1/2))
    print("\n")