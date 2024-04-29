from math import gcd

class RSA:

    def __init__(self, p, q):
        self.p = self.getNearestPrime(p)
        self.q = self.getNearestPrime(q)
        while self.p == self.q:
            self.q -= 1
            self.q = self.getNearestPrime(self.q)
        self.n = self.p * self.q
        self.phi = (self.p-1)*(self.q-1)
        self.e = self.getE()
        self.d = self.getD()

    def getNearestPrime(self, p):
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

    def getE(self):
        e = 2
        while e < self.phi:
            if gcd(e, self.phi) == 1 and self.isPrime(e):
                return e
            e += 1
    
    def getD(self):
        d = 2
        while d < self.phi:
            if (d * self.e) % self.phi == 1:
                return d
            d += 1

    def encrypt(self, message):
        tab = []
        for char in message:
            if ord(char) > self.n:
                raise ValueError(f"Character '{char}' is not supported by the current RSA configuration")
            else:
                tab.append(pow(ord(char), self.e, self.n))
        return tab
    
    def decrypt(self, message):
        result = ''
        for encrypted_char in message:
            result += chr(pow(encrypted_char, self.d, self.n))
        return result