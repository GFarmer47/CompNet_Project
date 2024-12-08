import smtplib
from email.mime.text import MIMEText

smtp_server = '192.168.1.106'
smtp_port = 25

from_addr = 'sender@example.com'
to_addr = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email.'

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = to_addr

server = smtplib.SMTP(smtp_server, smtp_port)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

print("Email sent successfully.")
