import csv

csv_filename='cereal_grains.csv'

with open(csv_filename,encoding='utf-8',newline='') as csv_file:
    # generally csv file consider all all string field  but here we are telling reader object that 
    #convert non numberic value to the float
    # but it has limiation 1) string value need to be quated 2) if want to keep int value as it is , it does not do this
    reader=csv.reader(csv_file,quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)