import urllib2

	# how to call: getURLContent("http://192.17.90.133:9999/mp1/tjorr2/?" + hex_cipher_text_attempt, True)
	
def getURLContent(url, debug = False):
	req = urllib2.Request(url)
	try:
		f = urllib2.urlopen(req)
		if debug:
			print f.read(), f.code
		return True
	except urllib2.HTTPError, e:
		if debug:
			print e.read(), e.code
		if e.code == 404:
			return True	#correct Padding
		return False #incorrect Padding

if __name__ == "__main__":
	ct_file = open("1.2.3_ciphertext.hex")
	ct = ct_file.read().strip()
	#ct = ct_pre.decode('hex')
	result = ""
	IV = ct[:32]
	ct = ct[32:]
	previous = int(IV,16)
	
	for i in range(len(ct)/32): #method of accessing each segment: ct[i*32:i*32+32]
		test = 0
		increment = 1
		padding = 0x10
		current = 0x10
		for j in range(15,-1,-1): #finds the correct byte for each byte
			
			if hex(previous ^ test ^ padding)[len(hex(previous ^ test ^ padding))-1:] == "L":
				attempt = "0" * (32-len(hex(previous ^ test ^ padding)[2:len(hex(previous ^ test^padding))-1])) + hex(previous ^ test ^ padding)[2:len(hex(previous ^ test^padding))-1] + ct[i*32:i*32+32]
			else:
				attempt = "0" * (32-len(hex(previous ^ test ^ padding)[2:])) + hex(previous ^ test ^ padding)[2:] + ct[i*32:i*32+32]
			while getURLContent("http://192.17.90.133:9999/mp1/tjorr2/?" + attempt, True) == False:
				test = test + increment
				if hex(previous ^ test ^ padding)[len(hex(previous ^ test ^ padding))-1:] == "L":
					attempt = "0" * (32-len(hex(previous ^ test ^ padding)[2:len(hex(previous ^ test^padding))-1])) + hex(previous ^ test ^ padding)[2:len(hex(previous ^ test^padding))-1] + ct[i*32:i*32+32]
				else:
					attempt = "0" * (32-len(hex(previous ^ test ^ padding)[2:])) + hex(previous ^ test ^ padding)[2:] + ct[i*32:i*32+32]
				print attempt, len(attempt)
				print hex(previous), len(hex(previous))
				print hex(test), len(hex(test))
				print hex(padding), len(hex(padding))
			increment = increment << 8
			current = current - 1
			padding = (padding << 8) + current
		print hex(test), len(hex(test))
		print hex(padding>>8), len(hex(padding>>8))
		print hex(test ^ (padding>>8)), len(hex(test^(padding>>8)))
		#dummy = raw_input()
		result = result + hex(test)[2:len(hex(test))-1]
		previous = int(ct[i*32:i*32+32],16)
	print result
	print result.decode('hex')


