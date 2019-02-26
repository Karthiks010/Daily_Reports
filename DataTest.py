import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromaddr = "karthiks010vs@gmail.com"
toaddr = "karthiks010vs@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("karthik@gmail.com", "********")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)


































#server = smtplib.SMTP('smtp.gmail.com', 587)
#Send the mail
#msg = "Hello!" # The /n separates the message from the headers
#server.sendmail("karthiks010vs@gmail.com", "karthiks010vs@gmail.com", msg)


