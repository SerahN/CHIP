import csv
import json
import hashlib

#End result = New CSV File
new_csv = 'Filename.output.csv'
f = open(new_csv, 'w')
writer = csv.writer(f)
writer.writerow([])

#Process A- first of all, convert csv file to one json file per entry
def csv_to_json(csv_file_path, json_file_path):
    #creating the data dictionary
    data_dict = {}
 
    #Step 2
    #open a csv file handler
    with open(csv_file_path, encoding = 'utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
 
        #convert each row into a dictionary
        #and add the converted data to the data_variable
 
        for rows in csv_reader:
 
            #the row tagged serial number is the primary key
            key = rows['Serial Number']
            data_dict[key] = rows
 
    #open a json file handler and use json.dumps
    #method to dump the data
    #Step 3
    jsonfile = json.dumps(data_dict, indent = 4)
    with open(f'json/''.json', 'w') as json_output:
        #Step 4
                json_output.write(jsonfile)
    json_output.close()
 
#Ensure you provide the correct absolute path for the csv file you want to change 
#Step 1
csv_file_path = input('Hello User, enter the absolute path of your CSV file: ')
json_file_path = json
 
csv_to_json(csv_file_path, json_file_path)

#Process B- Creating Sha256 hash from the created json file

sha256_hash = hashlib.sha256()
with open(json_file_path,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())

#Process C- Append the sha256_hash as a new column in csv file 
# def add_col_to_csv(Naming.csv, csv,new_list):
#     with open(Naming.csv, 'r') as read_f, \
#         open(new.csv, 'w', newline='') as write_f:
#         csv_reader = csv.reader(read_f)
#         csv_writer = csv.writer(write_f)
#         i = 0
#         for row in csv_reader:
#             row.append(new_list[i])
#             csv_writer.writerow(row)
#             i += 1 
#             new_list = ['sha-256',0]