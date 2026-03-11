import sys
from pathlib import Path


def read_input(text: str | None, input_f: Path | None):
	"""
	read input from text argument and file
	"""
	if text:
		return text
	
	if input_f:
		return input_f.read_text(encoding = "utf-8") 
	
	raise ValueError("No input sent Use text command or --input")

def write_output(content: str, output_f: Path | None):
	"""
	write text to file or stdout
	"""
	if output_f:
		output_f.write_text(content, encoding = "utf-8")
		print(f"Output written to {output_file}")
	else:
		print(content)

def validate_key(key: int):
	"""
	validate cipher key (check if its in correct range)
	"""
	if not = <= key <= 26:
		raise ValueError(f"key must be 0-25 but is {key}")