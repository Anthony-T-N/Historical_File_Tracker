__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

def write_to_text(directory_list, historical_file, temp_write_file):
  historical_file = open(historical_file, "r")
  historical_file_lines = historical_file.readlines()
  temp_write_file = open(temp_write_file, "w")
  deleted_list_file = open("deleted_files", "a")

  range_num = 0
  print(str(len(historical_file_lines)) + "+" + str(len(directory_list)))

  # Usually new file.
  if (len(historical_file_lines) == 0):
    for i in range(len(directory_list)):
      temp_write_file.write(directory_list[i] + "\n")
    historical_file.close()
    temp_write_file.close()
    os.remove(historical_file)
    os.rename(temp_write_file, historical_file)
    return

  if (len(historical_file_lines) >= len(directory_list)):
    range_num = len(historical_file_lines)
  else:
    range_num = len(directory_list)

  print(range_num)

  historical_file_count = 0
  directory_list_count = 0
  for i in range(range_num):
    
    if (historical_file_count >= range_num or directory_list_count >= range_num):
      break

    print("DEBUG SECTION: historical_file_count: " + str(historical_file_count) + " directory_list_count: " + str(directory_list_count) + "\n")

    print(historical_file_lines[historical_file_count].strip() + " | " + directory_list[directory_list_count].strip())
    if (historical_file_lines[historical_file_count].strip() != directory_list[directory_list_count].strip()):
      print("UNMATCH")
      deleted_list_file.write(historical_file_lines[historical_file_count].strip() + "\n")
      temp_write_file.write(directory_list[directory_list_count].strip() + "\n")
      directory_list_count += 1
    else:
      temp_write_file.write(directory_list[directory_list_count].strip() + "\n")
      historical_file_count += 1
      directory_list_count += 1

  print("!@")

  historical_file.close()
  temp_write_file.close()
  os.remove(historical_file)
  os.rename(temp_write_file, historical_file)

# Recursively read all files in directory and store as list.
def read_directory():
  dir_list = os.listdir("Historical_File_Tracker\Sample_Directory\\")
  return dir_list

def main():
  print("Running")
  historical_file = "Historical_File_Tracker\p[]-old.txt"
  temp_write_file = "Historical_File_Tracker\p[].txt"
  write_to_text(read_directory(), historical_file, temp_write_file)

if __name__ == '__main__':
  main()
