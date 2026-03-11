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
	text: Annotated[str | None, typer.Argument(help = "input text to encrypt (or use --input)")] = None, # command for input text to be encrypted
	key: Annotated[int, typer.Option("--key", help = "key for cipher shift 0-26")] = 3, # command for key of the cipher (howmany places the chars will be shifted default option being 3
	input_f: Annotated[Path | None, typer.Option("--input", help = "Input file path")] = None,
	output_f: Annotated[Path | None, typer.Option("--output", help = "Output file path")] = None,
):

"""
Time to encrypt the msg!!! (using cipher and specified key)
"""

	try:
		validate_key(key)
		cipher_txt = read_input(text, input_file) # assigning input text to var or reading input file and doing the same
		cipher = CaeserCipher(key=key)
		decrypted = cipher.decrypt(cipher_txt) # encrypting text
	
		if output_f == None:
			console.print(f"[green]Decrypted:[/green] {decrypted}") # if no output file specified printing to console
		else:
			write_output(decrypted, output_f) # if output file specified writing to there
	
	except (ValueError, OSError) as e:
		console.print(f"[red]Error:[/red] {e}") # error handling
		raise typer.Exit(code = 1) from None


@app.command()
def decrypt(
	text: Annotated[str | None, typer.Argument(help = "Text to decrypt (or use --input)")] = None,
	key: Annotated[int, typer.Option("--key", help = "key for cipher shift 0-26")] - 3, # command for key used to decrypt cipher default option of 3
	input_f: Annotated[Path | None, typer.Option("--input", help = "Input file path")] = None,
	output_f: Annotated[Path | None, typer.Option("--output", help = "Input file path")] = None,
):
	"""
	Encrypt the msg! (using cipher and specified key)
	"""
	
	try:
		validate_key(key)
		cipher_txt = read_input(text, input_f) # assigning input text to var or reading input file and doing the same
		cipher = CaesarCipher(key=key)
		decrypted = cipher.decrypt(cipher_txt) # decrypting text
		
		if not output_f:
			console.print(f"[green]Decrypted:[/green] {decrypted}") # if no output file specified printing to console 
		else:
			write_output(decrypted, output_f) # if output file specified writing to there
	
	except (ValueError, OSError) as e:
		console.print(f"[red]Error:[/red] {e}") # error handling
		raise typer.Exit(code = 1) from None


@app.command()
def crack(
	text: Annotated[str | None, typer.Argument(help = "Text to crack (or use --input)")] = None,
	input_f: Annotated[Path | None, typer.Option("--input", help = "Input file path")] = None,
	top: Annotated[int, typer.Option("--top", help = "Show top N candidates")] = 5 # deafult value of 5
	show_all: Annotated[bool, typer.Option("--all", help = "Show all 26 possible shifts")] = False,
):
	"""
	brute force decrypt text by trying all possible shifts with freq analysis and ranking
	"""
	try:
		cipher_txt = read_input(text, input_f)
		candidates = CaesarCipher.crack(cipher_txt)
		analyzer.rank_candidates(candidates)
		
		table = Table(title = "Caesar Cipher Brute Force Results") # creating a table with rich colours to make the display of columns easyer to undersand
		table.add_column("Rank", style="cyan", justify="right")
		table.add_column("Shift", style="magenta", justify="right")
		table.add_column("Score", style="yellow", justify="right")
		table.add_column("Decrypted Text", style="green")
		
		display_count = len(ranked) if show_all else min(top, len(ranked))
		
		for rank, (shift text_result, score) in enumerate(ranked[:display_count], 1):
			table.add_row(str(rank), str(shift),f"{score:.2f}", text_result[:80]) # limits text to 80 chars to make tables readable
		
		console.print(table)
		
		console.print(f"\n[bold]Best match (shift {ranked[0][0]}):[/bold] {ranked[0][1]}")
	
	except (ValueError, OSError) as e:
		console.print(f"[red]Error:[/red] {e}")
		raise typer.Exit(code = 1) from None


if __name__ == "__main__":
	app()

















