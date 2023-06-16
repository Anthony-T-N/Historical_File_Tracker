__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

def write_to_text(directory_list):
  input_file = open("p[]-old.txt", "r")
  input_file_lines = input_file.readlines()
  output_file = open("p[].txt", "w")
  deleted_list_file = open("deleted_files", "w")

  range_num = 0
  print(str(len(input_file_lines)) + "+" + str(len(directory_list)))

  # Usually new file.
  if (len(input_file_lines) == 0):
    for i in range(len(directory_list)):
      output_file.write(directory_list[i] + "\n")
    input_file.close()
    output_file.close()
    os.remove("p[]-old.txt")
    os.rename('p[].txt', 'p[]-old.txt')
    return

  if (len(input_file_lines) >= len(directory_list)):
    range_num = len(input_file_lines)
  else:
    range_num = len(directory_list)

  print(range_num)

  i = 0
  for i in range(range_num):
    print(input_file_lines[i].strip() + " | " + directory_list[i].strip())
    if (input_file_lines[i].strip() != directory_list[i].strip()):
      print("UNMATCH")
      deleted_list_file.write(input_file_lines[i].strip() + "\n")
    else:
      output_file.write(directory_list[i] + "\n")
    i += 1

  print("!@")

  input_file.close()
  output_file.close()
  os.remove("p[]-old.txt")
  os.rename('p[].txt', 'p[]-old.txt')

# Recursively read all files in directory and store as list.
def read_directory():
  dir_list = os.listdir("./")
  return dir_list

def main():
  print("Running")
  write_to_text(read_directory())

if __name__ == '__main__':
  main()
