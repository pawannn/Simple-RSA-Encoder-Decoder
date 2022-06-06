#!/usr/bin/python3
from Crypto.Util.number import *

ciphertext = int(input("Enter the ciphertext: ")) #ciphertext that you want to decode
p = int(input("Enter P : ")) 
q = int(input("Enter q : "))
e = int(input("Enter (e) : "))
n = p*q #n = p*q
phin = (p-1)*(q-1) # phin value 
d = inverse(e,phin) #private key
plaintext = pow(ciphertext,d,n) #plaintext = ciphertext^d mod n
print("\nPlaintext: ",long_to_bytes(plaintext)) #printing plaintext
print("\nYour Private key (d) : ",d) #printing private key