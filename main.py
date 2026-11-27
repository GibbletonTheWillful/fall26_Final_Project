import smtplib
email = input("SENDER EMAIL: ")
password = input("APP PASSWORD: ")
receiver_email  = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email,password)
server.sendmail(email,receiver_email,text)

print(f"email has been sent to {receiver_email}")
