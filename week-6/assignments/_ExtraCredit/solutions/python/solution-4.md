```
similar to soultion 1, 2, 3

More like continuation...
```
```
solution hints
```
```py
def ig_euclid(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
```
```py
## Running RSA

## Add codes
```
```py
## Remove initial padding

## add codes
```
```py
## status: Received output
```
