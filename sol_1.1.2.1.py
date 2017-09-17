import sys


def reverse_cipher(c_file, k_file, out):
	with open(c_file) as c:
		k = open(k_file)
		o = open(out, 'w')	

		inverse = ['0' for i in range(26)] 		#initializing our array
		cipher = c.read().strip()
		key = k.read().strip()
		
		for i in range(26):
			inverse[ord(key[i]) - ord('A')] = chr(i + ord('A'))
	
		result = ""
		for i in cipher:
			if ord(i) >= 65 and ord(i) <= 90:
				result += inverse[ord(i) - ord('A')]
			else:
				result += i

		o.write(result)
		k.close()
		o.close()


if __name__ == "__main__":
	from sys import argv
	if len(argv) ==  4:
		reverse_cipher(argv[1], argv[2], argv[3])
	else:
		print("Needs exactly three arguments")
