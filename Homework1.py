import Formulas

#Consider that you have bought 8 batteries and charged only 6 of
#them, but you have forgotten which are charged! If you now randomly
#select 4 batteries to use in a torch, what is the probability that you
#have selected:
#a) No uncharged batteries?
#b) One uncharged battery?
#c) Both uncharged batteries?
#d) An uncharged battery (one or both)?

def Q1_A():
    
    print("1 a) No uncharged batteries?")
    print("All Probabilities: ", Formulas.combination(8,4))
    print("All charged probilities: ", Formulas.combination(6,4))
    print("Probability of no uncharged batteries: ", Formulas.combination(8,6) - Formulas.combination(6,4))
    print("\n")


def Q1_B():
    
    print("1 b) One uncharged battery?")
    print("All Probabilities: ", Formulas.combination(8,4))
    print("Three charged probilities: ", Formulas.combination(6,3) * Formulas.combination(2,1))
    print("\n")

def Q1_C():

    print("1 c) Both uncharged batteries?")
    print("All Probabilities: ", Formulas.combination(8,4))
    print("Two charged probilities: ", Formulas.combination(6,2) * Formulas.combination(2,2))
    print("\n")

def Q1_D():

    print("1 d) An uncharged battery (one or both)?")
    print("All Probabilities: ", Formulas.combination(8,4))
    print("An uncharged battery (one or both) probilities: ", Formulas.combination(8,4) - Formulas.combination(6,4))
    print("\n")
    

def Question1():
    Q1_A()
    Q1_B()
    Q1_C()
    Q1_D()


#Question 2
#A security system uses a 3-by-3 keypad to set a code with 4 key presses.
#How many different codes are possible if:
#a) the order of key presses counts, but key presses cannot be repeated;
#b) the order of key presses does not count, and key presses cannot be repeated;
#c) the order of key presses counts, and key presses can be repeated.

# 1 2 3
# 4 5 6
# 7 8 9

# _ _ _ _

def Q2_A():
    print("2 a) The order of key presses counts, but key presses cannot be repeated")
    print("All Probabilities: ", Formulas.permutation(9,4))
    print("\n")

def Q2_B():
    print("2 b) The order of key presses does not count, and key presses cannot be repeated")
    print("All Probabilities: ", Formulas.combination(9,4))
    print("\n")

def Q2_C():
    print("2 c) The order of key presses counts, and key presses can be repeated")
    print("All Probabilities: ", Formulas.permutationWithRepetition(9,4))
    print("\n")

def Question2():
    Q2_A()
    Q2_B()
    Q2_C()



Question1()
Question2()