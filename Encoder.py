#!/usr/bin/python3
from Crypto.Util.number import *

plaintext = input("Enter the plaintext: ") #Plaintext that you want to encode
pt = plaintext.encode("utf-8").hex() #converting plaintext to hex
pt = int(pt, 16) #converting it to 16 bytes integer
p = getPrime(1024) #random prime number 'p'
q = getPrime(1024) #random prime number 'q'
n = p*q #n = p*q
e = input("Enter the public key (e) : (press enter for default key) ") #public key
if e == "":
    e = 65537
else:
    e = int(e)
phin = (p-1)*(q-1) # phin value
ciphertext = pow(pt, e, n) #ciphertext = pt^e mod n

#Adding data to file
data = open("Data.txt","w")
data.write("Plaintext: "+plaintext)
data.write("\n\n#Encrypted Data#\n")
data.write("\np: "+str(p))
data.write("\nq: "+str(q))
data.write("\ne: "+str(e))
data.write("\nCiphertext: "+str(ciphertext))
data.close()

#printing Encrypted data
print("Plaintext: ", plaintext) #printing plaintext
print("\np: ", p) #printing p
print("\nq: ", q) #printing q
print("\ne: ", e) #printing e 
print("\nCiphertext: ", ciphertext) #printing ciphertext