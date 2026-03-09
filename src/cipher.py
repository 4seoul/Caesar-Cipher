


from constants import (
    ALPHABET_SIZE,
    LOWERCASE_LETTERS,
    UPPERCASE_LETTERS,
)



class CaesarCipher:
	
	def __init__(self, key: int, alphabet: str | None = None): # expect alphabet to be str or None, if None set value to None
		if not -25 <= key <= 26:
			raise ValueError("Key must be between -25 and 26")
			

		self.key = key
		self.alphabet = alphabet or (UPPERCASE_LETTERS + LOWERCASE_LETTERS) # init alphabet, use custom alphabet or use default
		
		if alphabet and len(set(alphabet)) != len(alphabet): # checking for duplicate chars in alphabet variable
			raise ValueError("Alphabet must not contain duplicate chars")
			
		
		
	def shift_chars(self, char: str, shift: int):
		if char in UPPERCASE_LETTERS:
			pos = UPPERCASE_LETTERS.index(char) # get position of char in list
			return UPPERCASE_LETTERS(pos + shift) # return shifted char by adding the shift to the index of current char
		
		if char in LOWERCASE_LETTERS:
			pos = LOWERCASE_LETTERS.index(char)
			return LOWERCASE_LETTERS(pos + shift) # same as above
		
		return char
	
	def encrypt(self, text: str):
		"""
		encrypting word looping through each char in the word and shifting them forward using shift_chars()
		"""
		
		encrypted_word = ""
		for char in text:
			encrypted_word += self.shift_chars(char, self.key)
		return encrypted_word

	
	def decrypt(self, text: str):
		"""
		decrypting cypher text by looping through each char and shifting backwards using shift_chars()
		"""
		
		decrypted_word = ""
		for char in text:
			decrypted_word += self.shift_chars(char, -self.key)
		return decrypted_word
		
		# Note: Make both functions more efficient later im jus lazy rn fr
	
	@staticmethod # dosent operate on one instance, creates all possible instances to be compared to eachother
	def crack(text: str):
		"""
		creates instances of all possible solutions for frequency analysis 
		"""
		results = []
		for i in range(ALPHABET_SIZE): # recur for all letters, i will be all possible shift values
			cipher = CaesarCipher(key=i) # creates class instance where key = i
			decrypted_text = cipher.decrypt(text) # decrypts the text with the key as i
			results.append((i, decrypted_text)) # double brackets to create a tupple










