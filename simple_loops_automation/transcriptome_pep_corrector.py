"""script to correct the modified transcriptome pep results file since it includes several repeated headers,
which don't allow for the pandas library to read it properly and filter out the q-value > 0.01"""

import csv

def remove_repeated_header_lines(file_path, column_index, starting_letters): #where "starting_letters" refers to the headers to be removed
    lines = [] #store the lines from the CSV file
    #initialize a flag to keep track of whether the first matching line has been encountered or not
    first_line_encountered = False
    with open(file_path, 'r') as file:
        #create a CSV reader object
        reader = csv.reader(file)
        for row in reader:
            if row[column_index].startswith(starting_letters):
                if not first_line_encountered: #if it matches the letters and it's the first line, add to list
                    lines.append(row)
                    first_line_encountered = True
            else:
                lines.append(row) #if it doesn't match, add to list

    with open(file_path, 'w', newline='') as file:
        #create a CSV writer object
        writer = csv.writer(file)
        writer.writerows(lines)

file_path = "/home/adriana/tcc/smorfs/percolator/transcriptome/modified/pep_results.txt"
column_index = 0
starting_letters = 'PSMId'

remove_repeated_header_lines(file_path, column_index, starting_letters)