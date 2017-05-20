# Just a small Program to demonstrate overloading of 'print' function of class using __str__ and overloading of "+" operator using __add__


def gcd(m,n):
    if m%n != 0:
        return gcd(n,m%n)
    return n

class Fraction:

    def __init__(self,N= None,D = None):
        self.n=N
        self.d=D

    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def __add__(self, other):
        add = Fraction()
        add.n = self.n*other.d + other.n*self.d
        add.d = self.d * other.d
        ans = gcd(add.n,add.d)
        add.n=add.n/ans
        add.d=add.d/ans
        return add

    def __eq__(self, other):
        return self.n * other.d == self.d * other.n

    def __sub__(self, other):
        sub = Fraction()
        sub.n = self.n*other.d - other.n*self.d
        sub.d = self.d * other.d
        ans = gcd(sub.n,sub.d)
        sub.n=sub.n/ans
        sub.d=sub.d/ans
        return sub


n=int(raw_input("Enter Numerator: "))
d=int(raw_input("Enter Denominator: "))
f1=Fraction(n,d)
n=int(raw_input("Enter Numerator: "))
d=int(raw_input("Enter Denominator: "))
f2=Fraction(n,d)


f3 = f1-f2

print f3




