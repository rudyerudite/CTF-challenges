import binascii
import socket
#console.log_level = "debug"
s=socket.socket()
host="chal1.swampctf.com"
port=1450
ans=""
l=1
f=True
pad_len=48
h2=""
while (len(h2)!=128):#condition to be given
        s.connect((host,port))
        pt="A"*(pad_len-l)
        #h1=sending 47 A's initially for getting the last character of flag
        s.send(pt+"\n")
        h1=s.recv(1450)
        print("my ct which's to be decoded"+h1)
        while f:
	        #s.connect((host,port))
            for i in range(256):
                pt1=ans+chr(i)+pt
                s.send(pt1+"\n")
                h2=s.recv(1450)
                #h2=rcvng the equivalent ct
                if(h2==h1):
                    f=True
                    break
        ans+=chr(i)
        l+=1
s.close()              
print("flag is:"+ans)


        #sending part comes here
        #recv the ct


#recv a line from host
    

    
