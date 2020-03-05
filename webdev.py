import csv

def main():
  
    # line_count = 0
    # with open("webdev.csv", "r") as csv_file:
    #     csv_read = csv.reader(csv_file, delimiter=",")
        
    #     for row in csv_read[5]:
    #         print(row)

                

    with open("webdev.csv", "r") as data_csv:
        data = csv.reader(data_csv)
        for _ in range(12):  # skip the first 500 rows
            next(data)
 
        for row in data:
            print(row)





if __name__ == "__main__":
    main()
