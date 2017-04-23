import numpy as np
import time

# Create key based on timestamp
KEY = time.time()
np.random.seed(int(KEY))

# Read in message
with open('Message.txt', 'r') as f:
	Message = f.read()
	f.close()

# Generate vector of random integers
Encoder = np.random.random_integers(300, size=len(Message))

# Map message to encoded array
M = []
for i in range(len(Message)):
    M.append(ord(Message[i])*Encoder[i])

# Create or overwrite the file with the message
with open('ENCODED.txt', 'w') as e:
    for m in M:
        e.write(str(m)+" ")

# Create or overwrite the file with the key
with open('KEY.txt', 'w') as f:
    f.write(str(KEY))

print "Your message has been encoded!"