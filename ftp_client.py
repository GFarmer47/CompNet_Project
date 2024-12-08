from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)  # Enable verbose output
ftp.connect('192.168.1.105', 21)
ftp.login('myuser', 'mypass')

# Define a callback function to print each line
def print_line(line):
    print(line)

ftp.retrlines('LIST', callback=print_line)

ftp.quit()
