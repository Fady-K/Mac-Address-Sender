# Mac-Address-Sender
## Description:
This is a simple python program, aiding in Fetching the Mac Address of the pc where the Mac-sender.py is being operated, after acquiring the Mac Address, the program asks the user to enter an email (Gmail only) to send the Mac Address to it.

### MORE INFO
The user is asked to enter a valid email using a GUI made with Tkinter.
Mac-Address is fetched via importing getnode() from UUID lib, sent to the provided email via smtplib which a built-in lib in python

### All included libraries
smtplib, Tkinter, UUID

