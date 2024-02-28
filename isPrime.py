#This is the week 2 assignment for OAF PSD
#This code checks if a number is prime

def isPrime(number):
    #this code will not identify if a negative number is prime
    if number < 0:
        return False
    #if the number is one of these, it's prime
    elif number in [0, 1, 2, 3]:
        return True
    #if the number is even, it can't be prime
    elif (number % 2 == 0):
        return False
    #check if anything divides the number
    else:
        i = 2
        while i < number:
            if number % i == 0:
                return False
            else:
                i += 1
        #if the while loop expires, return True
        return True