from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('192.168.1.105', 21)
ftp.login('myuser', 'mypass')

# Upload a test file
with open('testfile.txt', 'w') as f:
    f.write('This is a test file.')

with open('testfile.txt', 'rb') as f:
    ftp.storbinary('STOR testfile.txt', f)

# List files with a custom callback
def print_line(line):
    print(line)

ftp.retrlines('LIST', callback=print_line)

ftp.quit()
