# check for instantaneous decodability
# code can be binary or otherwise
from sys import argv
script, filename = argv
with open(filename) as code:
    data = code.readlines()
clean=[line.split(' ', 2)[1] for line in data]
clean=[line.split('\n', 2)[0] for line in clean]
print(clean)
answer = 1 # prefix doesn't exist
length = len(clean)
for i in range(length):
	for j in range(length):
		if clean[j].startswith(clean[i]):
			if(i!=j):
				answer = 0 #prefix exists

if answer:
	print("Code is instantaneously decodable")
else:
	print("Code is not instantaneously decodable")