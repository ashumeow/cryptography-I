Only Solution hints (almost 75%) will be provided with <a href="https://github.com/ashumeow/cryptography-I/tree/master/week-3/assignments/_ExtraCredit/tests/python">some more</a>... ;)
<br><br>
Headers ;)
```py
import sys    
import os    
from Crypto.Hash import SHA256    
ig_size=1024  
```
The internals... ;)
```py
def ig_hash(ig_location):    
    f=open(path_file_name,'rb')    
    r_file=f.read()    
    block_quantity=len(r_file)/ig_size   
    h = SHA256.new()    
    h.update(r_file[block_quantity*ig_size:])    
    hash_result=''    
    for idx in range(block_quantity-1,-1,-1):    
        hash_result=r_file[idx*ig_size:(idx+1)*ig_size]    
        hash_result+=h.digest()    
        h = SHA256.new()    
        h.update(hash_result)    
    return h.hexdigest()
```
Fetching the internals... ;)
```py
def fetch_ig(ig_location):    
    f=open(ig_location,'rb')    
    for idx in reversed(range(0,os.path.getsize(ig_location),ig_size)):    
        f.seek(idx)    
        yield f.read(ig_size)    
    f.close()
```
Then... The final move is given to you... =D
```
Duh! Done.
```
