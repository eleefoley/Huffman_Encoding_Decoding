import math
import random
# used for testing the median finding function
from statistics import median

def main ():
	prompt()

# input from the user to determine which function(s) to go through
def prompt():
	print("Welcome to the CS 430 summer project!")
	done = False
	print_mode = False
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
			run_tests()
			done = True
		elif(response == 'b'):
			print_mode = True
			done = True
		else:
			print("Try again\n")

# Algorithm Design, Keinberg & Tardos: 13.5 Randomized Divide and Conquer: Median-Finding and Quicksort


# split = unsorted_list[0]
def select(S,k, print_mode): 
	if print_mode == True:
		print("We're looking for the " + str(k) +"th element of " + str(S))
    
	if len(S) == 1:
#         assert k == 0
		return S[0]
    
	if len(S) > 1 and all(element == S[0] for element in S):
		return S[0]
    
	split = random.choice(S)
	if print_mode == True:
		print("     We choose a random element to compare the others against, " + str(split))
	s_minus = []
	s_plus = []
	s_equal = []
    
	for i in S:
		if i < split:
			s_minus.append(i)
		elif i > split:
			s_plus.append(i)
		elif i == split:
 			s_equal.append(i)
    
	l = len(s_minus)

	if l >= k:
		if print_mode == True:
			print("     There are more than " + str(k) + " smaller values, so let's look inside that sub-list, s_minus")
		return select(s_minus, k, print_mode)
	elif l >= k - len(s_equal):
		if print_mode == True:
			print("     There are " + str(l) + " smaller values, so it is the one we're looking for")
		return split
	else:
		if print_mode == True:
			print("     There are than " + str(len(s_plus)) + " larger values, so let's look inside the other sub-list, s_plus")
		return select(s_plus,k-l-len(s_equal), print_mode)


##########################functions used for testing#############3
# given a lenght, generate a random 
def random_unsorted_list(n, max_val):
	test_list = []
	for i in range(n):
		test_list.append(random.choice(range(2,max_val)))
	#print(test_list)
	return test_list


# test the select function for randomized median finding
def test_select():
	print("1. testing select function for randomized median finding against the result of the python builtin sort for lists and lookup by index")
	for i in range(1,15):
		unsorted_list = random_unsorted_list(i,100)
		sorted_list = list(unsorted_list)
		sorted_list.sort()
		for i in range(1,len(unsorted_list)):
			my_kth = select(unsorted_list, i,print_mode = False)
			true_kth = sorted_list[i-1]
			if(my_kth != true_kth):
				print("	select function failed to find the kth element  for array " + str(unsorted_list) + "\n")
				print(str(my_kth) + " != " + str(true_kth))
				return False
	print("	select function successfully finds the kth element")
	return True
		
# run all the tests, returning True if they pass, Fail if they do not
def run_tests():
	print("Running tests")
	select = test_select()
	if(select == False):
		print("	Failed one or more tests")
	else:
		print("	All tests passed")
main()
