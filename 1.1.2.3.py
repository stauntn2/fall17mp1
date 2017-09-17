from Crypto.Cipher import AES

ct_file = open("1.1.2.3_aes_weak_ciphertext.hex")
ct = ct_file.read().strip()
ct = ct.decode('hex')
iv = "0000000000000000"

start = "00000000000000000000000000000000000000000000000000000000000000"
for i in range(20):
	if i < 16:
		key = start + "0" + hex(i)[2:]
	else:
		key = start + hex(i)[2:]
	key = key.decode('hex')
	
	cipher = AES.new(key,AES.MODE_CBC, iv)
	print("trial " + str(i) + ":\n" + cipher.decrypt(ct))

	
