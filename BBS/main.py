import math, random
from test import Tester

class BBS_generator:

    p = 0
    q = 0
    n = 0
    series_length = 20000

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = self.calculateN(p, q)

    def generate(self):
        x = self.__generateSeed()
        x0 = pow(x, 2, self.n)
        result = ''
        for _ in range(self.series_length):
            x0 = pow(x0, 2, self.n)
            if x0 % 2 == 0:
                result += '0'
            else:
                result += '1'
        
        return result

    def __generateSeed(self):
        seed = 0
        while seed < self.n:
            seed = random.randint(5000, self.n-1)
            if math.gcd(seed, self.n) == 1:
                print('-----------------SEED------------------')
                print(f"Seed: {seed}")
                return seed

    def calculateN(self, p, q):
        p = self.__findBellNumber(p)
        q = self.__findBellNumber(q)
        while q == p:
            q = self.__findBellNumber(q)
        return p * q

    def __findBellNumber(self, number):
        if number % 4 == 3 and self.__isPrime(number):
            return number
        decreasingNumber = number - 1
        increasingNumber = number + 1
        while True:
            if decreasingNumber % 4 == 3 and self.__isPrime(decreasingNumber):
                return decreasingNumber
            if increasingNumber % 4 == 3 and self.__isPrime(increasingNumber):
                return increasingNumber
            decreasingNumber -= 1
            increasingNumber += 1

    def __isPrime(self, number):
        if number < 2:
            return False
        for i in range(2, int(self.n**0.5)+1):
            if number % i == 0:
                return False
        return True
    
if __name__ == "__main__":
    p = 5124
    q = 9871
    bbs = BBS_generator(p, q)
    tester = Tester(bbs.generate())
    print('-----------------TESTS-----------------')
    tester.testSeries()
    print('------------------END------------------')