Ruby 2.2
```
Only adding hints... No exact solution will be provided..
```
Adding headers...
```rb
require 'openssl'
require 'digest'
```
Add keys given in <a href="https://github.com/ashumeow/cryptography-I/blob/master/week-2/assignments/_ExtraCredit/question.md">question</a>
```
```
Convert to ASCII
```rb
def toASCII(hex)
  s = ''
  while hex > 0
    p = hex & 0xff
    hex = hex >> 8
    s = p.chr + s
  end
  return s
end
```
Encryption
```rb
def encrypt(data, key, iv, cipher_type)
    aes = OpenSSL::Cipher::Cipher.new(cipher_type)
    aes.encrypt
    aes.key = key
    aes.iv = iv if iv != nil
    aes.update(data) + aes.final
end
```
Decryption
```rb
def decrypt(encrypted_data, key, iv, cipher_type)
    aes = OpenSSL::Cipher::Cipher.new(cipher_type)
    aes.decrypt
    aes.key = key
    aes.iv = iv if iv != nil
    aes.update(encrypted_data) + aes.final
end
```
