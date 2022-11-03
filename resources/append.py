from csv import writer
from csv import reader
from csv import DictReader
from csv import DictWriter

def add_column_in_csv_2(input_file, output_file, transform_row, tansform_column_names):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a DictReader object from the input file object
        dict_reader = DictReader(read_obj)
        # Get a list of column names from the csv
        field_names = dict_reader.fieldnames
        # Call the callback function to modify column name list
        tansform_column_names(field_names)
        # Create a DictWriter object from the output file object by passing column / field names
        dict_writer = DictWriter(write_obj, field_names)
        # Write the column names in output csv file
        dict_writer.writeheader()
        # Read each row of the input csv file as dictionary
        for row in dict_reader:
            # Modify the dictionary / row by passing it to the transform function (the callback)
            transform_row(row, dict_reader.line_num)
            # Write the updated dictionary or row to the output file
            dict_writer.writerow(row)

def main():
    print('Use DictReader DictWriter to add a column with same values to an existing csv')
    header_of_new_col = 'Address'
    default_text = 'Some_Text'
    # Add a Dictionary as a column in the existing csv file using DictWriter class
    add_column_in_csv_2('C:\Users\Okocha Nwoke\Documents\HNG\CHIP\Naming.csv', 'output_7.csv',
                        lambda row, line_num: row.update({header_of_new_col: default_text}),
                        lambda field_names: field_names.append(header_of_new_col))
if __name__ == '__main__':
    main()