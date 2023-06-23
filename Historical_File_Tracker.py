__author__ = 'Anthony N'
__version__ = '---'
__date__ = '2023-06-12'

import os

def write_to_text(directory_list, historical_file, temp_write_file, deleted_files):
  historical_file_o = open(historical_file, "r")
  historical_file_lines = historical_file_o.readlines()
  temp_write_file_o = open(temp_write_file, "w")
  deleted_list_file = open(deleted_files, "a")

  range_num = 0
  print(str(len(historical_file_lines)) + "+" + str(len(directory_list)))

  # Usually new file.
  if (len(historical_file_lines) == 0):
    for i in range(len(directory_list)):
      temp_write_file_o.write(directory_list[i] + "\n")
    historical_file_o.close()
    temp_write_file_o.close()
    os.remove(str(historical_file))
    os.rename(temp_write_file, historical_file)
    return

  if (len(historical_file_lines) >= len(directory_list)):
    range_num = len(historical_file_lines)
  else:
    range_num = len(directory_list)

  print(range_num)

  historical_file_count = 0
  directory_list_count = 0
  '''
  # Method 1
  for i in range(range_num):
    
    if (historical_file_count >= range_num or directory_list_count >= range_num):
      break

    print("\n" + "DEBUG SECTION: historical_file_count: " + str(historical_file_count) + " directory_list_count: " + str(directory_list_count) + "\n")
    print(historical_file_lines[historical_file_count].strip() + " | " + directory_list[directory_list_count].strip())

    if (historical_file_lines[historical_file_count].strip() != directory_list[directory_list_count].strip()):
      print("UNMATCH")
      print(historical_file_lines[historical_file_count].strip() + " Deleted")
      deleted_list_file.write(historical_file_lines[historical_file_count].strip() + "\n")
      temp_write_file_o.write(directory_list[directory_list_count].strip() + "\n")
      directory_list_count += 1
    else:
      temp_write_file_o.write(directory_list[directory_list_count].strip() + "\n")
      historical_file_count += 1
      directory_list_count += 1
  '''

  historical_file_count = 0
  directory_list_count = 0
  # Method 2
  for i in range(range_num):
    print("\n" + "DEBUG SECTION: historical_file_count: " + str(historical_file_count) + " directory_list_count: " + str(directory_list_count) + "\n")
    print(historical_file_lines[historical_file_count].strip() + " | " + directory_list[directory_list_count].strip())

    for j in range(range_num):
      print(str(j) + " " + str(len(directory_list)))
      if (j == len(directory_list)):
        print("Missing")
        break
      print(historical_file_lines[i].strip() + " | " + directory_list[j].strip())
      if (historical_file_lines[i].strip() == directory_list[j].strip()):
        print("Remove")
        break

  historical_file_o.close()
  temp_write_file_o.close()
  os.remove(historical_file)
  os.rename(temp_write_file, historical_file)

# Recursively read all files in directory and store as list.
def read_directory():
  dir_list = os.listdir("Historical_File_Tracker/Sample_Directory/")
  return dir_list

def main():
  print("Running")

  current_path = os.path.dirname(__file__)

  historical_file = os.path.join(current_path, "p[]-current.txt")
  temp_write_file = os.path.join(current_path, "p[]-temp.txt")
  deleted_files = os.path.join(current_path, "deleted_files.txt")

  print(historical_file)
  print(temp_write_file)

  write_to_text(read_directory(), historical_file, temp_write_file, deleted_files)

if __name__ == '__main__':
  main()
