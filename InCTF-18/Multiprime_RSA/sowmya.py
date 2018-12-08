from Crypto.Util.number import *
import gmpy2
import math
import binascii

#(13**4)*(gmpy2.mpz(mid)**7)
def find(n,low,high):
	mid = (low+high)//2
	if(high<=low):
		print(low)
		return low
	elif((13**4)*(gmpy2.mpz(mid)**7)>n):
		return find(n,low,mid-1)
	else:
		return find(n,mid+1,high)


n = 63503276937852850446665985957390379307440024971021230431993893491881624345662352363811917592750766531203356043483026044031384884152397966752357920486434617823027122279415036554847130392423900715402785773280279146047931988844559054831429226564586447952491921350715788091186848490634584031960739647318023686632925058823647108880767478971118608237886300608306051261004692404756371356302701018432847524301182730267480301933745056302779577973416730232149313436165949340434895975694570102514920769870034226468745369298052361213865705054347251550807
e = 65537
c = "464757bacf2e67e0e253adbd024ee12c9ab5a7250f2caadc99ba4231565635345ab549790aaf472a2efad32a81efbee50127c476c3dab7313168912a577e61012a56b1de50a72f30a23642749ad2dda71b6d11b488d79511d0298d91640fdc61fbb1332156596e75fe56776361af653c5b14a90d555e0eb6048cf28dcc89ec752a9f46bb7d8c2a5cc16d2ac0d0dafae06ef95419fca0384ed9168ecd8157a0478999cfc347bcf2487bd3171fd9723acc336a6bf5c1a27e4863a0a8f784ee85d79fe9c934190f95ddb8604a0453978df7bee1071f12aea363fadfa9e0bde9792328"

low = 2**(255)
high = 2**(256)

def next_prime(n):
    num = n + 1
    while True:
        if isPrime(num):
            return num
        num += 1

guess = find(n,low,high)
for i in range(-1000+guess,1000+guess):
	if(n%i==0):
		p = i
		print("aya")
		break

q = next_prime(p*13)
r =  next_prime(p*q)
s =  next_prime(r*q)
ni = p*q*r*s
print(ni==n)
'''q = 13*p
r = p*p*13
s = 13*p*p*13*p

print(p*q*r*s==n)'''
phi = (p-1)*(q-1)*(r-1)*(s-1)

d = inverse(e,phi)

c = bytes_to_long(c.decode("hex"))
c = pow(c,d,n)
print(long_to_bytes(c))

print("ENTER THE STRING")
input_string = raw_input()
str1 = binascii.unhexlify(input_string)

for i in range(0,255):
	str2=""
	for j in range(len(str1)):
		str2 += chr(ord( str1[j] ) ^ i)
		if "inctf{" in str2:
			print(str2)







'''
p
13*p
p*13*p
13*p*p*13*p'''