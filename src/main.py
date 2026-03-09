from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from analyzer import FrequencyAnalyzer # not implemented yet
from cipher import CaesarCipher
from utils import read_input, validate_key, write_output # not implemented yet


# Initialise the app
app = typer.Typer( 
	name = "Caesar-Cipher",
	help = "Caesar Cipher tool for encryption, decryption, and brute-force cracking",
	no_args_is_help = True,
)
console = Console()


@app.command()
def encrypt(
	text: Annotated[str | None, typer.Argument(...)] = None,
	key: Annotated[int, typer.Option("--key", "-k", ...)] = 3,
	input_file: 
	output_file:
	quiet: 
	# DO RESEARCH ON APP THING WRITE IT URSELF U BUM
