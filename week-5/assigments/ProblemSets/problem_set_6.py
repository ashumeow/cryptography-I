##Solve the equation 3x+2=7 in Z19.
#################################
##Solution:
##- Formula ;) => x = -b * a^(-1)
##- x = (7-2) * ig_mod(3,19) in Z19

import sys

def ig(x, y):
    a,b, u,v = 0,1, 1,0
    while x != 0:
        q, r = y//x, y%x
        m, n = a-u*q, b-v*q
        y,x, a,b, u,v = x,r, u,v, m,n
    return y, a, b

def ig_mod(a, m):
    g, x, y = ig(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

b = 2
a = 3
c = 7
p = 19

x = ((c-b) * ig_mod(a,p)) % p
print "x =", x

## Related link
## https://github.com/ashumeow/cryptography-I/tree/master/week-5/notes/2-Intro-to-Number-Theory
