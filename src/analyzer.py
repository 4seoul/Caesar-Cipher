from collections import Counter
from constants import ENGLISH_LETTER_FREQUENCIES


class FrequencyAnalyzer:
	"""
	Analyzes text for language patters using letter frequency
	"""
	def __init__(self):
		"""
		init analyzer with frequency data
		"""
		self.reference_frequencies = ENGLISH_LETTER_FREQUENCIES
		
	
	def calculate_chi_squared(self, text: str): # some weird math that took me too long to make sense of
		"""
		calc chi-squared statistic comparing the text to expected frequencies
		"""
		text_upper = text.upper()
		letter_counts = Counter(char for char in text_upper if char.isalpha()) # convert text to caps then counts only letters
		
		if not letter_counts: # cant score empty text
			return float("inf")
		
		total_letters = sum(letter_counts.values()) # total letter count
		chi_squared = 0.0
		
		for letter, expected_freq in self.reference_frequencies.items(): # for ever letter (a-z) compare observed letter count with expected letter count 
			observed_count = letter_counts.get(letter, 0) # number of times a letter appears in input text
			expected_count = (expected_freq / 100) * total_letters # expected times letter appears in input text
			
			if expected_count > 0:
				chi_squared += ((observed_count - expected_count)**2) / expected_count # adds up squred differences and is normalised by expected_count (expected values)
			
		return chi_squared
	
	def score_text(self, text: str):
		"""
		score for being potentially valid english (lowerscore = better)
		"""
		return self.calculate_chi_squared(text)
	
	def rank_candidates(self, candidates: list[tuple[int, str]])
		"""
		rank decryption candidates by score
		"""
		scored = [(shift, text, self.score_text(text)) for shift, text in candidates] # makes list of all potential decrypted texts and ranks them by score from best to worst
		return sorted(scored, key = lambda x: x[2])