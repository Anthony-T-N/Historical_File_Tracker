__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

def write_to_text(directory_list, historical_file, temp_file):
  input_file = open(historical_file, "r")
  input_file_lines = input_file.readlines()
  output_file = open(temp_file, "w")
  deleted_list_file = open("deleted_files", "w")

  range_num = 0
  print(str(len(input_file_lines)) + "+" + str(len(directory_list)))

  # Usually new file.
  if (len(input_file_lines) == 0):
    for i in range(len(directory_list)):
      output_file.write(directory_list[i] + "\n")
    input_file.close()
    output_file.close()
    os.remove(historical_file)
    os.rename(temp_file, historical_file)
    return

  if (len(input_file_lines) >= len(directory_list)):
    range_num = len(input_file_lines)
  else:
    range_num = len(directory_list)

  print(range_num)

  input_line_count = 0
  directory_list_count = 0
  for i in range(range_num):
    print(input_file_lines[input_line_count].strip() + " | " + directory_list[directory_list_count].strip())
    if (input_file_lines[input_line_count].strip() != directory_list[directory_list_count].strip()):
      print("UNMATCH")
      deleted_list_file.write(input_file_lines[input_line_count].strip() + "\n")
      directory_list_count += 1
    else:
      output_file.write(directory_list[directory_list_count] + "\n")
      input_line_count += 1
      directory_list_count += 1

  print("!@")

  input_file.close()
  output_file.close()
  os.remove(historical_file)
  os.rename(temp_file, historical_file)

# Recursively read all files in directory and store as list.
def read_directory():
  dir_list = os.listdir(".\\Sample_Directory")
  return dir_list

def main():
  print("Running")
  historical_file = ".\\p[]-old.txt"
  temp_file = ".\\p[].txt"
  write_to_text(read_directory(), historical_file, temp_file)

if __name__ == '__main__':
  main()
