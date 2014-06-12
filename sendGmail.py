import smtplib  # simple main transfer protocol lib 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr='inimitableharish@gmail.com'
toaddr='inimitableharish@gmail.com'
username='inimitableharish'
password='meraPassword'
text=' Hey this mail is send from sendmail '

msg=MIMEMultipart()   #creating multipart message 
msg['From']=fromaddr      #actually filling the part ,using dict notation
msg['TO']=toaddr
msg['Subject']='Test'
msg.attach(MIMEText(text))
server=smtplib.SMTP('smtp.gmail.com:587')   #connecting to the server 
server.ehlo()   #establish connection with server 
server.starttls()  # use encryption as pass and user is text
server.ehlo()
server.login(username,password)   # login
server.sendmail(fromaddr,toaddr,msg.as_string())  #send the mail built in function in MIMEMultipart to convert msg into string
server.quit()
