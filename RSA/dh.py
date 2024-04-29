from random import randint

class DiffieHelman:

    def __init__(self, p):
        self.p = self.getP(p)
        self.g = 2
        self.x = self.genPrivateKey()
        self.y = self.genPrivateKey()
        self.X = pow(self.g, self.x, self.p)
        self.Y = pow(self.g, self.y, self.p)
        self.k_A = pow(self.Y, self.x, self.p)
        self.k_B = pow(self.X, self.y, self.p)

    def getP(self, p):
        while not self.isPrime(p):
            p -= 1
        return p
    
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def genPrivateKey(self):
        return randint(1000,9999)
