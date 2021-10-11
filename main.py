import random
import Formulas

n = int(input("Enter the number of obj: "))
r = int(input("How many obg selected: "))


#coinProb.throwACoin()

#diceProb.rollOneDie()
#diceProb.rollTwoDice()
#diceProb.calculateProbability(4)
#diceProb.calculateAllProbability()
#diceProb.calculateTwoDiceProbability()


# Formulas
print("Combination: ",  Formulas.combination(n, r))
print("combinationWithRepetition: ", Formulas.combinationWithRepetition(n, r))
print("permutation: ",  Formulas.permutation(n, r) ,)
print("permutationWithRepetition: ",    Formulas.permutationWithRepetition(n, r))
