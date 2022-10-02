import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your Name here' #<- This is where you would put your name
email['to'] = 'Whoareyoursendingthisto@gmail.com' #<-This is where you would put the email recipient
email['subject'] = 'Enter a subject here' #<- This is where you would put the subject of the email

email.set_content(html.substitute({'name': 'Putyournamehere'}), 'html') #Replace "Putyournamehere with your actual name"

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('youremail@here', 'enteryourpassword')#post your email and password here
	smtp.send_message(email)
	print('All done') #You can change this to what everyou would like if you want.