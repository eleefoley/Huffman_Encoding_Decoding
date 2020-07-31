import math
import random
# used for testing the median finding function
import statistics

def main ():
	prompt()

def prompt():
	print("Welcome to the CS 430 summer project!")
	done = False
	while(done == False):
		response = input("""Type the letter for what you would like to do:
			a:  Run in test mode
			b:  Choose a function to run
			c:  Exit the program
		""")
		if(response == 'c'):
			exit()
			done = True
		elif(response == 'a'):
			done = True
		elif(response == 'b'):
			done = True
		else:
			print("Try again\n")

main()
