from Crypto.Cipher import AES
import sys



def inverse_AES(cipher_file, key_file, iv_file, out):
	c = open(cipher_file)
	k = open(key_file)
	iv_file = open(iv_file)
	o = open(out, 'w')

	ciphertext = c.read().strip()
	key = k.read().strip()
	initial_value = iv_file.read().strip()
	
	iv = initial_value.decode('hex')
	key = key.decode('hex')
	ciphertext = ciphertext.decode('hex')
	
	cipher = AES.new(key, AES.MODE_CBC, iv)
	result = cipher.decrypt(ciphertext)
	o.write(result)
	o.close()
	c.close()
	k.close()
	iv_file.close()

if __name__ == "__main__":
    from sys import argv
    if len(argv) ==  5:
        inverse_AES(argv[1], argv[2], argv[3], argv[4])
    else:
        print("Needs exactly four arguments")


