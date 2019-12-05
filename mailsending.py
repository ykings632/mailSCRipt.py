import smtplib , webbrowser
def get_mail():
	servicesAvailable=['hotmail','gmail','yahoo','outlook']
	while True:
			mail_id = input("Enter E-mail : ")
			if '@' in mail_id and '.com' in mail_id:
				#shahzanhasan@gmail.com
				symbol_pos = mail_id.find('@')
				dotcom_pos = mail_id.find('.com')
				sp = mail_id[symbol_pos+1:dotcom_pos]
				if sp in servicesAvailable:
					return mail_id , sp
					# ( 123@gmail.com ,  gmail )
					break
				else:
					print("Enter valid Email " + sp)
					print("Enter valid Email " + servicesAvailable)
					continue
			else:
				print("Enter Valid Email Again")
				continue

def set_smtp_domain(serviceProvider):
	if serviceProvider == 'gmail':
		return 'smtp.gmail.com'
	elif serviceProvider == 'yahoo':
		return 'smtp.yahoo.com'
	elif serviceProvider == 'hotmail' or serviceProvider == 'outlook':
		return 'smtp-mail.outlook.com'

print("Start Mail sending without opening any browser ")
print("Enter mail and password : ")
e_mail , serviceProvider = get_mail()
password = input("password : ")

while True:
		try:
			smtpDomain = set_smtp_domain(serviceProvider)
			connection = smtplib.SMTP(smtpDomain , 587)
			connection.ehlo()
			connection.starttls()
			connection.login(e_mail , password)
		except:
			if serviceProvider == 'gmail':
				print("login unsuccessfull")
				print("Please Less Secure Apps in your Chrome Browser or Login With correct Email or password")
				e_mail , serviceProvider = get_mail()
				password = input("password : ")
				continue
			else:
				print("login unsuccessfull")
				print("re-type password and email")
				e_mail , serviceProvider = get_mail()
				continue
		else:
			print("Login Successfull")
			break


print("Type receivers email")
receiverAddress , receiverSP = get_mail()
print("Enter Subject And Message ")
Subject = input("Subject : ")
Message = input("Message : ")
connection.sendmail(e_mail , receiverAddress , ("Subject: " + str(Subject) + '\n\n' + str(Message)))
print("Successfully Send Message")
connection.quit()