#This is the week 2 assignment for OAF PSD
#This code checks if a number is prime
from math import isqrt

def isPrime(number):
    #this code will not identify if a negative number is prime
    if number <= 3:
        return number > 1
    #if the number is even or divisible by 3
    if (number % 2 == 0) or (number % 3 == 0):
        return False
    #use square root as a limit for checking potential divisors
    limit = isqrt(number)

    #skip numbers that are divisible by 2 and 3
    for i in range(5, limit+1, 6):
        #check if current number & i+2
        #this logic ensures untested numbers are not skipped
        if number % i == 0 or number % (i+2) == 0:
            return False
    
    #if the while loop expires, return True
    return True