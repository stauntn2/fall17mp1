import sys
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.asymmetric import rsa
from Crypto.Util import number
import datetime
import hashlib
from pymd5 import md5, padding

limit1 = 2 ** 512
limit2 = limit1 **2

"""
After running phase1, run ./fastcoll -p pref1.2.5 -o col1 col2
"""
def phase1():
	in_1 = open("sol_1.2.5_certA.cer")
	prefix = open("pref1.2.5", "w")

	blocks = 1
	#length = 64*blocks # 512 bits -> bytes
	length = 256
	msg = in_1.read()[0:length]
	prefix.write(msg)
	prefix.close()

"""
Taken from discussion
"Chinese Remainder Theorem"
"""
def getCRT(b1, b2, p1, p2):
	N = p1 * p2
	invOne = number.inverse(p2, p1)
	invTwo = number.inverse(p1, p2)
	return -(b1 * invOne * p2 + b2 * invTwo * p1) % N

def coprime(x, e = 65537):
	result = False
	if(number.GCD(x,e) == e):
		result = True
	return result

def pq_maker(b_1, b_2):
	count = 0
	while True:
		print(count)
		p_1 = number.getPrime(500)
		p_2 = number.getPrime(500)
		print("a1")
		while not coprime(p_1-1):
			p_1 = number.getPrime(500)
		print("A")
		while not coprime(p_2-1):
			p_2 = number.getPrime(500)

		b_0 = getCRT(b_1, b_2, p_1, p_2)
		print("k")
		k = 0
		while k < limit2:
			b = b_0 + k*p_1*p_2
			q_1 = (b_1 * limit1 + b)/p_1
 			q_2 = (b_2 * limit1 + b)/p_2
 			if(number.isPrime(q_1) and number.isPrime(q_2) and coprime(q_1-1) and coprime(q_2-1)):
 				return q_1, q_2, p_1, p_2
 			k = k + 1
 			if (k %10000 == 0):
 				print(k)
 		count = count + 1





"""
Run phase2 after the ./fastcoll
"""
def phase2():
	col1 = open("col1")
	col2 = open("col2")
	out = open("output1.2.5.txt", "w")


	b_1 = col1.read()
	b_2 = col2.read()

	b_1 = b_1[256:]
	b_2 = b_2[256:]

	q_1, q_2, p_1, p_2 = pq_maker(b_1, b_2)

	print(q_1)
	print(q_2)
	print(p_1) 
	print(p_2)
	string = ""
	string += "p_1: " + hex(p_1)[2:] + "\n"
	string += "p_2: " + hex(p_2)[2:] + "\n"
	string += "q_1: " + hex(q_1)[2:] + "\n"
	string += "q_2: " + hex(q_2)[2:] + "\n"
	string += "n_1: " + hex(b_1*limit + b)[2:] + "\n"
	string += "n_2: " + hex(b_2*limit + b)[2:]

	print(string)

	out.write(string)


'''
	out = open("sol_1.2.5_certB.cer", "w")
	hex_1 = open("sol_1.2.5_factorsA.hex", "w")
	hex_2 = open("sol_1.2.5_factorsB.hex", "w")
'''
'''
	h = md5()
	h.update(msg)
	h.digest()

	certA = in_1.read()
'''

def main():
	#phase1()
	phase2()

if __name__ == "__main__":
	main()