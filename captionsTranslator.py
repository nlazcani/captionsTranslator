# -*- coding: utf-8 -*-

# Jesus if you are reading this. Forgive me for this piece of garbage. I failed you :(
# Also thanks to the people at Hacklab Kika and one guy on stackoverflow that helped me fix it.

import argparse
import srt
import pydeepl
import os
import shutil
import sys
import time
from datetime import datetime

# Now this is where all the fun begins

def translate(input, output, languagef, languaget):
	file = open(input, 'r').read()
	fileresp = open(output, 'w') # Use w mode instead
	subs = list(srt.parse(file))
	for sub in subs:
		try:
			linefromsub = sub.content
			translationSentence = pydeepl.translate(linefromsub, languaget.upper(), languagef.upper())
			print(str(sub.index) + ' ' + translationSentence)
			fileresp.write("{}\n{} --> {}\n{}\n\n".format(sub.index,str(sub.start)[:-3], str(sub.end)[:-3], translationSentence))
		except IndexError:
			print("Error parsing data from deepl")


def parsefiles(inputFile, outputFile, languageFrom, languageTo):
	if inputFile == None:
		print("Input file not specified! Exiting...")
		sys.exit(2)
	if languageTo == None:
		print("Language not specified! Exiting...")
		sys.exit(2)

	if outputFile == None:
		outputFile = inputFile + languageTo + '.srt'

	shutil.copyfile(inputFile, outputFile)
	# Due to a bug that files cannot be accessed I had to move everything to another function
	translate(inputFile, outputFile, languageFrom, languageTo)


def main():
	# Parse Arguments
	parser = argparse.ArgumentParser(description='Python Program that translates a subtitle file using deepl')
	parser.add_argument('-i', '--input-file', action="store", help="takes the input file", metavar="FILE")
	parser.add_argument('-o', '--output-file', action="store", help="takes the output file", metavar="FILE")
	parser.add_argument('-lf', '--language-from', action="store", help="language to translate from", default="auto")
	parser.add_argument('-lt', '--language-to', action="store", help="language to translate to")
	args = parser.parse_args()
	parsefiles(args.input_file, args.output_file, args.language_from, args.language_to)


main()
