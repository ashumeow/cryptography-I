I. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-1.jpg">Introduction</a><br>
<code>The common mistake made in software projects are the "incorrect combination of encrypted and integrity mechanisms".</code><br>
<br>
II. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-2.jpg">Combining MAC and ENC (CCA)</a><br>
<code>Three options -- SSL, IPSec, SSH</code><br><br>
<code>Which is more secure? </code><br>
<code>SSH -- The output of the MAC algorithm must leak some bits, so it's not secure.</code><br>
<code>This method is known as "encrypt-and-mac". </code><br>
<br>
<code>IPSec (Recommended) -- Any modification in the ciphertext can be easily detected. </code><br>
<code>This method is known as "encrypt-then-mac".</code><br>
<br>
<code>SSL -- CBC encryption system being combined with the MAC.. where, the result would be vulnerable to ciphertext attack.</code><br>
<code>How? - Bad interaction between the encryption scheme and the MAC algorithm which is why it causes such SSL attack.</code><br>
<code>This method is known as "mac-then-encrypt".</code><br>
<br>
III. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-3.jpg">Authenticated Encryption (A.E.)</a><br>
<br>
IV. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-4.jpg">Standards</a><br><br>
V. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-5.jpg">OpenSSL</a> -- an example API <br>
<br>
VI. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-6.jpg">MAC Security</a><br>
<br>
VII. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-7.jpg">OCB: Direct construction from a PRP</a><br>
<br>
VIII. <a href="http://geekresearchlab.net/coursera/crypto1/crypto-4-4-8.jpg">Performance</a>
