import string

#for i in string.printable:
	#print(i," ",hex(ord(i)))
l=[]
k=[]
j=[]

l="BB 02 9B 03 C4 04 6C 05 4A 06 2E 07 22 08 45 09 33 0A B8 0B D5 0C 06 0D 0A 0E BC 0F FA 10 79 11 24 12 E1 13 B2 14 BF 15 2C 16 AD 17 86 18 60 19 A4 1A B6 1B D8 1C 59 1D 87 1E 41 1F 94 20 77 21 F0 22 4F 23 CB 24 61 25 25 26 C0 27 97 28 2A 29 5C 2A 08 2B C9 2C 9F 2D 43 2E 4E 2F CF 30 F9 31 3E 32 6F 33 65 34 E7 35 C5 36 39 37 B7 38 EF 39 D0 3A C8 3B 2F 3C AA 3D C7 3E 47 3F 3C 40 81 41 32 42 49 43 D3 44 A6 45 96 46 2B 47 58 48 40 49 F1 4A 9C 4B EE 4C 1A 4D 5B 4E C6 4F D6 50 80 51 2D 52 6D 53 9A 54 3D 55 A7 56 93 57 84 58 E0 59 12 5A 3B 5B B9 5C 09 5D 69 5E BA 5F 99 60 48 61 73 62 B1 63 7C 64 82 65 BE 66 27 67 9D 68 FB 69 67 6A 7E 6B F4 6C B3 6D 05 6E C2 6F 5F 70 1B 71 54 72 23 73 71 74 11 75 30 76 D2 77 A5 78 68 79 9E 7A 3F 7B F5 7C 7A 7D CE 7E 0B 7F 0C 80 85 81 DE 82 63 83 5E 84 8E 85 BD 86 FE 87 6A 88 DA 89 26 8A 88 8B E8 8C AC 8D 03 8E 62 8F A8 90 F6 91 F7 92 75 93 6B 94 C3 95 46 96 51 97 E6 98 8F 99 28 9A 76 9B 5A 9C 91 9D EC 9E 1F 9F 44 A0 52 A1 01 A2 FC A3 8B A4 3A A5 A1 A6 A3 A7 16 A8 10 A9 14 AA 50 AB CA AC 95 AD 92 AE 4B AF 35 B0 0E B1 B5 B2 20 B3 1D B4 5D B5 C1 B6 E2 B7 6E B8 0F B9 ED BA 90 BB D4 BC D9 BD 42 BE DD BF 98 C0 57 C1 37 C2 19 C3 78 C4 56 C5 AF C6 74 C7 D1 C8 04 C9 29 CA 55 CB E5 CC 4C CD A0 CE F2 CF 89 D0 DB D1 E4 D2 38 D3 83 D4 EA D5 17 D6 07 D7 DC D8 8C D9 8A DA B4 DB 7B DC E9 DD FF DE EB DF 15 E0 0D E1 02 E2 A2 E3 F3 E4 34 E5 CC E6 18 E7 F8 E8 13 E9 8D EA 7F EB AE EC 21 ED E3 EE CD EF 4D F0 70 F1 53 F2 FD F3 AB F4 72 F5 64 F6 1C F7 66 F8 A9 F9 B0 FA 1E FB D7 FC DF FD 36 FE 7D FF 31".split(" ")

#k = " ' | s euro ) \x11 t | |  + oooo | full full ( 0 \x1B q oooo s # e oooo | e \x11 \x11 + # oooo ' full # oooo \x05 e +".split(" ")[::-1]
k = "' | s ) \x11 t | | + | ( 0 \x1B q s # e | e \x11 \x11 + # ' # \x05 e +".split(" ")

#j = ['27', 'B3', '73', '9D','29', '11', '74', 'B3', 'B3', '2B','D6','B3',  '28', '30', '1B', '71','D6', '73', '23', '65', 'D6','B3', '65', '11', '11', '2B', '23','D6', '27', '23','D6', '5', '65', '2B']

j =  "27 B3 73 9D F5 11 E7 B1 B3 BE 99 B3 F9 F9 F4 30 1B 71 99 73 23 65 99 B1 65 F11 11 BE 23 99 27 F9 23 99 05 65 CE".split(" ")
print len(j)

'''for i in k: 
	print k.index(i)
	j.append(hex(ord(i))[2:].upper())
print j'''

#print(l)
#ans = raw_input()
tmp = ""
flag = ""

for a in range(len(j)):
	print(a)
	for b in range(len(l)):
		if(j[a]==l[b] and (chr(int(l[b-1],16)) in string.printable)):
			print(j[a],l[b-1])
			print(chr(int(l[b-1],16))+"\n")
	print("______________________\n")
print("tobias ")

for i in range(len(l)):
	if(chr(int (l[i],16)) in string.ascii_lowercase+string.ascii_uppercase):
		tmp+=chr(int (l[i],16))
print len(tmp)
