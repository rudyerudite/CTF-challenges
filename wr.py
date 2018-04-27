from pwn import *
import string
dictionary=string.ascii_letters + string.digits + string.punctuation


#console.log_level = "debug"

conn=remote("chal1.swampctf.com",1450)
def apple(pt):
    
    conn.send(pt+"\n")
    return conn.recvline()
    
ans=""
pt="singing"
l=1
f=True
pad_len=48
h2=""
while (len(pt)>5):#condition to be given
    pt="A"*(pad_len-l)
        #h1=sending 47 A's initially for getting the last character of flag
    h1=apple(pt) #sending my first pt to
    print("my ct which's to be decoded :"+h1)
        #while f:

    for i in range(len(dictionary)):#iterating thru each 256 characters
        h2=apple(ans+dictionary[i]+pt)
                #h2=rcvng the equivalent ct
        if(h2==h1):
            f=False
            break
    ans+=dictionary[i]
    print(ans)
    f=True
    l+=1
        
                     
print("flag is:"+ans)