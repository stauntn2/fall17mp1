import sys
from Crypto.Hash.SHA256 import SHA256Hash as hash 

def hamming_dist(a, b):
	total = 0
	temp = 0
	for i in range(len(a)):
		temp = ord(a[i]) ^ ord(b[i])
		while temp != 0:
			if temp % 2 == 1:
				total += 1
			temp >>=  1	
	return total

def sha_dist(a, b):
	hasher = hash()
	hasher.update(a)
	a_hash = hasher.digest()
	hasher = hash()
	hasher.update(b)
	b_hash = hasher.digest()
	return hamming_dist(a_hash, b_hash)

def main(in_1_file, in_2_file, out_file):
	in_1 = open(in_1_file)
	in_2 = open(in_2_file)
	o = open(out_file, 'w')
	distance = sha_dist(in_1.read().strip(), in_2.read().strip())
	o.write(hex(distance)[2:]) 	#writes result in hex
	in_1.close()
	in_2.close()
	o.close()
	

if __name__ == "__main__":
	from sys import argv
	if len(argv) == 4:
		main(argv[1], argv[2], argv[3])
	else:
		print("Exactly three arguments required")

