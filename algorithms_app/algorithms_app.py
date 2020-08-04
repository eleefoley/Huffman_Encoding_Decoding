import math
import random
import pandas as pd
from pathlib import Path
from datetime import datetime

####global variables#####
log_filename = datetime.now().strftime("%Y%m%d_%H.%M.%S") + ".txt"
log_pathstring = str(Path("./logs/" + log_filename))
break_message = "#####\n\n"

####################

def main ():
	log_message("CS 430 Summer 2020 Final Project, Emma Foley\n")
	prompt()
	log_message(break_message, False)
	log_message("Exiting")

####################logging functions###################
def log_message(message, timestamp = True):
	message = "	" + message + "\n"
	with open(log_pathstring, "a+") as file:
		if(timestamp):
			lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),message]
			file.writelines(lines)
		else:
			file.write(message)

#####################ui functions###################
# input from the user to determine which function(s) to go through
def prompt():
	print("Welcome to the CS 430 summer project!")
	message = "Starting user prompts"
	log_message(break_message, False)
	log_message(message)

	done = False
	print_mode = False
	while(done == False):
		message = "User chose to "
		response = input("""Type the letter for what you would like to do:
			a:  Run in test mode
			b:  Choose a function to run
			c:  Exit the program
		""")
		if(response == 'c'):
			message = message + "exit the program"
			log_message(message)
			exit()
			done = True
		elif(response == 'a'):
			message = message + "run in test mode"
			log_message(message, False)
			run_tests()
			done = True
		elif(response == 'b'):
			print_mode = True
			message = message + " pick a function"
			log_message(message, False)
			user_choose_a_function(print_mode)
			done = True
		else:
			print("Try again\n")
			done = True

def user_manual_or_random():
    print("Random or Manual Mode")
    done = False
#     print_mode = False
    while(done == False):
            message = "User chose to "
            response = str()
            try:
                response = str(input("""Choose whether you want to enter a list manually or have one randomly generated:
                        a:  Random
                        b:  Manual
                        c:  Exit the program
                """)).strip()
            except Exception as error:
                print(error)
            if(response == 'c'):
                    message = message + "exit the program"
                    log_message(message)
                    exit()
                    done = True
            elif(response == 'a'):
                    message = message + "randomly generate a list: "
                    n = user_random_list_params()
                    unsorted_list = random_unsorted_list(n,100)
                    message = message + str(unsorted_list)
                    log_message(message, False)
                    return unsorted_list
                    done = True
            elif(response == 'b'):
                    message = message + "enter a list of integers: " 
                    unsorted_list = user_entered_list()
                    message = message + str(unsorted_list)
                    log_message(message, False)
                    return unsorted_list
                    done = True
            else:
                    log_message("Invalid user entry", True)
                    print("Try again\n")
                    done = True
  
def user_choose_a_function(print_mode):
    print("Choose a function")
    done = False
    print_mode = True
    while(done == False):
            response = str()
            try:
                response = str(input("""Choose a function to run:
                    a:  Find the kth element of a list
                    b:  Sort a list
                    c:  Huffman encoding
                    d:  Exit the program
            """)).strip()
            except Exception as error:
                print(error)
            if(response == 'd'):
                    exit()
                    done = True
            elif(response == 'a'):
                    unsorted_list = user_manual_or_random()
                    k = user_choose_k(len(unsorted_list))
                    print("Run that function")
                    log_message(break_message, False)
                    print(select(unsorted_list,k,print_mode))
                    done = True
            elif(response == 'b'):
                    unsorted_list = user_manual_or_random()
                    print("Run that function")
                    log_message(break_message, False)
                    print(quicksort(unsorted_list,print_mode))
                    done = True
            elif(response == 'c'):
                    print("Huffman encoding")
                    huffman()
                    log_message(break_message, False)
                    done = True
            else:
                    print("Try again\n")
                    done = True
  

#get a manually entered list from a user
def user_entered_list():
    type_correct = False
    while type_correct == False:
        try:
            response = str(input("Type in a list of integer values, separated by commas like this: '1,2,3,4' ")).replace(" ","")
    #         response = tuple(response)
            print(response)
            unsorted_list = response.split(",")
            for i, item in enumerate(unsorted_list):
                unsorted_list[i] = int(item)
            if all(isinstance(item, int) for item in unsorted_list) == True:
                type_correct = True
        except Exception as error:
            print(error)
    print("You entered: " + str(unsorted_list))
    return unsorted_list

def user_random_list_params():
    type_correct = False
    while type_correct == False:
        try:
            response = input("Type the desired length of your list (an integer): ")
#             print(response)
#             print(type(response))
            n = int(response)
            type_correct = True
        except Exception as error:
            print(error)
    print("Let's generate a list of length: " + str(n))
    return n

def user_choose_k(n):
    type_correct = False
    while type_correct == False:
        try:
            response = str(input("Choose which element between 1 and the length of your list you'd like to find. (1 for the minimum, n for the maximum): ")).replace(" ","")
#             print(response)
#             print(type(response))
            k = int(response)
            if k in range(1,n+ 1):
                type_correct = True
        except Exception as error:
            print(error)
    print("You've selected to look for the " + str(k) + "th element")
    return k
######################random median finding functions######################333
###### Algorithm Design, Keinberg & Tardos: 13.5 Randomized Divide and Conquer: Median-Finding and Quicksort
# split = unsorted_list[0]
def select(S,k, print_mode):
	log_message("Begin select function for randomized recursive finding of the " + str(k) + "th element of " + str(S))
	if print_mode == True:
		print("We're looking for the " + str(k) +"th element of " + str(S))
	if len(S) == 1:
#         assert k == 0
		log_message("Return the one element list, " + str(S[0]), False)
		return S[0]
    
	if len(S) > 1 and all(element == S[0] for element in S):
		log_message("All elements are equivalent, " + str(S[0]), False)
		return S[0]
   
	split = random.choice(S)
	log_message("The randomly selected split element is: " + str(split), False)
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
	log_message("Elements smaller than the split: " + str(s_minus), False)
	log_message("Elements larger than the split: " + str(s_plus), False)
	log_message("Elements equal to the split: " + str(s_equal), False)
	
	if l >= k:
		log_message("Look inside the smaller elements", False)
		if print_mode == True:
			print("     There are more than " + str(k) + " smaller values, so let's look inside that sub-list, s_minus")
		return select(s_minus, k, print_mode)
	elif l >= k - len(s_equal):
		log_message("The " + str(k) + "th element is: " + str(split), True)
		if print_mode == True:
			print("     There are " + str(l) + " smaller values, so it is the one we're looking for")
		return split
	else:
		log_message("Look inside the larger elements", False)
		if print_mode == True:
			print("     There are than " + str(len(s_plus)) + " larger values, so let's look inside the other sub-list, s_plus")
		return select(s_plus,k-l-len(s_equal), print_mode)

def quicksort(S,print_mode):
    log_message("Begin quicksort function on " + str(S))
    if print_mode == True:
        print("We're using the result of our randomized median function to help us recursively sort the list " + str(S))
    n = len(S)
#     print(n)
    if n == 1:
        log_message("There is only one element in the list: " + str(S))
        if print_mode == True:
            print("    The list is only one element long, so no need to sort")
        return S
    elif n <= 3:
        if print_mode == True:
            print("    The list is less than three elements long, so we'll sort using the minimums")
        temp_1 = []
        temp_2 = list(S)
#         print temp_2
        for i in range(0,n):
            min_value = min(temp_2)
            temp_2.remove(min_value)
            temp_1.append(min_value)
#             print(temp_1)
        S = temp_1
        log_message("Less than 4 elemengs, sorted by minimums: " + str(S))
        return S
    else:
        s_minus = []
        s_plus = []
        s_equal = []
        
        midpoint = n//2 + 1
        # use the select function that we wrote for randomized median finding to get us to the right pivot point from the get-go
        split = select(S,midpoint, False)
        log_message("Returning to the quicksort function, using " + str(split) + " as our split point", False)
        if print_mode == True:
            print("   The median is " + str(split))
#         found = False
        for i in S:
            if i < split:
                s_minus.append(i)
            elif i > split:
                s_plus.append(i)
            elif i == split:
                s_equal.append(i)
 	
        log_message("Elements smaller than the split: " + str(s_minus), False)
        log_message("Elements larger than the split: " + str(s_plus), False)
        log_message("Elements equal to the split: " + str(s_equal), False)
				        		   
        if print_mode == True:
            print("    Recursively use this sorting method on any values less than " + str(split))
        
        log_message("Now sort the list of smaller elements", False)
        s_minus = quicksort(s_minus, print_mode)
        if print_mode == True:
            print("    Recursively use this sorting method on any values greater than " + str(split))
        s_plus = quicksort(s_plus, print_mode)
        log_message("Now sort the list of larger elements", False)
        s_minus = quicksort(s_minus, print_mode)
        
#         print(s_minus)
#         print(s_plus)
#         print(s_equal)
        log_message("Concatenate the resulting lists", False)
        if print_mode == True:
            print("    Concatenating together " + str(s_minus) + ", " + str(s_equal) + ", " + str(s_plus))
        sorted_list = list(s_minus)
#         print(sorted_list)
        sorted_list = sorted_list + s_equal
#         print(sorted_list)
        sorted_list = sorted_list + s_plus
#         print(sorted_list)
        if print_mode == True:
             print("    The sorted result is " + str(sorted_list) + "\n")
        log_message("The sorted result is " + str(sorted_list))
        return sorted_list

####################huffman#############
class Node(object):
    left = None
    right = None
    char = None
    prefix_part = None
    freq = 0
    
    def __init__(self,c,f):
        self.char = c
        self.freq = f
    
    def set_children(self,left_node,right_node):
        self.left = left_node
        self.right = right_node
    
    def set_prefix_part(self, n):
        self.prefix_part = n
        
    def __repr__(self):
        return "%s - %s -- %s _ %s" % (self.char, self.freq, self.left, self.right)
    
    def __cmp__(self,other_node):
        return cmp(self.freq, other_node.freq)
    
    def insert(self, other_node):
# Compare the new value with the parent node
        if self.freq:
            if other_node < self:
               if self.left is None:
                    self.left = other_node
               else:
                    self.left.insert(other_node)
            elif other_node > self:
                if self.right is None:
                    self.right = other_node
                else:
                    self.right.insert(other_node)
        else:
            self = other_node
    
    def print_tree(self,count = 1, pos = 'mid'):
        if self.left:
            self.left.print_tree(count + 2, 'left')
#         print(' ' * count + str(self.char))
        text = str(self.char)
        if pos == 'mid':
            print(text)
        elif pos == 'left':
            print(' ' * count + text)
        elif pos == 'right':
            print('| ' + text)
        if self.right:
            self.right.print_tree(count + 2, 'left')
            

def textfile_to_str():
        file_name = 'pride_and_prejudice_ch_1.txt'
        file_to_open = Path("./algorithms_app/text/" + file_name)
        print("Opening the file to read in characters")

        data = str()
        with open(str(file_to_open), 'r') as file:
                data = file.read().replace('\n', '')
        return(data)


def str_to_count_df(text_string):
        char_df = pd.DataFrame(list(text_string), columns = ['char'])
        grouped_df = char_df.groupby('char').size().reset_index(name = "freq").sort_values(by = ['freq', 'char'], ascending = False).reset_index()
        print("Here are the most frequent characters in the file:\n")
        print(grouped_df.head())
        return grouped_df

class Binary_Freq_Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        
    def bubble_up(self,i):
        while i // 2 > 0:
          if self.heap_list[i] < self.heap_list[i // 2]:
             temp_spot = self.heap_list[i // 2]
             self.heap_list[i // 2] = self.heap_list[i]
             self.heap_list[i] = temp_spot
          i = i // 2

    def insert(self,freq):
        self.heap_list.append(freq)
        self.current_size = self.current_size + 1
        self.bubble_up(self.current_size)
        
    def bubble_down(self,i):
        while (i * 2) <= self.current_size:
            smallest = self.get_smallest_freq(i)
            if self.heap_list[i] > self.heap_list[smallest]:
                temp_spot = self.heap_list[i]
                self.heap_list[i] = self.heap_list[smallest]
                self.heap_list[smallest] = temp_spot
            i = smallest
        
    def get_smallest_freq(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_smallest(self):
        deleted = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.bubble_down(1)
        return deleted

    def build_freq_heap(self,freq_list):
        i = len(freq_list) // 2
        self.current_size = len(freq_list)
        self.heap_list = [0] + freq_list[:]
        while (i > 0):
            self.bubble_down(i)
            i = i - 1

def children(node_heap, position):
    node_list = node_heap.heap_list
    size = node_heap.current_size
    if position > size - 1:
       print("There is no node at this heap position", position)
       return
    else:
       print("Parent", node_list[position])
             
    if (2*position+1) > size-1:
        print("no children for this node")
        return [None,None]
    else:
        print("Left Child",node_list[2*position+1])
        if not((2*position+2) > size-1):
           print("Right Child",node_list[2*position +2])
    return [node_list[2*position+1],node_list[2*position +2]]

def huffman():
	data = textfile_to_str()
	count_df = str_to_count_df(data)
	
	node_queue = []
	for i, row in count_df.iterrows():
		new_node = Node(row['char'],row['freq'])
		node_queue.append(new_node)

	freq_heap = Binary_Freq_Heap()
	freq_heap.build_freq_heap(list(count_df['freq']))

	print(freq_heap.heap_list)

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
	log_message(break_message, False)
	log_message("Run the program in test mode, running functions on random values as needed and comparing to python built in results")
	message = "1. testing select function for randomized median finding against the result of the python builtin sort for lists and lookup by index"
	log_message(message)
	print(message)
	for i in range(1,15):
		log_message("\nTest 1 " + str(i), False)
		unsorted_list = random_unsorted_list(i,100)
		sorted_list = list(unsorted_list)
		sorted_list.sort()
		for i in range(1,len(unsorted_list)):
			my_kth = select(unsorted_list, i,print_mode = False)
			true_kth = sorted_list[i-1]
			log_message("The built in python sort and list indexing found: " + str(true_kth))
			if(my_kth != true_kth):
				print("select function failed to find the kth element  for array " + str(unsorted_list) + "\n", False)
				print(str(my_kth) + " != " + str(true_kth))
				
				log_message("select function failed to find the kth element  for array " + str(unsorted_list) + "\n", False)
				log_message(str(my_kth) + " != " + str(true_kth), False)
				
				log_message("!!!FAIL!!!", False)
				return False
	message = "	select function successfully finds the kth element"
	print(message)
	log_message(message, False)
	log_message("!!!PASS!!!")
	return True

# test the quicksort function for quicksorting using randomized median finding to smartly pick the pivot
def test_quicksort():
	message = "2. Testing the quicksort function for quicksorting using our kth element selector to smartly pick our pivot element, comparing the results to the builtin python list sort"
	print(message)
	log_message(message)
	for i in range(1,15):
		log_message("\nTest 2 " + str(i), False)
		unsorted_list = random_unsorted_list(i,100)
		sorted_list = list(unsorted_list)
		sorted_list.sort()
		
		my_sorted_list = quicksort(unsorted_list, False)
		
		log_message("The built in python sort function returned: " + str(sorted_list), False)
		if(sorted_list != my_sorted_list):
			print("  quicksort function failed to sort " + str(unsorted_list))
			print("  " + str(my_sorted_list) + " != " + str(sorted_list))
			log_message("  quicksort function failed to sort " + str(unsorted_list), False)
			log_message("  " + str(my_sorted_list) + " != " + str(sorted_list), False)
			return False

	message = "  quicksort function successfully sorts lists"
	print(message)
	log_message(message, False)
	log_message("!!!PASS!!!")
	return True
	
# run all the tests, returning True if they pass, Fail if they do not
def run_tests():
	print("Running tests")

	test_results = []

	select = test_select()
	test_results.append(select)

	quicksort = test_quicksort()
	test_results.append(quicksort)

	if(False in test_results):
		log_message("FAILED ONE OR MORE TESTS", False)
		print("	Failed one or more tests")
	else:
		log_message("PASSED ALL TESTS", False)
		print("	All tests passed")
main()
