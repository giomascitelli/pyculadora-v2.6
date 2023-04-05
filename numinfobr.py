import numpy as np

# Definição das funções que recebem os resultados das operações e retornam as informações
def evenOdd(calc):
    if calc % 2 == 0:
        return "\n esse número é par."
    else:
        return "\n esse número é ímpar."

def isPrime(x):
    if x < 2:
        return "\n esse número é composto."
    elif x == 2:
        return "\n esse número é primo."  
    for n in np.arange(2, x):
        if x % n == 0:
            return "\n esse número é composto."
    return "\n esse número é primo."

def divisible(x):
    divisors = []
    for nums in np.arange(1, 501):
        if x % nums == 0:
            divisors.append(nums)
        
    return f"\ndivisível por {divisors}"