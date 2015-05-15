```
Message Integrity:

The goal is to provide integrity, no confidentiality.

Examples:
-- Protecting public binaries on disk.
-- Protecting banner ads on web pages.

Message Integrity: Message Authentication Code (MAC)

Alice ---> Bob
With the help of inputting key, transfers a message.
The tag is generated through Message Signing Algorithm.
tag <- S(k,m)
Bob receives the message tag.
And it undergoes Message Verification Algorithm.
V(k,m,tag) = 'yes'
MAC I = (S,V) defined over (K,M,T) is a pair of algorithms,
where S(k,m) outputs t in T and V(k,m,t) outputs 'yes' or 'no'.

Integrity requires a secret key.
The attacker can easily modify message m and re-compute CRC.
CRC designed to detect random, not malicious errors.
Alice ---> Bob
Tag generation from Alice:
tag <- CRC(m)
Tag generation from Bob:
V(m,tag)='yes'
tag = CRC(m)
```
![](http://geekresearchlab.net/coursera/crypto1/MAC-secure.jpg)<br><br>
![](http://geekresearchlab.net/coursera/crypto1/MAC-secure-2.jpg)<br><br>
![](http://geekresearchlab.net/coursera/crypto1/MAC-secure-question.jpg)<br><br>
![](http://geekresearchlab.net/coursera/crypto1/MAC-secure-question-2.jpg)<br><br>
![](http://geekresearchlab.net/coursera/crypto1/MAC-secure-example.jpg)
