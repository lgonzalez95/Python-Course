"""
file.read([size])
file.readline([size])
file.readlines([sizehint]): Reads all lines and adds them to a list
file.write(str)
file.writelines(sequence)
file.flush()
file.close()
readable()
writable()
file.tell()
file.seek(offset[,whence])
"""

# file = open('properties.txt', 'r')
# print(file.name)
# print(file.mode)
# print(file.closed)

# file = open('properties.txt', 'r')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readlines(), end='')

file = open('properties.txt', 'w')
lines = ['One line\n', 'Another line\n', 'Last line\n']
file.writelines(lines)
