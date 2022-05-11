# tests/read_files.py
# uses data/sample.txt
from utilities import *

# when you use only open(file) as file this might lead to stack/buffer overflow (memory leak)

with open("../data/sample.txt") as samplefile:
    #  READING LINE BY LINE
    # firstline = samplefile.readline()  # reading line by line

    # READING AS A LIST OF LINE
    # lines = samplefile.readlines()   # returns you the list with lines in it
    # print(lines)
    # print("printing each line....")
    # for line in lines:
    #     print(line)
    #     print('------------------')

    # READING AS A WHOLE FILE
    contents = samplefile.read()
    print("reading the file a whole")
    print(contents)

with open("../data/sample.txt", 'a') as samplefile:
    print(".... writing to the file ...")
    samplefile.write(f"{get_str_seconds()} - Test Result : Test passed\n")

import yaml
print("****** using yaml file *******************")
# content = None
with open("../data/sample_input.yml") as input_file:
    input = yaml.safe_load(input_file)

print(input)
print(input['xmas-fifth-day']['num-birds'])    # >> 'four'
print(input['calling-birds'][1]) # >> 'dewey'