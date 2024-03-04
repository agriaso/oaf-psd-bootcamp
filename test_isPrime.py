#test cases for isPrime, which returns True if the number is Prime
from isPrime import isPrime

#these 3 tests confirm the first if statement works
def test_isPrime_negative():
    assert isPrime(-2) == False

def test_isPrime_zero():
    assert isPrime(0) == False

def test_isPrime_smallnumbers():
    assert isPrime(2) == True

#these two tests redundantly check the 2nd if statement
def test_isPrime_evennum():
    assert isPrime(4) == False

def test_isPrime_nonprimeoddnum():
    assert isPrime(15) == False

#these tests confirm the functionality of the for loop
#that generates divisors to test primality
def test_isPrime_primenum():
    assert isPrime(17) == True

def test_isPrime_largenumber():
    assert isPrime(22409) == True