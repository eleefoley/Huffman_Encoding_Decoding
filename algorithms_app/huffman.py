import pandas as pd
from pathlib import Path

class Node()
def main():
	data = textfile_to_str()
	count_df = str_to_count_df(data)
	
def textfile_to_str():
	file_name = 'pride_and_prejudice_ch_1.txt'
	file_to_open = Path("text/" + file_name)
	print("Opening the file to read in characters")
	
	data = str()
	with open(str(file_to_open), 'r') as file:
    		data = file.read().replace('\n', '')
	return(data)

def str_to_count_df(text_string):
	char_df = pd.DataFrame(list(text_string), columns = ['char'])
	grouped_df = char_df.groupby('char').size().reset_index(name = "count").sort_values(by = ['count', 'char'], ascending = False)
	print("Here are the most frequent characters in the file:\n")
	print(grouped_df.head())
	return grouped_df

main()
