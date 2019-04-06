import time, sys, os
from Crypto.Cipher import AES, DES3
from Crypto import Random

# To do: Other file sizes, multiple key sizes, output data points

# declare setup variables

key = os.urandom(16)
keyMed = os.urandom(24)
keyBig = os.urandom(32)

def openFile():
	try:
	    data = open(sys.argv[1], 'rb')
	except IOError:
	    sys.exit("Could not open the input file")
	textStuff = data.read()
	data.close()
	return textStuff

def AESTest(key, textStuff):
	outFileAES = "encrypted-AES"
	iv = os.urandom(16)
	e_cipher = AES.new(key, AES.MODE_CFB, iv)
	d_cipher = AES.new(key, AES.MODE_CFB, iv)
	try:
	    encAES = open(outFileAES, 'wb')
	except IOError:
	    sys.exit("Could not create the output file")

	startTime = time.time() # start timer
	msg = e_cipher.encrypt(textStuff) # AES encryption
	encTime = time.time() - startTime # time to encrypt/end timer

	encAES.write(msg) # write encrypted message to file

	try:
	    encAES = open(outFileAES, 'rb')
	except IOError:
	    sys.exit("Could not create the output file")

	encData = encAES.read()
	startTimeEnc = time.time() # start timer
	decrypAES = d_cipher.decrypt(encData) # AES decryption
	decTime = time.time() - startTimeEnc # end timer

	totTime = encTime + decTime

	plainSize = os.stat(sys.argv[1])
	encSize = os.stat(outFileAES)
	encAES.close()
	print ("AES using key size of " + str(len(key)) + " bytes")
	print ("AES time to encrypt: " + str(round(encTime*1000, 4)) + " milliseconds")
	print ("AES time to dencrypt: " + str(round(decTime*1000, 4)) + " milliseconds")
	print ("AES total time: " + str(round(totTime*1000, 4)) + " milliseconds")
	print ("Original size: " + str(plainSize.st_size) + ", encrypted size: " + str(encSize.st_size))
	print
	return


def DES3Test(key, textStuff):
	outFileDES3 = "encrypted-DES3"
	ivD = Random.new().read(DES3.block_size)
	e_cipherD = DES3.new(key, DES3.MODE_CFB, ivD)
	d_cipherD = DES3.new(key, DES3.MODE_CFB, ivD)

	startTimeD = time.time() # start timer
	msgD = e_cipherD.encrypt(textStuff) # DES3 encryption
	encTimeD = time.time() - startTimeD # end timer

	try:
	    encDES3 = open(outFileDES3, 'wb')
	except IOError:
	    sys.exit("Could not create the output file")

	encDES3.write(msgD) # write encrypted message to file

	try:
	    encDES3 = open(outFileDES3, 'rb')
	except IOError:
	    sys.exit("Could not create the output file")

	encDataD = encDES3.read() # read encrypted file 

	startTimeDecD = time.time() # start timer
	decrypDES3 = d_cipherD.decrypt(encDataD) # DES3 decryption
	decTimeD = time.time() - startTimeDecD # end timer

	totTimeD = encTimeD + decTimeD
	
	plainSize = os.stat(sys.argv[1])
	encSizeD = os.stat(outFileDES3) 
	
	encDES3.close()
	print ("DES3 using key size of " + str(len(key)) + " bytes")
	print ("DES3 time to encrypt: " + str(round(encTimeD*1000, 4)) + " milliseconds")
	print ("DES3 time to dencrypt: " + str(round(decTimeD*1000, 4)) + " milliseconds")
	print ("DES3 total time: " + str(round(totTimeD*1000, 4)) + " milliseconds")
	print ("Original size: " + str(plainSize.st_size) + ", encrypted size: " + str(encSizeD.st_size))
	print
	return


AESTest(key, openFile())
AESTest(keyMed, openFile())
AESTest(keyBig, openFile())
DES3Test(key, openFile())






