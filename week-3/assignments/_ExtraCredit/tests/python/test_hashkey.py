import sys

rawhex1 = b'\x11'*1024
rawhex2 = b'\x22'*1024
rawhex3 = b'\x33'*1024
rawhex4 = b'\x44'*773
e1 = open('crypto-1/week3/ig1','wb')
e2 = open('crypto-1/week3/ig2','wb')
e3 = open('crypto-1/week3/ig3','wb')
e4 = open('crypto-1/week3/ig4','wb')
t1 = open('crypto-1/week3/ig','wb')
e1.write(rawhex1)
e2.write(rawhex2)
e3.write(rawhex3)
e4.write(rawhex4)
t1.write(rawhex1+rawhex2+rawhex3+rawhex4)
t1.close()
e1.close()
e2.close()
e3.close()
e4.close()

## This sample code script has been extracted from the coursera discussion forum.
