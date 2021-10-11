#Factiorial
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


# Combination
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

# Combination with repetition
def combinationWithRepetition(n, r):
    return factorial(n + r - 1) / (factorial(r) * factorial(n - 1))

#Permutation
def permutation(n, r):
    return factorial(n) / factorial(n-r)

#Permutation with repetition
def permutationWithRepetition(n, r):
    return n**r




        
            
