#!/usr/bin/python3

import sys

file = open("Test.txt","w")
file_text = ""
file_finish = "1"
while file_text != file_finish:
	file_text = input("Enter text: ")
	if file_text == file_finish:
		break
	file.write(file_text)
	file.write("\n")
file.close()
    
file = open("Test.txt","r")
file_text = file.read()
file.close
print (file_text)
