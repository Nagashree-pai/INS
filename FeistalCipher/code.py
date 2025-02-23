import numpy as np

s=input("enter a string:")
result="".join(format(ord(i),'08b')for i in s)
print("result: ",result)

l=int(len(result)/2)
left=result[:l]
right=result[l:]

k=input("enter a key: ")
key="".join(format(ord(i),'08b') for i in k)

s=bin(int(right,2)+int(key,2))
answer=bin(int(s[2:],2)^int(left,2))
newr=answer[2:]
newl=right
newr,newl=newl,newr

s=bin(int(newr,2)+int(key,2))
ans=bin(int(s[2:],2)^int(newl,2))

nl=newr
nr=ans[2:]
nl,nr=nr,nl
cipher=nl+nr

if(len(cipher)!=len(result)):
    while(len(cipher)!=len(result)):
        cipher="0"+cipher
print(cipher)
plaintext=""

for i in range(0,len(cipher),8):
    temp=cipher[i:i+8]
    d=int(temp,2)
    plaintext=plaintext+chr(d)
print("decrypted text:", plaintext)  