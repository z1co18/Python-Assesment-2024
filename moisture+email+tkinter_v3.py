import tkinter as tk
from tkinter import messagebox
from gpiozero import DigitalInputDevice
import smtplib

# Email server connection setup
email = "joshuazicofowler@gmail.com"  # Change based on user
receiver_email = "z1cocs18@gmail.com"  # Change based on user
subject = "Water"  # Email subject
message = "Your plant needs watering!"  # Email Body
text = "Subject: {}\n\n{}".format(subject, message)  # What variables make up the content in email
smtp_server = "smtp.gmail.com"  # Change if receiver and sender email suffix is different
smtp_port = 587  # Pre-defined value, DO NOT CHANGE
password = "ricuzbfqhiozrscx"  # Get this from google

# GPIO setup for moisture sensor
d0_input = DigitalInputDevice(21)

# Track if email was already sent and auto-check is enabled
email_sent = False
auto_check_enabled = False
auto_check_id = None

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

# Function to check the number of plants and enable/disable features
def check_plants():
    try:
        num_plants = int(plant_entry.get())
        if num_plants == 1:
            check_button.config(state='normal')
            auto_button.config(state='normal')
            result_label.config(text="Plant moisture status: \n \n Unchecked", fg='black')
        else:
            check_button.config(state='disabled')
            auto_button.config(state='disabled')
            result_label.config(text="Error: \n \n You can only monitor a single plant.", fg='red')                     
            messagebox.showerror("Invalid Input", "You can only use this program to monitor a single plant.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of plants to monitor.")

# Tkinter UI setup
root = tk.Tk()
root.title("Moisture Checker")

# Label to ask how many plants are being monitored
plant_label = tk.Label(root, text="How many plants are you monitoring? \n \n Input a valid number of \n plants to be watered to continue", font=('Helvetica', 14))
plant_label.pack(pady=10)

# Entry field to input the number of plants
plant_entry = tk.Entry(root, font=('Helvetica', 12))
plant_entry.pack(pady=10)

# Button to submit the number of plants
submit_button = tk.Button(root, text="Submit", command=check_plants, font=('Helvetica', 12))
submit_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Plant moisture status: \n \n Unchecked", font=('Helvetica', 14), fg='black')
result_label.pack(pady=20)

# Button to trigger the moisture check (initially disabled)
check_button = tk.Button(root, text="Check Moisture", command=check_moisture, font=('Helvetica', 12), bg='blue', fg='white', state='disabled')
check_button.pack(pady=20)

# Button to toggle the auto-check feature (initially disabled)
auto_button = tk.Button(root, text="Enable Auto Check", command=toggle_auto_check, font=('Helvetica', 12), bg='green', fg='white', state='disabled')
auto_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()