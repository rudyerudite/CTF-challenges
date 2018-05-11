from Crypto.Util.number import *

fp = open('FLAG.enc', 'r')
#fp.write(long_to_bytes(int(ENC, 2)))

def decrypt(msg):
	print("Lemme try...")
	v=""
	for i in range(len(msg)-1):
		if((i+1)%3!=0):
			v+=msg[i]
	#if("asis" in long_to_bytes(int(v,2))):
	print("Hagrid's right!!!")
	print(long_to_bytes(int(v,2)))
	return v

dec=""
with open("FLAG.enc") as f:
	for line in f:
		dec+=bin(bytes_to_long(line.strip()))[2:]

		
for i in range(100):
	dec=decrypt(dec)

#for i in range(100):
	#dec=decrypt(dec)
'''def encrypt(msg):
	enc = [msg[i:i+2] + str(int(msg[i]) ^ int(msg[min(i+1, len(msg)-1)])) for i in range(0, len(msg), 2)]
	enc="".join(enc)
	print(enc)
	return enc

def decrytp(msg):
	d=""
	for i in range(len(msg)-1):
		if((i+1)%3!=0):
			d+=msg[i]
	return d

for j in range(2):
	enc=encrypt(enc)

for j in range(2):
	enc=decrytp(enc)
print(enc)
print(msg)
if(enc==msg):
	print("Hagrid's right")
else:
	print("Slytherin's upto smth")
'''


