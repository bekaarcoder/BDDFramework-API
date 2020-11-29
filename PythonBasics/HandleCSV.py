import csv

# reading csv files
# with open('userinfo.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     # print(list(csv_reader))
#     name = []
#     email = []
#     for row in csv_reader:
#         name.append(row[0])
#         email.append(row[1])
#
# print(name)
# print(email)

# writing in csv files
with open('userinfo.csv', 'a') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(['Jane Doe', 'jane@example.com', '123-123-123', 'Fake Street 321'])