import csv

# with open("people.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     #next(csv_reader)  this skips the first line of index titles.  to skip more than more just copy and paste the function how ever many lines you want to skip
#     for line in csv_reader:
#         #each line printed is an array of the row
#         print(line)
#         print(f"First: {line[0]}.  Last: {line[1]}.  Email: {line[2]}")


#must stay within scope of context manager because the file is closed outside the scope
with open("people.csv", "r") as file1:
    csv_reader = csv.reader(file1)
    print(csv_reader) #this prints the location in memory
    print(list(csv_reader)) #this prints a list of rows- each row is another list

    with open("newPeople.csv", "w") as file2:
        csv_writer = csv.writer(file2, delimiter="\t")
        for line in csv_reader:
            csv_writer.writerow(line)
        
 