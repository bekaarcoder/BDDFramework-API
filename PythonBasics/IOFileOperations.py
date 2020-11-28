# file = open('text.txt')

# print(file.read())
# read all the characters in a file

# print(file.read(3))
# read the number of characters in a file passed as a parameter

# print(file.readline())
# read the single line at a time in the file

# printing all the lines in a file using readline
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# print(file.readlines())
# readlines method store all the lines in a file in a python list

# printing all the lines in a file using readlines
# lines = file.readlines()
# for line in lines:
#     print(line)
# file.close()


# writing to a file
with open('text.txt', 'r') as reader:
    lines = reader.readlines()
    with open('text.txt', 'w') as writer:
        for line in reversed(lines):
            writer.write(line)