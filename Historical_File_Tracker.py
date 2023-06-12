__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

# Recursively read all files in directory and store as list.
def read_files():
  dir_list = os.listdir("./")
  return dir_list

def write_to_text(list):
  output_file = open("p[].txt", "w")

def main():
  print("Running")
  print(read_files())
  write_to_text(read_files())

if __name__ == '__main__':
  main()
