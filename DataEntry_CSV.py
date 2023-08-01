import csv
import os

file_name = 'tryfile.txt'
file_exists = os.path.isfile(file_name)
headers = ["SN", "Name", "Age", "Add"]

# If the file already exists, get the data from the file
if file_exists and os.path.getsize(file_name) > 0:  # Check if the file is not empty
    with open(file_name, 'r', newline='') as entryfile:
        csv_reader = csv.reader(entryfile)
        data = list(csv_reader)
    try:
        last_row = data[-1]  # Get the last row of the file
        last_sn = int(last_row[0])  # Extract the SN value from the last row
    except IndexError:
        last_sn=0
else:
    last_sn = 0  # If the file is empty or does not exist, start SN from 0


n = int(input("Enter How many Data You want to Add: "))

with open(file_name, 'a', newline='') as entryfile:
    csv_writer = csv.writer(entryfile)

    if not file_exists or os.path.getsize(file_name) == 0:  # If the file is empty or does not exist, write the column headers
            csv_writer.writerow(headers)   

    for i in range(n):
        last_sn += 1  # Increment the SN for each new data entry
        Name = input("Enter Name: ")
        Age = input("Enter Age: ")
        Add = input("Enter Address: ")

        csv_writer.writerow([last_sn, Name, Age, Add])
