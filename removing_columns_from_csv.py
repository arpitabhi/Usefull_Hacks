import os
import re
import csv

#path = input('Enter the path to folder: ')
path = '/home/cfg/new'
try:
    var1 = os.listdir(path)
except:
    print("Path not found")

global col_name
col_name=input("Enter the column name: ")

for i in var1:
    input_file = path+'/'+i
    output_file = path+'/'+'nu_'+i
    if re.search('^test_.*\.csv$',i):
        global k
        with open(input_file, "r") as source:
            reader = csv.reader(source)
            names = next(reader)
            try:
                k=names.index(col_name)
            except:
                print("Column not found")
        with open(input_file, "r") as source:
            reader = csv.reader(source)
            with open(output_file, "w", newline='') as result:
                writer = csv.writer(result)
                for row in reader:
                    del row[k]
                    writer.writerow(row)
        os.rename(output_file,input_file)
        
    else:
        pass







