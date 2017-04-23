import numpy as np
import time
import csv

with open('KEY.txt', 'r') as f:
	KEY_V = f.read()
	f.close()

M_to_Decode = list(csv.reader(open('ENCODED.txt', 'rb'), delimiter=' '))

# Decode
DECODED = []

np.random.seed(int(float(KEY_V)))

Decoder = np.random.random_integers(300, size=len(M_to_Decode[0]))

for i in range(len(M_to_Decode[0])-1):
	DECODED.append(chr(int(M_to_Decode[0][i])/Decoder[i]))

# Create or overwrite the file with the key
with open('DECODED.txt', 'w') as d:
    for q in DECODED:
        d.write(str(q))

d.close()

with open('DECODED.txt', 'r') as y:
	file_contents = y.read()
	print file_contents
	y.close()