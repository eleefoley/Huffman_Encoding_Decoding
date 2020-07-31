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

# Algorithm Design, Keinberg & Tardos: 13.5 Randomized Divide and Conquer: Median-Finding and Quicksort
def select(S,k):
	s_minus = []
	s_plus = []
	split = random.choice(range(1,len(S)))-1
	for i in S:
		if i < S[split]:
			s_minus.append(i)
		elif i > S[split]:
			s_plus.append(i)
		
	if len(s_minus) == k-1:
		return(S[split])
	elif len(s_minus) >= k:
		select(s_minus,k)

main()
