import os, sys
from Crypto.Cipher import AES

'''fn = sys.argv[1]
data = open(fn,'rb').read()

# Secure CTR mode encryption using random key and random IV, taken from
# http://stackoverflow.com/questions/3154998/pycrypto-problem-using-aesctr
secret = os.urandom(16)
crypto = AES.new(os.urandom(32), AES.MODE_CTR, counter=lambda: secret) 

encrypted = crypto.encrypt(data)
open(fn+'.enc','wb').write(encrypted)'''
import array

class Secret(object):
  def __init__(self, secret=None):
    if secret is None: secret = os.urandom(16)
    self.secret = secret
    print(secret)
    self.reset()
  def counter(self):
    for i, c in enumerate(self.current):
      self.current[i] = c + 1
      if self.current: break
    print(self.current)
    return self.current.tostring()
  def reset(self):
    self.current = array.array('B', self.secret)

secret = Secret()
crypto = AES.new(os.urandom(32), AES.MODE_CTR, counter=secret.counter)
encrypted = crypto.encrypt(16*'a' + 16*'b' + 16*'c')
secret.reset()
print crypto.decrypt(encrypted)
