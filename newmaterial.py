import csv

with open ("oldest.csv", "r") as data:
    old_data = csv.reader(data)
    
    with open ("newest.csv", "r") as data:
        new_data = csv.reader (data)
        
        for oldest_row, newest_row in zip(old_data, new_data):
            #print(old, b)#
            
            oldest_row_length = len (oldest_row)
            newest_row_length = len (newest_row)
            
            if oldest_row_length > newest_row_length:
                oldest_row = oldest_row[0:newest_row_length]
            else:
                newest_row = newest_row[0:oldest_row_length]
            print (len(oldest_row), len(newest_row))
            
            stitchedString = ""
            for oldest_cell, newest_cell in zip (oldest_row, newest_row):
                #print (oldest_cell, "|", newest_cell)#
                stitchedString = stitchedString + oldest_cell.strip() + " " + newest_cell.strip() + " "
            print (stitchedString)