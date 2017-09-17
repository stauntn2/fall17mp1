from Crypto.PublicKey import RSA


def decrypt_RSA(ct_name, key_name, mod_name, out_name):
	ct_file = open(ct_name)
	key_file = open(key_name)
	mod_file = open(mod_name)
	out_file = open(out_name, 'w')

	ct = ct_file.read().strip()
	key = key_file.read().strip()
	mod = mod_file.read().strip()
	
	ct = int(ct,16)
	key = int(key,16)
	mod = int(mod,16)
	
	remainder = pow(ct,key,mod)
	rtype = type(remainder)
	result = hex(remainder)
	if rtype == 'int':
		out_file.write(result[2:])
	else:
		out_file.write(result[2:len(result)-1])
	out_file.close()
	ct_file.close()
	key_file.close()
	mod_file.close()

from sys import argv
if len(argv) ==  5:
	decrypt_RSA(argv[1], argv[2], argv[3], argv[4])
else:
	print("Needs exactly four arguments")
