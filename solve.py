from signal import alarm
from Crypto.Util.number import *

p = 160634950613302858781995506902938412625377360249559915379491492274326359260806831823821711441204122060415286351711411013883400510041411782176467940678464161205204391247137689678794367049197824119717278923753940984084059450704378828123780678883777306239500480793044460796256306557893061457956479624163771194201
g = 2
#p is 1024 bit long
bits = size(p)
print(bits)
print(4+bits//4)
flag=""

with open("flag", "r") as f:
    flag = f.readline().strip().encode("latin1")
    m = bytes_to_long(flag) 
print(size(m))

def run(input):
        line = input[:4+bits//4]
        s = int(line, 0) #                 Note: input is HEX
        c = pow(g, m ^ s, p)
        return hex(c)

if __name__ == "__main__":
    fla=""
     #2^m mod p
    c0=int(run(hex(0)),0)
    for i in range(size(p)):
        d=hex(2**i)
        '''if(d[-1]=='L'):
            cn=int(run(d[:-1]),0)
        else:'''
        cn=int(run(d),0)
        #comparing the actual answer with the one made by me
        if((c0*pow(g,2**i,p))%p  == cn):
            fla+='0'
        else:
            fla+='1'#else this would need a condition 2**(m-n)modp to fulfill but here we use 2**(m+n)mod p
    print(fla)
    fla=int(fla[::-1],2)
    
    print((long_to_bytes(fla)))
    



