import csv, json, hashlib

#End result = New CSV File
new_csv = 'HNGi9 CSV FILE.output.csv'
f = open(new_csv, 'w')
writer = csv.writer(f)
writer.writerow(['Team Names', 'Series Number', 'Filename', 'Name', 'Description', 'Gender', 'Attributes', 'UUID', 'SHA-256'])

#Process A- first of all, convert the csv file to one json file per entry
        #Step 1
        #open a csv file handler

csv_file = open(input('Hello User, enter the absolute path or name of your CSV file: '), 'r')
read_csv = csv.reader(csv_file, delimiter=',')
next(read_csv)
data = [i for i in read_csv] 

        #Step 2
        #convert each row into a dictionary
        #and add the converted data to the data_variable
for row in data:
        if row[1] and row[2]:
            Teamnames, SN, Filename, Name, Description, Gender, Attributes, UUID = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            
        #creating the data dictionary
            json_file = {
                "format": "CHIP-0007",
                "filename": Filename,
                "name": Name,
                "description": Description,
                "gender": Gender,
                "minting_tool": Teamnames,
                "sensitive_content": False,
                "series_number": SN,
                "series_total": "420",
                "attributes": [
                        {
                                    "trait_type": "gender",
                                    "value": Gender,
                        },
                                
                ], 
                "collection": {
                        "name": "Zuri NFT Tickets for Free Lunch",
                        "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                        "attributes": [
                        {
                                    "type": "description",
                                    "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                }}
                
            attr = [x.split(':') for x in Attributes.split(';') if x]
                
            for att in attr:
                    json_file['attributes'].append({'trait_type': att[0].strip(), 'value':att[1].strip()})

        #Step 3
        #open a json file handler and use json.dumps
        #method to dump the data
        
            jsonCreate = json.dumps(json_file, indent=4)
            with open(f'Output/json/{Filename}.json', 'w') as output:
        #Step 4
                    output.write(jsonCreate)
            output.close()

#Process B- Creating Sha256 hash from the created json file
            hashString = hashlib.sha256(jsonCreate.encode()).hexdigest()

#Process C- Append the sha256_hash as a new column in csv file 
            row.append(hashString)
            writer.writerow(row)


f.close()
        