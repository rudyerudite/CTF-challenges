#Revolutional Secure Angou Writeup

In this challenge we are provided with 3 files. The file generator.rb is the encryption script in ruby. We will now analyze this script and see if we can find any odds which may favour us to find our flag!

```ruby
require 'openssl'

e = 65537
while true
  p = OpenSSL::BN.generate_prime(1024, false)
  q = OpenSSL::BN.new(e).mod_inverse(p) #size 1024,exploit!!!
  next unless q.prime?
  puts(q.prime?)#pq prime
  puts(q)
  puts("dex")
  key = OpenSSL::PKey::RSA.new
  key.set_key(p.to_i * q.to_i, e, nil)#generating n and e key pair
  File.write('publickey.pem', key.to_pem)
  File.binwrite('flag.encrypted', key.public_encrypt(File.binread('flag')))
  break
end```

So after 
