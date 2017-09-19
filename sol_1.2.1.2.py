import sys
import pymd5 as m
import urllib as url

"""
Grabs the state from the query String
"""
def grab_state(orig_query):
	hash_string = orig_query[6:38]	# String will always start the same way
	return hash_string

def build_query(new_hash, orig_query, command):
	result = "token="
	result = result + new_hash + orig_query[38:] + url.quote(m.padding(len(orig_query) * 8)) + command
	return result

def main(query_file, command3_file, output_file):
	q = open(query_file)
	c = open(command3_file)
	out = open(output_file, "w")

	query = q.read().strip()
	command = c.read().strip()

	hash_string = grab_state(query)
	h = m.md5(state = hash_string.decode("hex"), count = 512) # eight bits per char
	h.update(command)
	updated_hash = h.hexdigest()

	result = build_query(updated_hash, query, command)

	out.write(result)

	q.close()
	c.close()
	out.close()



if __name__ == "__main__":
	from sys import argv
	if len(argv) == 4:
		main(argv[1], argv[2], argv[3])
	else:
		print("Exactly three arguments required")

