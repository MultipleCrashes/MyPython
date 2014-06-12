import imaplib # impap is internet standard for reading email 

mailserver=imaplib.IMAP4_SSL('imap.gmail.com', 993)
username='inimitableharish'
password='ChangeThisAndPutYourPassword'
mailserver.login(username,password)

status, count=mailserver.select('Inbox')   # count will contain number of email
status, data=mailserver.fetch(count[0],'(UID BODY[TEXT])')    # retrive email using fetch item 
                      # body of the email message to be displayed ,by uid body 

print data[0][1]

mailserver.close()
mailserver.logout()
