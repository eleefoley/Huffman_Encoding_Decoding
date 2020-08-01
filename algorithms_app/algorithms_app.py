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
			done = True
		else:
			print("Try again\n")

# Algorithm Design, Keinberg & Tardos: 13.5 Randomized Divide and Conquer: Median-Finding and Quicksort
def splitter(S):
    if len(S) == 1:
        split = S[0]
    else:
        split = random.choice(S)
    return split

def select(S,k, splitter):
        if len(S) == 0:
            return []
        if len(S) == 1:
            return S[0]
        
        s_minus = []
        s_plus = []
        test_median = splitter(S)
        print("The test median is: " + str(test_median))
        for i in S:
            if i < test_median:
                s_minus.append(i)
            elif i > test_median:
                s_plus.append(i)

        if len(s_minus) == k - 1:
#             print("condition one")
#             print("The kth element is: " + str(test_median))
            return test_median
        elif len(s_minus) >= k:
#             print("condition two")
            if len(s_minus) == 0:
                return test_median
            else:
                test_median = select(s_minus,k,splitter)
                return test_median
        else:
#             print("condition three")
            test_median = select(s_plus, k - 1 - len(s_plus), splitter)
            return test_median

##########################functions used for testing#############3
# given a lenght, generate a random 
def random_unsorted_list(n):
	test_list = []
	for i in range(n):
		test_list.append(random.choice(range(1,100)))
	return test_list


# test the select function for randomized median finding
def test_select():
	print("testing select function for randomized median finding")
	for i in range(3,8,2):
		unsorted_list = random_unsorted_list(i)
		unsorted_list = [83, 53, 38, 44, 51, 52]
		if len(unsorted_list) % 2 != 0:
    			k = len(unsorted_list)/2 + 1
		else:
    			k = len(unsorted_list) / 2 + .5
		my_median = select(unsorted_list, k, splitter)
		true_median = median(unsorted_list)
		if my_median != true_median:
			print("	select function failed to find the median for array " + str(unsorted_list) + "\n")
			print(str(k) + " != " + str(true_median))
			return False
	print("	select function successfully finds the median")
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
