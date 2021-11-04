#from typing import cast

#Add our depencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

# #Print each row in teh CSV file.
#     for row in file_reader:
#         print(row)




