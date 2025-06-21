"""
remove_duplicates.py
By: Konrad Jeziorski
Date: 12/11/2022
"""
# Opens the previously created nodes.csv file through the output of the running code, 
# checks each of its rows and removes their duplicates from the list

# Import for processing files from different places in the system
import os.path
def remove_duplicates_from_CSV():
    newrows = []
    directory = './Results/'
    filename = "nodes.csv"
    file_path = os.path.join(directory, filename)
    rows = open(file_path).read().split('\n')
    for row in rows:
        if row not in newrows:
            newrows.append(row)

    f = open(file_path, 'w')
    f.write('\n'.join(newrows))
    f.close()


remove_duplicates_from_CSV()