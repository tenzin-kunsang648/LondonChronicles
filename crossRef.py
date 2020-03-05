import sys
import csv


'''
usage: python3 Python_name "CSV file name" "Chronicles Text file name"
Example: python3 crossRef.py "Gazetteer.csv" "Chronicle.txt" 
'''

csv_file = sys.argv[1]
txt_file = sys.argv[2]

location_dict = {}
with open(csv_file, "r") as file:
    for line in file:
        line = line.split(",")
        names = line[5].split("|")
        for name in names:
            name = name.strip()
            location_dict[name] = line[3]
print(len(location_dict))

big_list = []
with open(txt_file, encoding = "utf8", errors = 'ignore') as file:
    for line in file:
        big_list.append(line.strip("\n"))
        
big_string = " ".join(big_list)

count_dict = {}

for key in location_dict:
    count = big_string.count(key)
    totalcount = count_dict.get(location_dict[key], 0)
    totalcount += count
    count_dict[location_dict[key]] = totalcount
    
print(count_dict)

with open('frequency', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in count_dict.items():
        writer.writerow([key, value])
csv_file.close()