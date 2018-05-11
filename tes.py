from Crypto.Util.number import *

fp = open('FLAG.enc', 'r')
#fp.write(long_to_bytes(int(ENC, 2)))

def decrypt(msg):
	print("Lemme try...")
	v=""
	for i in range(len(msg)-1):
		if((i+1)%3!=0):
			v+=msg[i]
	print("Check this one!!!")
	print(long_to_bytes(int(v,2)))
	return v

dec=""
with open("FLAG.enc") as f:
	for line in f:
		dec+=bin(bytes_to_long(line.strip()))[2:]

		
for i in range(100):
	dec=decrypt(dec)

