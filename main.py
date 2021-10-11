import Formulas
import coinProb
import diceProb
import Homework1





#coinProb.throwACoin()
#diceProb.rollOneDie()
#diceProb.rollTwoDice()
#diceProb.calculateProbability(4)
#diceProb.calculateAllProbability()
#diceProb.calculateTwoDiceProbability()


n = int(input("Enter the number of obj: "))
r = int(input("How many obj selected: "))

# Formulas
print("Combination: ",  Formulas.combination(n, r))
print("Combination With Repetition: ", Formulas.combinationWithRepetition(n, r))
print("Permutation: ",  Formulas.permutation(n, r) ,)
print("Permutation With Repetition: ",    Formulas.permutationWithRepetition(n, r))
