import csv
html_output = ""
names = []
##reader method
# with open("patrons.csv") as pat_file:
        ##reader turns each line into a list(array)
#     pat_reader = csv.reader(pat_file)
#     next(pat_reader)
#     next(pat_reader)
#     for line in pat_reader:
#         if(line[0]=="No Reward"):
#             break
#         # print(line[0],line[1])
#         names.append(f"{line[0]} {line[1]}")
#         # print(f"{line[0]} {line[1]}")
        
#     print(len(names))
#     html_output += f"There are {len(names)} participants.  Thank you!!"

#     html_output += f"\n<ul>"
#     for name in names:
#         # print (name)
#         html_output += f"\n\t<li>{name}</li>"

#     html_output += "\n</ul>"

#     print(html_output)


    #DictReader method
with open("patrons.csv") as pat_file:
    #instead of turning each line into a list, the DictReader turns each line into a dictionary
    pat_reader = csv.DictReader(pat_file)
    next(pat_reader)
    for item in pat_reader:
        print(item)
        print()

    #only one of these needed because DictReader eliminates the header row
#     next(pat_reader)
#     for line in pat_reader:
#         if(line["FirstName"]=="No Reward"):
#             break
#         # print(line[0],line[1])
#         names.append(f'{line["FirstName"]} {line["LastName"]}')
#         # print(f"{line[0]} {line[1]}")
#     # print(names)  
#     # print(len(names))
# html_output += f"There are {len(names)} participants.  Thank you!!"

# html_output += f"\n<ul>"
# for name in names:
#     # print (name)
#     html_output += f"\n\t<li>{name}</li>"

# html_output += "\n</ul>"
# print(html_output)