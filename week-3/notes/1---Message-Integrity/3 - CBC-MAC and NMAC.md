I.<a href="http://geekresearchlab.net/coursera/crypto1/00-review.jpg">Review</a><br>
<br>
II.Construction methods: <br>
II.A.Construction 1: <a href="http://geekresearchlab.net/coursera/crypto1/01-constr1.jpg">Encrypted CBC-MAC</a> (ECBC) <br>
<code>Without final step, the "raw CBC" can be used.</code><br>
<code>But, the raw CBC isn't secure. So. the final step is a very crucial one.</code><br>
II.B.Construction 2: <a href="http://geekresearchlab.net/coursera/crypto1/01-constr2.jpg">Nested MAC</a> (NMAC)<br>
<code>Remember that in ECBC, the output needs to be in X.</code><br>
<code>But in NMAC, the output needs to be in K.</code><br>
<code>Without final output, we get "cascade" which isn't a secure MAC.</code><br>
<code>To get a secure MAC, We need to map the element t to the K into the set X.</code><br>
II.C.<a href="http://geekresearchlab.net/coursera/crypto1/02-constr-example.jpg">Example</a> and Solution <a href="http://geekresearchlab.net/coursera/crypto1/02-constr-example-why.jpg">explaining why and how</a><br>
<br>
III.<a href="http://geekresearchlab.net/coursera/crypto1/03-why-last.jpg">Why the last encryption step in ECBC-MAC?</a><br>
<br>
IV.<a href="http://geekresearchlab.net/coursera/crypto1/04-analysis.jpg">ECBC-MAC and NMAC analysis</a> 
with an <a href="http://geekresearchlab.net/coursera/crypto1/04-analysis-eg.jpg">example</a><br>
<br>
V.Security Attacks (<a href="http://geekresearchlab.net/coursera/crypto1/05-sec-attack.jpg">Part one</a> and 
<a href="http://geekresearchlab.net/coursera/crypto1/05-sec-attack-2.jpg">Part two</a>)<br><br>
VI.<a href="http://geekresearchlab.net/coursera/crypto1/06-comparison.jpg">Comparison</a>
