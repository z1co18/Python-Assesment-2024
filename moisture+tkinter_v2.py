import tkinter as tk
from gpiozero import DigitalInputDevice
import smtplib

# Email server connection setup
email = "joshuazicofowler@gmail.com" # Change based on user
receiver_email = "z1cocs18@gmail.com" # Change based on user
subject = "Water" # Email subject
message = "Your plant needs watering!" # Email Body
text = "Subject: {}\n\n{}".format(subject, message) # What variables make up the content in email
smtp_server = "smtp.gmail.com" # Change if receiver and sender email suffix is different
smtp_port = 587 # Pre-definded value, DO NOT CHANGE
password = "ricuzbfqhiozrscx"  # Get this from google

# GPIO setup for moisture sensor
d0_input = DigitalInputDevice(21)

# Track if email was already sent and auto-check is enabled
email_sent = False
auto_check_enabled = False

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
                print("Failed to send email: " + str(e))
        else:
            print("Email already sent.")
    else:
        result_label.config(text='Plant moisture status: \n Moist \n \n Your plant is ok for now', fg='green')
        email_sent = False  # Reset if the moisture level is back to normal

# Function to enable or disable auto-check
def toggle_auto_check():
    global auto_check_enabled
    if auto_check_enabled:
        auto_check_enabled = False
        auto_button.config(text="Enable Auto Check")
        root.after_cancel(auto_check_id)  # Stop the auto-check loop
    else:
        auto_check_enabled = True
        auto_button.config(text="Disable Auto Check")
        auto_check_moisture()  # Start the auto-check loop

# Function for automatically checking moisture periodically
def auto_check_moisture():
    global auto_check_id
    if auto_check_enabled:
        check_moisture()  # Check the moisture
        auto_check_id = root.after(3000, auto_check_moisture)  # Re-check every 3 seconds

# Tkinter UI setup
root = tk.Tk()
root.title("Moisture Checker")

# Label to display the result
result_label = tk.Label(root, text="Plant moisture status: \n \n Unchecked", font=('Helvetica', 14),)
result_label.pack(pady=20)

# Button to trigger the moisture check
check_button = tk.Button(root, text="Check Moisture", command=check_moisture, font=('Helvetica', 12), bg='blue', fg='white')
check_button.pack(pady=20)

# Button to toggle the auto-check feature
auto_button = tk.Button(root, text="Enable Auto Check", command=toggle_auto_check, font=('Helvetica', 12), bg='green', fg='white')
auto_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()