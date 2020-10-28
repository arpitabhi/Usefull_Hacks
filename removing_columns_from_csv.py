import os
import re
import csv

#PATH = input('Enter the path to folder: ')
PATH = '/home/cfg/new/'

try:
    var1 = os.listdir(PATH)
except:
    print("Path not found")

global COL_NAME
global INDEX_KEY

COL_NAME = input("Enter the column name: ")
REGEX_EXP = '^test_.*\.csv$'
ERROR_DES = "Column not found"

for i in var1:
    INPUT_FILE = PATH+i
    OUTPUT_FILE = PATH+'nu_'+i
    if re.search(REGEX_EXP,i):
        try:
            with open(INPUT_FILE, "r") as source:
                reader = csv.reader(source)
                names = next(reader)
                INDEX_KEY=names.index(COL_NAME)
                
            with open(INPUT_FILE, "r") as source:
                reader = csv.reader(source)
                with open(OUTPUT_FILE, "w", newline='') as result:
                    writer = csv.writer(result)
                    for row in reader:
                        del row[INDEX_KEY]
                        writer.writerow(row)
            os.rename(OUTPUT_FILE,INPUT_FILE)
        except:
            print(ERROR_DES)
        
    else:
        pass







