import csv 
 
filename = "Text messages and depression.csv"
  
outfile = 'PHQ.csv'

# initializing the titles and rows list 
fields = [] 
rows = [] 

fields_new = ['What is your age?','How many Text Messages do you receive in a day?','How many social media and messaging applications do you use?','PHQ']
rows_new = []

# reading csv file 
with open(filename, encoding='utf-8') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader)
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

for row in rows:
    PHQ = 0
    temp = []
    for i in row[-9:]:
        if i.lower() == 'not at all':
            PHQ += 0
        elif i.lower() == 'several days':
            PHQ += 1
        elif i.lower() == 'more than half the days':
            PHQ += 2
        elif i.lower() == 'nearly every day':
            PHQ += 3
    temp.append(row[1])
    temp.append(row[2])
    temp.append(row[3])
    temp.append(PHQ)
    rows_new.append(temp)

with open(outfile, 'w+') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields_new) 
      
    # writing the data rows 
    csvwriter.writerows(rows_new)        
