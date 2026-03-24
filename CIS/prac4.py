import smtplib
from cryptography.fernet import Fernet

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "SENDER_EMAIL"
smtp_password = "SENDER_PASSWORD"

sender = "SENDER_EMAIL"
recipient = "RECEIVER_EMAIL"

subject = "Testing Email"
message = "CIS Practical 4"

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_message = cipher.encrypt(message.encode("UTF-8"))
msg = f"From:{sender}\nTo:{recipient}\nSubject:{subject}\n\n{encrypted_message.decode('UTF-8')}"

with smtplib.SMTP(smtp_server,smtp_port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(smtp_username,smtp_password)
    smtp.sendmail(sender, recipient, msg)

print("Email sent successfully")