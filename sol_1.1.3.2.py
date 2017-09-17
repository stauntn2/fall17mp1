import sys
from Crypto.Random import random 

def wha(inStr):
        mask = 0x3fffffff
        outHash = 0
	for raw_byte in inStr:
		byte = ord(raw_byte)
		temp = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
		outHash = (outHash & mask) + (temp & mask)
	return outHash 

def brake_hash(inStr):
	goal = wha(inStr)
	my_guess = ""
	cur_char = 'a' 
	while wha(my_guess) != goal:
		cur_char = chr(ord(cur_char) + 1)
		if wha(my_guess + cur_char) == goal:
			my_guess += cur_char
			brake
		if cur_char == 'z':
			my_guess += cur_char
			cur_char = 'a'
	return my_guess
		

def main(inFile, outFile):
	input_f = open(inFile)
	out_f = open(outFile, 'w')
	
	inStr = input_f.read().strip()
	outHash = wha(inStr)
	#print(brake_hash(inStr))
	out_f.write(hex(outHash)[2:])
	
	input_f.close()
	out_f.close()

if __name__ == "__main__":
	from sys import argv
	if len(argv) == 3:
		main(argv[1], argv[2])
	else:
		print("Need exactly two arguments")
