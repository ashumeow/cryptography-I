For the <a href="">question</a>, some solution hints (almost 80% hints) are provided,
<br><br>
Adding header
```rb
require 'openssl'
```
Adding <code>SHA-256</code>
```rb
sha256 = OpenSSL::Digest::SHA256.new
```
And some more...
```rb
blocks = Array.new
data = Array.new
```
Targetted file... the video link file that's shared in question
```rb
file_ig = "ig/2.mp4"
```
Hello data...
```rb
file_ig_data = File.open(file_ig)
```
Start Hex... ;)
```rb
hex = file_ig_data.read().unpack('H*')
```
Then... :)
```
Add some FOR-LOOPS (^_^)
```
Finally... Hello last step!
```rb
puts sha256.digest(blocks.last).unpack('H*')
```
Done!
```git
dell@DELL3521 /d/Ruby22-x64/bin
$ ruby ig/hash_test.rb
```
There comes the solution ;)
