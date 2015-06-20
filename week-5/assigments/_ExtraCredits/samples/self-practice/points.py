import numbthy

class Point:
    x = long(0)
    y = long(0)
    def __eq__(self,n):
        if(self.x == n.x and self.y == n.y):
            return True
        else:
            return False
    def __init__(self,x0,y0):
        self.x = long(x0)
        self.y = long(y0)
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
        

zero = Point(0,0)

class ellipticCurve:
    a = long(1)
    b = long(0)
    n = long(0)
    def __init__(self,a0,b0,n0):
        self.a = long(a0)
        self.b = long(b0)
        self.n = long(n0)
    def __repr__(self):
        return "y^2 = x^3 + "+str(self.a)+"x + "+str(self.b)+" mod("+str(self.n)+")"

def addTwoPoints(E,p1,p2):
    if(p1 == zero):
        return p2
    elif(p2 == zero):
        return p1
    elif(p1.x == p2.x and p1.y == -p2.y):
        return Point(0,0)
    else:
        slope = 0
        if(p1 == p2):
            num = (3*p1.x*p1.x + E.a) % E.n
            den = (2*p1.y) % E.n
            slope = num * numbthy.invmod(den,E.n)
        else:
            num = (p2.y-p1.y) % E.n
            den = (p2.x-p1.x) % E.n
            slope = num * numbthy.invmod(den,E.n)
        x3 = (slope*slope-p1.x-p2.x) % E.n
        y3 = (slope*(p1.x-x3)-p1.y) % E.n
        return Point(long(x3),long(y3))

print addTwoPoints(ellipticCurve(3,8,13),Point(9,7),Point(1,8))
print addTwoPoints(ellipticCurve(3,8,13),Point(9,7),Point(9,7))
