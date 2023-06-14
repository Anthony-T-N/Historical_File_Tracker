__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

# Recursively read all files in directory and store as list.
def read_files():
  dir_list = os.listdir("./")
  return dir_list

def write_to_text(list):
  input_file = open("p[]-old.txt", "r")
  input_file_lines = input_file.readlines()
  output_file = open("p[].txt", "w")

  count = 0
  for current_line in input_file_lines:
    count += 1
    print("Line{}: {}".format(count, current_line.strip()))

  for item in list:
    print(item)
    output_file.write(item + "\n")
  input_file.close()
  output_file.close()
  os.remove("p[]-old.txt")
  os.rename('p[].txt', 'p[]-old.txt')

def main():
  print("Running")
  write_to_text(read_files())

if __name__ == '__main__':
  main()
