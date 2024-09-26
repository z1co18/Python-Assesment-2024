import tkinter as tk
from gpiozero import DigitalInputDevice
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

# Function to check moisture and send email if necessary
def check_moisture():
    global email_sent
    if d0_input.value:  # Plant needs watering
        result_label.config(text='Plant moisture status: \n Dry \n \n Water your plant', fg='red')

        if not email_sent:  # Send email only if not already sent
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, receiver_email, text)
                print("Email has been sent to " + receiver_email)
                email_sent = True  # Prevent duplicate emails
                server.quit()
            except Exception as e:
                print("Failed to send email: " + e)
        else:
            print("Email already sent.")
    else:
        result_label.config(text='Plant moisture status: \n Moist \n \n Your plant is ok for now', fg='green')
        email_sent = False  # Reset if the moisture level is back to normal

# Tkinter UI setup
root = tk.Tk()
root.title("Moisture Checker")


# Label to display the result
result_label = tk.Label(root, text="Plant moisture status: \n \n Unchecked", font=('Helvetica', 14),)
result_label.pack(pady=20)

# Button to trigger the moisture check
check_button = tk.Button(root, text="Check Moisture", command=check_moisture, font=('Helvetica', 12), bg='blue', fg='white' )
check_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()