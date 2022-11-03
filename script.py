import csv
import hashlib
import json

#End result = New CSV File
new_csv = 'filename.output.csv'
f = open(new_csv, 'w')
writer = csv.writer(f)
writer.writerow(['S/N', 'Filename','Name','Description','Gender','UUID', 'SHA256'])

#Process A- first of all, convert the csv file to one json file per entry
# def csv_to_json(csv_file, json_file_path):

        #Step 2
        #open a csv file handler
with open('naming.csv', 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    data = [a for a in read_csv] 

   #convert each row into a dictionary
                #and add the converted data to the data_variable

    for row in data:
        #the row tagged serial number is the primary key
        # key = row['Series Number']
        # data_dict[key] = row
        if row[1] and row[2]:
            SN, File_name, UUID = row[0], row[1], row[2]
           #creating the data dictionary
            json_file = {
                "format": "CHIP-0007",
                "name": File_name,
                "description": " ",
                "minting_tool": " ",
                "sensitive_content": False,
                "series_number": SN,
                "series_total": data[-1][0],
                "collection": {
                        "name": "HNG9 NFT COLLECTION",
                        "id": UUID,
                }
        }

            #Step 3
        #open a json file handler and use json.dumps
        #method to dump the data
        
            jsonCreate = json.dumps(json_file, indent=4)
            with open(f'json/{File_name}.json', 'w') as output:
        #Step 4
                    output.write(jsonCreate)
            output.close()

 #Process B- Creating Sha256 hash from the created json file
            hashString = hashlib.sha256(jsonCreate.encode()).hexdigest()

#Process C- Append the sha256_hash as a new column in csv file 
            row.append(f'{File_name}.{hashString}.csv')
            writer.writerow(row)


f.close()
        