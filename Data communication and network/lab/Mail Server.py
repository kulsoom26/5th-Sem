import smtplib
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 80) #smtp server and port no #smtp.world4you.com
server.ehlo() #to start the process
#encrypt password in txt file and the decrypt it
with open('password.txt','r') as f:
    password = f.read()

server.login('kulsoomkhurshid026@gmail.com', password) #to login in to your serverinto the smtp serverinto your mail account to create the message
#define msg as my multi-part
msg = MIMEMultipart()
msg['From'] = 'kulsoom'
msg['To'] = 'kulsoomkhurshid26@gmail.com'
msg['Subject'] = 'Demo'

#write the message in the txt file and import it
with open('mail.txt','r') as f:
    message = f.read()

text = msg.as_string()
server.sendmail('kulsoomkhurshid026@gmail.com','kulsoomkhurshid26@gmail.com')