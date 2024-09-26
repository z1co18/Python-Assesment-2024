from gpiozero import DigitalInputDevice
import time
import smtplib

# Predefined email addresses and server settings
email = "joshuazicofowler@gmail.com"
receiver_email = "z1cocs18@gmail.com"
subject = "Water"
message = "Your plant needs watering!"
text = "Subject: {}\n\n{}".format(subject, message)
smtp_server = "smtp.gmail.com"
smtp_port = 587
password = "ricuzbfqhiozrscx"  # Replace with your actual app-specific password

# GPIO setup for moisture sensor
d0_input = DigitalInputDevice(21)

# Track if email was already sent
email_sent = False

# Start monitoring moisture level
while True:
    if d0_input.value:  # Plant needs watering
        print('You need to water your plant \n')

        if not email_sent:  # Send email only if not already sent
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, receiver_email, text)
            print("Email has been sent to " + receiver_email)
            email_sent = True  # Prevent duplicate emails
            server.quit()
       
        time.sleep(10)  # Wait 10 seconds before checking moisture level again
    else:
        print('Moisture level is sufficient. No need to water the plant. \n')
        email_sent = False  # Reset if the moisture level is back to normal
 
    time.sleep(3)  # Continue monitoring every 3 seconds