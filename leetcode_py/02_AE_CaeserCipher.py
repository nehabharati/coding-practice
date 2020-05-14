def caesarCipherEncryptor(string, key):
    newLetter = []
	newKey = key % 26
	for letter in string:
		newLetter.append(getKey(letter,newKey))
	return "".join(newLetter)

def getKey(letter,key):
	nlc = ord(letter) + key
	return chr(nlc) if nlc <= 122 else chr(96 + nlc % 122)
