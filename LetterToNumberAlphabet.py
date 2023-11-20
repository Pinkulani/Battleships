Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def LetterToNumber(Letter):
	for X in range(0, len(Alphabet)):
		if Letter == Alphabet[X]:
			return X

print(LetterToNumber("C"))