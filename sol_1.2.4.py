from math import floor
from math import fmod
from fractions import gcd
from Crypto.PublicKey import RSA
import pbp

def product(X):
	result = [X]
	while len(X) > 1:
		thisSet = []
		for i in range((len(X))/2):
			thisSet.append(X[i*2]*X[i*2+1])
		if(len(X)%2 == 1):
			thisSet.append(X[len(X)-1])
		X = thisSet
	return X[0]

def remainderUsingProductTree(N, tree):
	result = [N]
	for t in reversed(tree):
		current = []
		for i in range(len(t)):
			current.append(result[int(floor(i/2))] % t[i])
		result = current
	return result

def productTree(X):
	result = [X]
	while len(X) > 1:
		thisSet = []
		for i in range((len(X))/2):
			thisSet.append(X[i*2]*X[i*2+1])
		if(len(X)%2 == 1):
			thisSet.append(X[len(X)-1])
		X = thisSet
		result.append(X)
	return result

def remainders(n,X):
	tree = productTree(X)
	return remainderUsingProductTree(n, tree)

def batchgcd_simple(X):
	R = remainders(product(X), [n*n for n in X])
	if len(X) != len(R):
		print "incorrect lengths"
		return
	gcds = []
	for i in range(len(X)):
		gcds.append(gcd(R[i]/X[i], X[i]))
	return gcds

#credit for xgcd algorithm: http://anh.cs.luc.edu/331/notes/xgcd.pdf
def xgcd(a,b):#pass in order: e, phi
	prevx, x = 1,0
	prevy, y = 0,1
	while b:
		q = a/b
		x, prevx = prevx-q*x,x
		y, prevy = prevy-q*y, y
		a,b = b, a%b
	return a, prevx, prevy #returns d

if __name__ == "__main__":
	n_file = open("../../_shared/mp1/moduli.hex")
	n = n_file.read().split("\n")
	n = n[:len(n)-1]
	for i in range(len(n)):
		n[i] = int(n[i],16)
	
	gcds = batchgcd_simple(n)

	phi = []
	new_n = []
	for i in range(len(gcds)):
		if gcds[i] != 1:
			new_n.append(n[i])
			phi.append((gcds[i]-1)*((n[i]/gcds[i])-1))
	d = []

	for i in range(len(phi)):
		g,x,y = xgcd(long(65537), phi[i])
		x = x % phi[i] 
		if(g != 1):
			print "error"
		else:
			d.append(x)
	
	encrypted_file = open("1.2.4_ciphertext.enc.asc")
	msg = encrypted_file.read()
	out_file = open("sol_1.2.4.txt", 'w')

	for i in range(len(d)):
		RSAkey = RSA.construct((new_n[i],long(65537),d[i]))
		try:
			result = pbp.decrypt(RSAkey, msg)
			out_file.write(result)
		except:
			print "key " + str(i) + " is not correct"
				
	out_file.close()
	encrypted_file.close()















