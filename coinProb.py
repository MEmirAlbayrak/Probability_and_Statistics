import random

# throw a coin
def throwACoin():
    m = 0
    for i in range(1, 100001):
        if random.randint(1,2) == 1:
            m += 1
    print("Total heads is ", m, " out of", i)
    print("Probability of heads is ", m/i)
    print("error", ((m/i)-1/2)/(1/2))
    print("\n")