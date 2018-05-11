#!/usr/bin/python


#So here's my very frist writeup for my first challenge that I solved during ASIS CTF QUALS 2018 (https://asisctf.com). 
#The name of the challenge was The_Early_School which was given under the crypto category for 30 points but it's a basic 
#python script reversing challenge and a very good challenge to test your coding skills.

#So here Crypto.Util.Number is just a module imported from pycrypto for using long_to_bytes and bytes_to_long in the script
#here flag might misguide you as a module but it's not 

from Crypto.Util.number import *
from flag import FLAG, round

#our main encryption function begins here
def encrypt(msg):

    assert set(msg) == set(['0', '1'])
    
    enc = [msg[i:i+2] + str(int(msg[i]) ^ int(msg[min(i+1, len(msg)-1)])) for i in range(0, len(msg), 2)]#length is incrsng with every call
    return ''.join(enc)

ENC = bin(bytes_to_long(FLAG))[2:]

for _ in xrange(round):
    ENC = encrypt(ENC)

fp = open('FLAG.enc', 'w')
fp.write(long_to_bytes(int(ENC, 2)))
fp.close()
'''
So after going through the above program we can figure out a few things:
1) our encrypted flag is being written to a file called 'FLAG.enc'.Before writing to the file our flag is converted from long int 
	to corresponding string
2) FLAG is changed to corresponding binary and the resultant is sent 'round' times to the function round as 'msg'
3) Inside the encrypt function the first line checks whether 'msg' is of binary format
4) The crux of our given code line that follows...
	enc = [msg[i:i+2] + str(int(msg[i]) ^ int(msg[min(i+1, len(msg)-1)])) for i in range(0, len(msg), 2)]

5) Here 2 bytes of the message are taken at a time and appended with a single character whose integer value is given by,
			position= (ascii of current character ^ msg[minimum of (i+1) and len(msg)-1])
		on each iteration is counter is incremented by 2 and the next two characters are taken. With each iteration one character is addded 
		in the string.
6) With the resultant string step 5 is repeated and this done 'round' times.

EXPLOIT:
So we know that on each iteration an extra character is been added. So our job is to remove those extra characters and get the flag.
For doing this we first start with removeing the characters at index positions which are multiple of 3's. Then we do the same with the 
resultant string i.e. the string we get after removing the characters. And after a few iterations we get our flag!!!
			FLAG::ASIS{50_S1mPl3_CryptO__4__warmup____}'''