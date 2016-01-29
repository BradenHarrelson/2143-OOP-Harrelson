class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        l = self.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator / l
        self.denominator = self.denominator / l
        if self.numerator == self.denominator:
            return"1"
        elif self.numerator > self.denominator:
            return("%d %d/%d" % (self.numerator // self.denominator, self.numerator % self.denominator, self.denominator))
        else:
            return "%d/%d" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def gcd(self,x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self,rhs):
        print("%d/%d + %d/%d = " % (self.numerator,self.denominator,rhs.numerator,rhs.denominator))
        if self.denominator == rhs.denominator:
            x = self.numerator + rhs.numerator
            y = self.denominator
            return fraction(x,y)
        elif self.denominator % rhs.denominator == 0:
            if self.denominator > rhs.denominator:
                g = self.denominator / rhs.denominator
                rhs.denominator = rhs.denominator * g
                rhs.numerator = rhs.numerator * g
            else:
                g = rhs.denominator / self.denominator
                self.denominator = self.denominator * g
                self.numerator = self.numerator * g
            x = self.numerator + rhs.numerator
            y = self.denominator
            return fraction(x,y)
            
        else:
            self.numerator = self.numerator * rhs.denominator
            rhs.numerator = rhs.numerator * self.denominator
            temp = self.denominator
            self.denominator = self.denominator * rhs.denominator
            rhs.denominator = rhs.denominator * temp
            x = self.numerator + rhs.numerator
            y = self.denominator
            return fraction(x,y)

if __name__ == '__main__':
    a = fraction(11,12)
    b = fraction(3,4)
    c = a + b
    print(c)
