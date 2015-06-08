import sys
import numbthy

def ig(a,b):
	## ig(a,b) returns a list of form [g,x,y], where g is gcd(a,b) and
	## x,y satisfy the equation g = ax + by.
	a1=1; b1=0; a2=0; b2=1; aneg=1; bneg=1
	if(a < 0):
		a = -a; aneg=-1
	if(b < 0):
		b = -b; bneg=-1
	while (1):
		quot = -(a // b)
		a = a % b
		a1 = a1 + quot*a2; b1 = b1 + quot*b2
		if(a == 0):
			return [b, a2*aneg, b2*bneg]
		quot = -(b // a)
		b = b % a;
		a2 = a2 + quot*a1; b2 = b2 + quot*b1
		if(b == 0):
			return [a, a1*aneg, b1*bneg]

a = 7
b = 23

print "a =", a
print "b =", b

def invmod(a,n):
## invmod(b,n) - Compute 1/b mod n
	return ig(a,n)[1] % n

a = 7
n = 23

print "Modular inverse for", a, "=", invmod(a, n)

## the value of a and b came as 7, 23
## but i was adding in answer column as 10, -3
## i feel so dumb, my mind went somewhere
## Why did i add as -3??
## -3 makes no sense. It was like adding coffee with cheese instead of sugar.
## the python execution came as 7, 23 for a and b
## Something is wrong with me. Meow! :(

## the inverse answer came as 10 while executing, 
## but it was wrong mathematically.

## i think that the value of inv(a, b) must come as 1, 
## but mine is wrong since i got inv(a, b) => 10

## Related link
## https://github.com/ashumeow/cryptography-I/tree/master/week-5/notes/2-Intro-to-Number-Theory
