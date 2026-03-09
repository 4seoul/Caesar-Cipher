import string
from typing import Final

# Creating lists of all uppercase and lowercase letters

UPPERCASE_LETTERS: Final[str] = string.ascii_uppercase
LOWERCASE_LETTERS: Final[str] = string.ascii_lowercase

ALL_LETTERS: Final[str] = UPPERCASE_LETTERS + LOWERCASE_LETTERS

ALPHABET_SIZE: Final[int] = 26

# var_name: Expected type of variable = variable assignment