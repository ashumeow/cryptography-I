<b>
```
1. Key Derivation
```
</b>
<b>Key Derivation Function (KDF)</b><br>
I.<a href="http://geekresearchlab.net/coursera/crypto1/key-1.jpg">Introduction</a><br>
II.<a href="http://geekresearchlab.net/coursera/crypto1/key-2.jpg">Definition</a><br>
III.<a href="http://geekresearchlab.net/coursera/crypto1/key-3.jpg">Question: Purpose of CTX</a><br>
IV.<a href="http://geekresearchlab.net/coursera/crypto1/key-4.jpg">Discussing what if source key not uniform</a><br>
V.<a href="http://geekresearchlab.net/coursera/crypto1/key-5.jpg">Extract-then-Expand paradigm</a><br>
VI.<a href="http://geekresearchlab.net/coursera/crypto1/key-6.jpg">HKDF</a><br>
<code>HKDF is a KDF from HMAC.</code><br>
VII.<a href="http://geekresearchlab.net/coursera/crypto1/key-7.jpg">Password-based KDF (PBKDF)</a>
<b>
```
2. Deterministic Encryption
```
</b>
<b>Deterministic Encryption</b><br>
I.<a href="http://geekresearchlab.net/coursera/crypto1/det-1.jpg">Need for Deterministic Encryption</a><br>
II.Problem (<a href="http://geekresearchlab.net/coursera/crypto1/det-2.jpg">Part one</a> and 
<a href="http://geekresearchlab.net/coursera/crypto1/det-2-1.jpg">Part two</a>)<br>
III.<a href="http://geekresearchlab.net/coursera/crypto1/det-3.jpg">Solution</a><br>
IV.<a href="http://geekresearchlab.net/coursera/crypto1/det-4.jpg">Deterministic CPA Security</a><br>
V.<a href="http://geekresearchlab.net/coursera/crypto1/det-5.jpg">Common mistakes</a><br>
VI.<a href="http://geekresearchlab.net/coursera/crypto1/det-6.jpg">Question on whether counter mode is CPA secure or not</a>
<b>
```
3. Deterministic Encryption : SIV and PRP
```
Construction of Deterministic Encryption <br></b>
I. Construction 1: Synethrtic IV (SIV) <br>
I.A.<a href="http://geekresearchlab.net/coursera/crypto1/11-1.jpg">Theorem</a><br>
I.B.<a href="http://geekresearchlab.net/coursera/crypto1/11-2.jpg">Ensuring ciphertext integrity</a><br>
I.C.<a href="http://geekresearchlab.net/coursera/crypto1/11-3.jpg">Free deterministic auth. encryption</a><br>
II. Construction 2: Using PRP <br>
II.A.<a href="http://geekresearchlab.net/coursera/crypto1/11-4.jpg">Theorem</a><br>
II.B.<a href="http://geekresearchlab.net/coursera/crypto1/11-5.jpg">EME: Constructing a wide block PRP</a><br>
II.C.<a href="http://geekresearchlab.net/coursera/crypto1/11-6.jpg">PRP-based Free deterministic auth. encryption</a><br>
II.D.<a href="http://geekresearchlab.net/coursera/crypto1/11-7.jpg">PRP-based deterministic auth. encryption</a>
<b>
```
4. Tweakable Encryption
```
</b>
I. Disk Encryption<br>
I.A.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-1.jpg">Lemma</a><br>
I.B.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-2.jpg">How it's done and it's problem?</a><br>
I.C.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-3.jpg">Solution</a><br>
I.D.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-4.jpg">Much better solution -- Tweakable block ciphers</a> and 
<a href="http://geekresearchlab.net/coursera/crypto1/tweak-5.jpg">Secure tweakable block ciphers</a><br>
I.D.I.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-6.jpg">Example 1: Trivial Construction</a><br>
I.D.II.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-7.jpg">Example 2: XTS tweakable block cipher</a><br>
I.D.III.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-8.jpg">Question related to it.</a><br>
I.E.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-9.jpg">Disk Encryption using XTS</a><br>
II.<a href="http://geekresearchlab.net/coursera/crypto1/tweak-10.jpg">Summary</a>
<b>
```
5. Format preserving encryption
```
</b>
I.<a href="http://geekresearchlab.net/coursera/crypto1/preserve-1.jpg">Encrypting credit card numbers</a><br>
II.<a href="http://geekresearchlab.net/coursera/crypto1/preserve-2.jpg">Format Preserving Encryption (FPS)</a><br>
III.Construction <br>
III.A.<a href="http://geekresearchlab.net/coursera/crypto1/preserve-3.jpg">Step-1</a><br>
III.B.<a href="http://geekresearchlab.net/coursera/crypto1/preserve-4.jpg">Step-2</a><br>
III.C.<a href="http://geekresearchlab.net/coursera/crypto1/preserve-5.jpg">Security</a><br>
```
```
<a href="http://geekresearchlab.net/coursera/crypto1/xyz.jpg">FURTHER READINGS</a>
