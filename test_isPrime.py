#test cases for isPrime, which returns True if the number is Prime
from .isPrime import isPrime

def test_isPrime():
    assert isPrime(-2) == False
    assert isPrime(0) == True
    assert isPrime(4) == False
    assert isPrime(15) == False
    assert isPrime(17) == True