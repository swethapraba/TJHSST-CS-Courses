#from cryptomath import *
#import Cryptoalphabet as ca 
#alpha = ca.Cryptoalphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def affine_encode(plaintext, a, b):
	process = ""
	cipherFinal = ""
	modulusValue = len(alphabet)
	#removes punctuation from plaintext
	for s in plaintext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			process+=s
	#converts to uppercase
	process = process.upper() 
	# converts each character using	y=ax+b(mod 26)
	for letter in process:
		ind = alphabet.index(letter)
		step1 = ind * a
		step2 = step1 + b
		step3 = step2 % modulusValue
		char = alphabet[step3]
		cipherFinal+= char
	# returns the ciphertext string
	return cipherFinal
def affine_decode(ciphertext, c, d):
	stringproc = ""
	plainFinal = ""
	modulusVal = len(alphabet)
	#return plainFinal
	# strip	punctuation	from ciphertext###
	#convert to	uppercase###
	for s in ciphertext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			stringproc+=s
	stringproc = stringproc.upper()
	# converts each character using	x=cy+d (mod	26)
	for letters in stringproc:
		index = alphabet.index(letters)
		stepone = index * c
		steptwo = stepone + d
		stepthr = steptwo % modulusVal
		chars = alphabet[stepthr]
		plainFinal += chars
	# note the (c,d) pair are the inverse coefficients of
	#the(a,b) pair used to encode
	# returns the plaintext	string
	return plainFinal
def affine_crack(c1, p1, c2, p2):
	return c2
	#o c1,p1,c2,p2	are	characters	
	# c1	is	the	encoded	char	of	p1
	# c2	is	the	encoded	char	of	p2
	# returns	a	pair	(c,d)	to	use	in	affine_decode
	# solves	a	linear	system
	# result:	p1	=	c	*	c1	+	d2	and	p2	=	c	*	c2	+	d2	(mod	26)
	# returns	the	pair	(c,	d)	or	None	if	no	solution	can	be	found
def mod_inverse(a,m):
	x = 1
	for i in range(0,m-1):
		if (a*i) % m == 1:
			x = i
			break
	return x  
#problemset1
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#test the encode function:
decrypted1 = "I KNOW' WHO.!?, PUT THE PUMPKIN ON THE CLOCK TOIQD"
cd1 = 21
dd1 = 8
print(affine_encode(decrypted1, cd1, dd1))

#decryptions:
encrypted1 = "UKVQCCZQLMRRZOLMALKUVQVRZOYFQYKRQUGT"
c1 = 5
d1 = -14
print(affine_decode(encrypted1, c1, d1))
encrypted2 = "lqpfzfaifstqufqqjjtakfnvfqnjisvkk"
c2 = -3
d2 = 15
print(affine_decode(encrypted2, c2, d2))
encrypted3 = "qgxetvepjyleexlkxujyxlksfbrqboxk"
c3 = 9
d3 = -21
print(affine_decode(encrypted3, c3, d3))
encrypted4 = "cpvvkmtsbkmtkgqlcbsepsbueqlvzcll"
c4 = 7
d4 = -14
print(affine_decode(encrypted4, c4, d4))
encrypted5 = "axhugoabuzabrloeusbxalxfubudxorhag"
c5 = 5
d5 = -18
print(affine_decode(encrypted5, c5, d5))
encrypted6 = "lqqlshykibymgsnfskvqlkmdmbmpoxqfma"
c6 = 21
d6 = -10
print(affine_decode(encrypted6, c6, d6))
encrypted7 = "mxfpyxmxyfyyxqykliimxeymfpkrryxyb" #the one letter crib
c7 = 17 #?????
d7 = -14 #????
print(affine_decode(encrypted7, c7, d7))

#test practice
print("TEST PRACTICE")
newalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptMeString = "TABLE"
theAValue = 15
theBValue = 11
print(affine_encode(encryptMeString,theAValue,theBValue)) #encoded to KLAUT
print()
newalpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decryptMeString = "XMRPQ"
theAValueE = 3
theBValueE = -9
#find C Value
theCValue = 0
#find D value
theDValue = 0
#use those in the method
print(affine_decode(decryptMeString,theCValue,theDValue))

#avals
# for a in range(1,26):
# 	#bvals
# 	for b in range(-26,1):
# 		string = affine_decode(encrypted7,a,b)
# 		print("A: ", a,"B: ", b, "String: " ,string)
#examples
#i = alpha.getIndex("H")
#c = alpha.charNum(i)
#d = alpha.charNum(100)
#print i + c + d
#print(gcd(124,296))
#print(lcm(148,2560))
#print(mod_inverse(13,142))
#print(mod_inverse(8,17)) #test modulus
