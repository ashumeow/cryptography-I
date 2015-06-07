######################################################################################
# NUMBTHY.PY
# Basic Number Theory functions implemented in Python
# Note: Currently requires Python 2.x (uses +=, %= and other 2.x-isms)
# Note: Currently requires Python 2.3 (uses implicit long integers - could be back-ported though)
# Note: Not yet tested with Python 3.x
# Author: Robert Campbell, <campbell@math.umbc.edu>
# Date: 24 Nov, 2012
# Version 0.6
# License: Simplified BSD (see details at bottom)
######################################################################################
"""Basic number theory functions.
   Functions implemented are:
   		gcd(a,b) - Compute the greatest common divisor of a and b.
   		xgcd(a,b) - Find [g,x,y] such that g=gcd(a,b) and g = ax + by.
   		powmod(b,e,n) - Compute b^e mod n efficiently.
   		invmod(b,n) - Compute 1/b mod n.
   		isprime(n) - Test whether n is prime using a variety of pseudoprime tests.
   		isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.
   		isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.
		eulerphi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.
		carmichaellambda(n) - Computer Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
   		factor(n) - Find a factor of n using a variety of methods.
   		factors(n) - Return a sorted list of the prime factors of n.
   		factorPR(n) - Find a factor of n using the Pollard Rho method
		isprimitive(g,n) - Test whether g is primitive - generates the group of units mod n.
		sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
		TSRsqrtmod(a,grpord,n) - Compute sqrt(a) mod n using Tonelli-Shanks-RESSOL algorithm.
   A list of the functions implemented in numbthy is printed by the command info()."""
   
   
Version = 'NUMBTHY.PY, version 0.6, 24 Nov, 2012, by Robert Campbell, <campbell@math.umbc.edu>'

import math  # Use sqrt, floor

def gcd(a,b):
	"""gcd(a,b) returns the greatest common divisor of the integers a and b."""
	if a == 0:
		return abs(b)
	return abs(gcd(b % a, a))
	
def powmod(b,e,n):
	"""powmod(b,e,n) computes the eth power of b mod n.  
	(Actually, this is not needed, as pow(b,e,n) does the same thing for positive integers.
	This will be useful in future for non-integers or inverses.  Currently assumes e>0.)"""
	accum = 1; i = 0; bpow2 = b
	while ((e>>i)>0):
		if((e>>i) & 1):
			accum = (accum*bpow2) % n
		bpow2 = (bpow2*bpow2) % n
		i+=1
	return accum
	
def xgcd(a,b):
	"""xgcd(a,b) returns a list of form [g,x,y], where g is gcd(a,b) and
	x,y satisfy the equation g = ax + by."""
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
			
def isprime(n):
	"""isprime(n) - Test whether n is prime using a variety of pseudoprime tests."""
	if (n in [2,3,5,7,11,13,17,19,23,29]): return True
	return isprimeE(n,2) and isprimeE(n,3) and isprimeE(n,5)
			
def isprimeF(n,b):
	"""isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
	return (pow(b,n-1,n) == 1)
	
def isprimeE(n,b):
	"""isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
	if (not isprimeF(n,b)): return False
	r = n-1
	while (r % 2 == 0): r //= 2
	c = pow(b,r,n)
	if (c == 1): return True
	while (1):
		if (c == 1): return False
		if (c == n-1): return True
		c = pow(c,2,n)
	
def factor(n):
	"""factor(n) - Find a prime factor of n using a variety of methods."""
	if (isprime(n)): return n
	for fact in [2,3,5,7,11,13,17,19,23,29]:
		if n%fact == 0: return fact
	return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned
			
def factors(n):
	"""factors(n) - Return a sorted list of the prime factors of n."""
	if (isprime(n)):
		return [n]
	fact = factor(n)
	if (fact == 1): return "Unable to factor "+str(n)
	facts = factors(n/fact) + factors(fact)
	facts.sort()
	return facts

def factorPR(n):
	"""factorPR(n) - Find a factor of n using the Pollard Rho method.
	Note: This method will occasionally fail."""
	for slow in [2,3,4,6]:
		numsteps=2*math.floor(math.sqrt(math.sqrt(n))); fast=slow; i=1
		while i<numsteps:
			slow = (slow*slow + 1) % n
			i = i + 1
			fast = (fast*fast + 1) % n
			fast = (fast*fast + 1) % n
			g = gcd(fast-slow,n)
			if (g != 1):
				if (g == n):
					break
				else:
					return g
	return 1
	
def eulerphi(n):
	"""eulerphi(n) - Computer Euler's Phi function of n - the number of integers
	strictly less than n which are coprime to n.  Otherwise defined as the order
	of the group of integers mod n."""
	thefactors = factors(n)
	thefactors.sort()
	phi = 1
	oldfact = 1
	for fact in thefactors:
		if fact==oldfact:
			phi = phi*fact
		else:
			phi = phi*(fact-1)
			oldfact = fact
	return phi
	
def carmichaellambda(n):
	"""carmichaellambda(n) - Computer Carmichael's Lambda function 
	of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
	Otherwise defined as the exponent of the group of integers mod n."""
	thefactors = factors(n)
	thefactors.sort()
	thefactors += [0]  # Mark the end of the list of factors
	carlambda = 1 # The Carmichael Lambda function of n
	carlambda_comp = 1 # The Carmichael Lambda function of the component p**e
	oldfact = 1
	for fact in thefactors:
		if fact==oldfact:
			carlambda_comp = (carlambda_comp*fact)
		else:
			if ((oldfact == 2) and (carlambda_comp >= 4)): carlambda_comp /= 2 # Z_(2**e) is not cyclic for e>=3
			if carlambda == 1:
				carlambda = carlambda_comp
			else:
				carlambda = (carlambda * carlambda_comp)/gcd(carlambda,carlambda_comp)
			carlambda_comp = fact-1
			oldfact = fact
	return carlambda
	
def isprimitive(g,n):
	"""isprimitive(g,n) - Test whether g is primitive - generates the group of units mod n."""
	if gcd(g,n) != 1: return False  # Not in the group of units
	order = eulerphi(n)
	if carmichaellambda(n) != order: return False # Group of units isn't cyclic
	orderfacts = factors(order)
	oldfact = 1
	for fact in orderfacts:
		if fact!=oldfact:
			if pow(g,order/fact,n) == 1: return False
			oldfact = fact
	return True
	
def invmod(a,n):
	"""invmod(b,n) - Compute 1/b mod n."""
	return xgcd(a,n)[1] % n

def sqrtmod(a,n):
	"""sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
	Currently n must be prime, but will be extended to general n (when I get the time)."""
	if(not isprime(n)): raise ValueError("*** Error ***:  Currently can only compute sqrtmod(a,n) for prime n.")
	if(pow(a,(n-1)/2,n)!=1): raise ValueError("*** Error ***:  a is not quadratic residue, so sqrtmod(a,n) has no answer.")
	return TSRsqrtmod(a,n-1,n)
	
def TSRsqrtmod(a,grpord,p):
	"""TSRsqrtmod(a,grpord,p) - Compute sqrt(a) mod n using Tonelli-Shanks-RESSOL algorithm.
	Here integers mod n must form a cyclic group of order grpord."""
	# Rewrite group order as non2*(2^pow2)
	ordpow2=0; non2=grpord
	while(not ((non2&0x01)==1)):
		ordpow2+=1; non2/=2
	# Find 2-primitive g (i.e. non-QR)
	for g in range(2,grpord-1):
		if (pow(g,grpord/2,p)!=1):
			break
	g = pow(g,non2,p)
	# Tweak a by appropriate power of g, so result is (2^ordpow2)-residue
	gpow=0; atweak=a
	for pow2 in range(0,ordpow2+1):
		if(pow(atweak,non2*2**(ordpow2-pow2),p)!=1):
			gpow+=2**(pow2-1)
			atweak = (atweak * pow(g,2**(pow2-1),p)) % p
			# Assert: atweak now is (2**pow2)-residue
	# Now a*(g**powg) is in cyclic group of odd order non2 - can sqrt directly
	d = invmod(2,non2)
	tmp = pow(a*pow(g,gpow,p),d,p)  # sqrt(a*(g**gpow))
	return (tmp*invmod(pow(g,gpow/2,p),p)) % p  # sqrt(a*(g**gpow))/g**(gpow/2)	
	
def info():
	"""Return information about the module"""
	print locals()

# import numbthy
# reload(numbthy)
# print numbthy.__doc__

############################################################################
# License: Freely available for use, abuse and modification
# (this is the Simplified BSD License, aka FreeBSD license)
# Copyright 2001-2012 Robert Campbell. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in 
#       the documentation and/or other materials provided with the distribution.
############################################################################
