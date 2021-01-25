import sys
import scandir
from pathlib import Path as libPath


# Note:
	# I'm using "scandir" here since it's faster than using "os".
	# You may need to "pip install scandir" though, depending on your python version.
	# Or just replace "scandir" with "os" everywhere (it does the same exact thing) if you can't get scandir to install.

# TODO:
	# Add a quit option.
	# Make it ask for a new path after it's done.


def ask_for_and_validate_path():
	while True:
		filePath = input("Enter path to traverse: ").strip()	# Relative to where this script is located
		if filePath:
			if libPath(filePath).is_dir():
				return filePath
			else:
				print(f'Error; Could not find path: "{filePath}". Try again!')


def ask_for_a_string():
	while True:
		stringToLookFor = input("String to look for?: ").strip()
		if stringToLookFor:
			return stringToLookFor


def printing_function(lineContainingPhrase, path_to_file):
	seperator = "=" * 40
	print(f"\n{seperator}")
	print("Found:\n")
	print(f"{lineContainingPhrase}")
	print("In file:\n")
	print(path_to_file)


def look_for_string(pathToTraverse, string):
	for root, _, files in scandir.walk(pathToTraverse):
		for _file in files:
			if _file.endswith(".txt"):
				pathToFile = libPath(root).resolve() / _file
				# "encoding='utf-8'" and "errors='ignore'" are used here to avoid UnicodeDecodeError when finding a byte instead of text and to ignore errors.
				with open(pathToFile, 'r', encoding='utf-8', errors='ignore') as f:
					for line in f:
						if string in line:
							printing_function(line, pathToFile)


targetPath = ask_for_and_validate_path()
targetString = ask_for_a_string()

look_for_string(targetPath, targetString)



