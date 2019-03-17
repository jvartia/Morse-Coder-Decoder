# -*- coding: utf-8 -*-
import os,sys;
import csv;
## Text / Morse converter 
## Made by Jaakko Vartiainen 03/2019



def ReadInputFile():
	#This function gets input file and conversion method from the user. 
	# Input file can be given as path or filename(if exists in same folder than main script)
	
	while True:
		InputFile = input("\nPlease give input file for decoder:");
		
		try:
			f = open(InputFile, "r");
			content = f.readlines();
			break;
			
		except:
			print("\nDecoder was not able to find your file - Please check given filepath");
			

	print("\nConversion methods are: 1)Text to Morse  2)Morse to Text ");
	method = "";
	while (method != "1" or method != "2"):
	
		method = input("Select conversion method: ");
		if (method == "1" or method == "2"):
			break;
		else:
			print("Conversion method should be given as a number 1 or 2\n");
			
	#Function returns input file content and conversion method
	return content,method;

def CryptMorse(InputFile, Dictionary):
	#This function Converts normal characters into Morse code. .
	#Text is automatically uppercased for dictionary.
	#Text can not include special characters or two dots in a row.
	output = [];
	
	for file in InputFile:
		i = 0;
		translation = "";
		file = file.replace(" ","");
		for letter in file.rstrip():
			if (letter != "."):
				i = 0;
				try:
					translation += Dictionary[letter.upper()];
					translation += " ";
				except:
					sys.exit("\nDetected invalid Character - CRYPTING TERMINATED");
			else:
				i = i+1;
				if (i > 1):
					sys.exit("\nInput file contains to dots in a row!");
		translation = translation.rstrip();
		output.append(translation);
		
	#funtion returns list of morse-coded elements.
	return output;
	
def EncryptMorse(InputFile,Dictionary):
	#This function converts morse code to readable text format.
	#Conversion terminates if morse data contains two separators in a row or invalid characters.
	output = [];

	
	for file in InputFile:
		translation = "";
		j = 0;
		CharacterList = file.split(" ");
		for item in CharacterList:
			item = item.rstrip();
		
			if (item ==" "):
				j = j+1;
				translation += " ";
			else:
				if (j<2):
					try:
						translation += list(Dictionary.keys())[list(Dictionary.values()).index(item)];
						j = 0;
					except:
						sys.exit("Detected innvalid morse characters. CONVERSION TERMINATED");
				else:
					sys.exit("Detected two separators in a row - CONVERSION TERMINATED");
		
		output.append(translation);
	
	#Function returns list of text charaters
	return output;
	
def WriteToFile(message):

	#This function defines file location for converted message.
	
	OutputFile = input("\nPlease give output file destination:");
	try:
		mode = 'a' if os.path.exists(OutputFile) else 'w'
		with open(OutputFile, mode) as f:
			f.write("\n".join(message));
			print("Converted message saved to:",OutputFile);
	except:
		sys.exit("File could not be saved to system");
		
def main():
	#Main function is activated when program starts.
	#Contains dictionary for morse coding / encoding.
	#Contains sub-function calls.
	
	MORSE_DICTIONARY = {
	'A':'.-', 'B':'-...', 'C':'-.-.',
	'D':'-..','E':'.', 'F':'..-.', 'G':'--.', 
	'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
	'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...',
	'T':'-','U':'..-', 'V':'...-','W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..', '.':'.-.-.-',
	',':'--..--', '?':'..--..','/':'-..-.', '1':'.----',
	'2':'..---', '3':'...--', '4':'....-', '5':'.....',
	'6':'-....', '7':'--...', '8':'---..', '9':'----.',
	'0':'-----' };
	
	InputFileContent,Method = ReadInputFile();
	
	if (Method == "1"):
		message = CryptMorse(InputFileContent, MORSE_DICTIONARY)
	else:
		message = EncryptMorse(InputFileContent,MORSE_DICTIONARY);

	WriteToFile(message);
	
if __name__ == '__main__':
    main()
