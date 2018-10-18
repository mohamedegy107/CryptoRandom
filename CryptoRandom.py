'''
CryptoRandom.Ecrypt()
	3 Arge:
		 1- String To Encryption
		 2- File To Encryption
	NOTE: If you Want Encryption File Will be frist arge = "" 
		EXM: CryptoRandom.Encrypt("",'File.pdf')

CryptoRandom.Decrypt()
	3 Arge:
		1- KEY
		2- Encrypted Data to Decryption
		3- File To Decryption
	NOTE: If you Want Decryption File Will be Second arge = "" 
	EXM: CryptoRandom.Encrypt(KEY,"",'File.pdf')

CryptoRandom.Key()
	No Arge
	This Function For Get Your Key 

CryptoRandom.Encrypted_data()
	No Arge
	This Function For Get Your Encrypted Data
	NOTE: Uesing If Your Data Type is (Text)

Crypto.Random.Decrypted_data()
	No Arge
	This Function For Get Your Decrypted Data	
	 NOTE: Uesing If Your Data Type is (Text)
'''
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import random
import base64

def Encrypt(Value='',FileName=''):

	_alpha = ['أ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','\n',
		  'u', 'v', 'w', 'x', 'y', 'z', 'ش', 'س', 'ب', 'ل', 'ت', 'ن', 'م', 'ك', 'ط', 'ئ', 'ء', 'ؤ', 'ر', 'ل','ا','ى',
	          'ة', 'و', 'ز','ظ', 'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح','ج', 'د', 'A', 'B', 'C', 'D', 'E', 'F','؛',
	          'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z', ' ', '`', '0',
	          '1','2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%','^', '&', '*', '(', ')', '-', '+', '\'',
	          '\\', '/', '.', '_', ':', ';', ',',"'", '>', '<', '[', ']', '{', '}', '|','إ']

	_rd = random.sample(_alpha,k=len(_alpha))

	global enct
	global FileXFN
	global tempkey
	tempkey = ''
	global _rand
	_rand = _rd

	inp = list(Value)
	try:
		if len(FileName) > 1:
			if ".txt" not in FileName:
				enct = ''
				file = open(FileName,'rb')
				filer = file.read()
				file.close()
				key = Random.new().read(256)
				iv = Random.new().read(256)
				tempkey = SHA.new(iv+key).digest()
				E = ARC4.new(tempkey)
				EMS = base64.b64encode(E.encrypt(filer))
				file1 = open(FileName,'wb')
				file1w = file1.write(EMS)
				file1.close()
			else:
				tempkey = ''
				Value = ''
				FileReadX = open(FileName,'r')
				FileXF = FileReadX.read()
				FileXFN = FileXF.replace(" ","`")
				FileReadX.close()
				Value = FileXF
				
				idxf = []
				for i_alpha in Value:
					idx = _alpha.index(str(i_alpha))
					idxf.append(str(idx))

				enct = ""
				for i_rand in idxf:
					edx = _rand[int(i_rand)]
					enct += edx
					
				FileWX = open(FileName,'w')
				FileWXF = FileWX.write(enct)
				FileWX.close()
				_rand = _rd
		else:
			idxf = []
			for i_alpha in inp:
				idx = _alpha.index(str(i_alpha))
				idxf.append(str(idx))
			
			enct = ""
			for i_rand in idxf:
				edx = _rand[int(i_rand)]
				enct += edx
			tempkey = ''
			_rand = _rd
	except Exception as Error:
	    _key = ''
	    for i_key in _rand:
	        _key += str(i_key)
	    print("Key: \n")
	    print(Error)
	    print(_key)

def Key():
	if len(tempkey) <= 0:
	    _key = ''
	    for i_key in _rand:
	        _key += str(i_key)
	    KND = _key.encode("utf-8")
	    KNB = base64.b64encode(KND) 
	    return KNB
	else:
		return base64.b64encode(tempkey)

def Encrypted_data():
    _enc = ''
    for i_key in enct:
        _enc += str(i_key)
    return _enc



global FileXFND
def Decrypt(Key,Value='',FileName=''):


	_alpha = ['أ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','\n',
	          'u', 'v', 'w', 'x', 'y', 'z', 'ش', 'س', 'ب', 'ل', 'ت', 'ن', 'م', 'ك', 'ط', 'ئ', 'ء', 'ؤ', 'ر', 'ل','ا','ى',
	          'ة', 'و', 'ز','ظ', 'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح','ج', 'د', 'A', 'B', 'C', 'D', 'E', 'F','؛',
	          'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z', ' ', '`', '0',
	          '1','2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%','^', '&', '*', '(', ')', '-', '+', '\'',
	          '\\', '/', '.', '_', ':', ';', ',',"'", '>', '<', '[', ']', '{', '}', '|','إ']

	global denct

	if len(FileName) > 1:
		if len(Key) <= len(_alpha):
			if FileName not in ".txt":
				denct = ""
				file = open(FileName,'rb')
				filer = file.read()
				file.close()
				KD = base64.b64decode(Key)
				D = ARC4.new(KD)
				Em = D.decrypt(base64.b64decode(filer))
				file2 = open(FileName,'wb')
				filew = file2.write(Em)
				file2.close()
		else:
			KeY = base64.b64decode(Key).decode("utf-8")
			_rand = list(KeY)
			inp = list(Value)
			denct = ""
			Value = ''
			FileReadX = open(FileName,'r')
			FileXF = FileReadX.read()
			FileReadX.close()
			Value = FileXF
			idxf = []
			for i_alpha in Value:
				idx = _rand.index(str(i_alpha))
				idxf.append(str(idx))
	
			enct = ""
			for i_rand in idxf:
				edx = _alpha[int(i_rand)]
				enct += edx

			FileXFN = enct.replace("`"," ")
			FileWX = open(FileName,'w')
			FileWXF = FileWX.write(FileXFN)
			FileXFN.close()
	else:
		KeY = base64.b64decode(Key).decode("utf-8")
		_rand = list(KeY)
		inp = list(Value)
		idxf = []
		for i_alpha in inp:
			idx = _rand.index(str(i_alpha))
			idxf.append(str(idx))

		denct = ""
		for i_rand in idxf:
			edx = _alpha[int(i_rand)]
			denct += edx

def Decrypted_data():
    _enc = ''
    for i_key in denct:
        _enc += str(i_key)
    return _enc
