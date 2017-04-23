# Dear Diary - Message Encryption

This code is meant to allow for sending an encrypted message with a timestamp-dependent key.

NOTE: This is my first approach to encryption, and I acknowledge there is a lot of work on the subject that I hope to learn from and improve the approach to code in this repository with.

Steps: 

1) Write your message in Message.txt

2) At your terminal, type `python Encoder.py`. This generates "ENCODED.txt" and "KEY.txt" files. The desired recipient should have both the key along with the encoded text file, as well as "Decoder.py"

3) The recipient should open a terminal with the files "ENCODED.txt", "KEY.txt", and "Decoder.py". The recipient must type at his or her terminal, `python Decoder.py`

4) The message will display on the terminal.