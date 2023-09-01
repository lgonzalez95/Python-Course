# r: Read a file
file = open('my-data.txt', 'r')
data_file = file.read(6)  # Read X characters, if not specified everything is read
print(data_file)
file.close()

# w: to write a new file, if it exists it overwrites the content if not, it creates a new file
new_file = open('new_fileTwo.txt', 'w')
new_file.write("Hello!\n")
new_file.write("How are you?\n")
new_file.close()

# a: to append content to a new file, the file has to exists
new_file = open('new_file.txt', 'a')
new_file.write('Old content was not overwritten!\n')
new_file.close()

# r+: to read as well as append:
existing_file = open('new_file.txt', 'r+')
print(existing_file.read())
existing_file.write("New content\n")
existing_file.close()
existing_file = open('new_file.txt', 'r+')
print(existing_file.read())
# w+: to write and read data into a file
# a+: to append and read
# x: to create a new file, it must not exist
