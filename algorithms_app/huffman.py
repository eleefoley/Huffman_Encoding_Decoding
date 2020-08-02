import pandas
from pathlib import Path

file_name = 'pride_and_prejudice_ch_1.txt'
#folder_path = Path("./text/")
file_to_open = Path("text/" + file_name)
print(file_to_open)
print(file_to_open.exists())

with open(file_to_open, 'r') as file:
    data = file.read().replace('\n', '')
