CS 430 Summer Project
========================

Emma Foley, A20290331

To Run
======
Run 'make' in the top level directory, Huffman_Encoding_Decoding

About
======
This program focuses on three areas:

#. Identifing the kth largest element in a list, using random selection and recursion
#. Sorting an unsorted list
#. Huffman encoding (incomplete)

This is a terminal program, where users will be prompted to make selections and enter values.  For ease, there is the option of randomly generating lists as needed and running the program in 'test mode'

At this time, 'test mode' only checks part 1&2, comparing the results against the built-in python functions for lists

Huffman coding:
* imports the first chapter of Pride and Prejudice (found via Project Gutenberg) from a text file
* creates a frequency table of characters
* Uses a custom node class with character, frequency, right, and left
* Uses a priority queue to create a binary tree of these nodes for the algorithm in section 16.3 of Introduction to Algorithms
* Prints the tree as a list
* Assigns digits

Decoding is not done and prefix assignment does not appear to be correct

Python
======
This was written in a python virtual environment, running python 3.5.2

The required packages are included in the requirements.txt and can be imported via:
	'pip install -r requirements.txt'

Output
======
This program prints to a timestamped text file in the 'logs' subdirectory.

If you run this in test mode, search for "PASS" and (perhaps more importantly) "FAIL".  This tests the kth value finding and quicksort against the results of puthon's sort and find by index.

Resources
========
* Algorithm Design: Kleinberg & Tardos
* Introduction to Algorithms: Cormen, Leiserson, Rivest, Stein
* https://www.techrepublic.com/article/huffman-coding-in-python/
* https://rosettacode.org/wiki/Huffman_coding#Python
* https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476
* https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
* Hitchhiker's Guide to Python


