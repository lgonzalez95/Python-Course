# with open('my-binary-data.txt', 'wb') as file:
#     file.write('abcdefghi'.encode())

# seek to move the cursor on a file, to be able to read from different places on the file
# we must specify the offset and from where we want to read: 0: from the beginning
# 1: from current position, 2: from the end
with open('my-binary-data.txt', 'rb') as file:
    print(file.read(2).decode())
    file.seek(-3, 2)
    print(file.read(1).decode())
    print(file.tell())


with open('my-binary-data.txt', 'rb') as file:
    print(file.read(5).decode())
    file.seek(-3, 1)
    print(file.read(1).decode())
    print(file.tell())