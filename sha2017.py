ct1= open("flag.pdf.enc",'rb').read()
ct=[]
for i in range(0,len(ct1),16):
	if(i+16>len(ct1)):
		ct.append(ct1[i:len(ct1)])
	else:
		ct.append(ct1[i:i+16])
print(len(ct1),len(ct))

fir8="".join(chr(ord(a)^ord(b)) for a,b in zip(ct[0][:8],"%PDF-1.3"))
print(fir8)
nex3="".join(chr(ord(a)^ord(b)) for a,b in zip(ct[35][8:11],"ace"))

las5="".join(chr(ord(a)^ord(b)) for a,b in zip(ct[6861][-5:],"\nstar"))
nexa="".join(chr(ord(a)^ord(b)) for a,b in zip(ct[6862][-5:], las5))
print(nexa)
key=fir8+nex3+las5
for i in range(0,len(ct)):
	nexa+="".join(chr(ord(a)^ord(b)) for a,b in zip(ct[i], key))
txt=open("flags.pdf","wb").write(nexa)
print("Done!")
