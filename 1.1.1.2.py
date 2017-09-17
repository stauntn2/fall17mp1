if __name__ == "__main__":
	with open("1.1.1.2_value.hex") as f:
		file_content = f.read().strip()
		bi_file = open("sol_1.1.1.2_binary.txt", "w")
		dec_file = open("sol_1.1.1.2_decimal.txt", "w")
		int_parse = int(file_content, 16)
		bi_str = bin(int_parse)[2:]
		dec_str = str(int_parse)
		bi_file.write(bi_str)
		dec_file.write(dec_str)
		bi_file.close()
		dec_file.close()
