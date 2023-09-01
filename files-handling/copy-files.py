file = open('extracted-data/python-logo.png', 'rb')
data = file.read()
copy_file = open('extracted-data/python-logo-copy.png', 'wb')
copy_file.write(data)

file.close()
copy_file.close()