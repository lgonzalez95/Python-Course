from zipfile import *

#
# zipped_file = ZipFile('compress_data.zip', 'w', ZIP_DEFLATED)
# zipped_file.write('python-logo.png')
# zipped_file.write('python-logo-copy.png')
# zipped_file.close()

with ZipFile('compress_data.zip', 'r') as unzipped_file:
    unzipped_file.extractall('data')
    unzipped_file.close()
