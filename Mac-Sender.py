import os
from uuid import getnode
import smtplib
from tkinter import *


# initialize a root
root = Tk()

# add title to the root (program name)
root.title("Mac-Sender")

# add the root size of pixels
root.geometry("500x400")

# add root background color
root.config(background="#dae6f6")

# main functions


# this function returns the mac of instant device in hex form
def get_mac():
    mac = getnode()
    return hex(mac)


# return the the Main user name of the instant pc
def get_pc_user_name():
    return os.getlogin()


# this function checks if a functions works then prints label of the result
def check_function(is_it_working):
    if is_it_working:
        message = Label(root, text="Done!!".upper(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#000000")
    else:
        message = Label(root, text="Faild!!".upper(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#000000")
    # place the message
    message.place(x=220, y=300)

    # destroy the message after 3 seconds from being displayed
    root.after(3000, message.destroy)


def send_email(subject, body, sender, password, reciver):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()         # to identified to mail service
            smtp.starttls()     # this encrypts the traffic between us and the server
            smtp.ehlo()         # to identified us to mail service again after encrypting the traffic

            # Now we are encrypted and identified to the mail service

            # login
            smtp.login(sender, password)    # password is generated from two-step-verification in Gmail security

            # send the mail
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(sender, reciver, msg)
            check_function(True)

    except:
        check_function(False)


heading1 = Label(root, text="Send Mac-Address To:".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading1.place(x=122, y=150)

# add the entry
enter_text1 = Entry(root, justify="center", width=20, font=("timesnewroman", 15), bg="white", border=2)
enter_text1.place(x=150, y=200)


# parameters of send_email function
subject = f"Mac Address From: {get_pc_user_name()}"
body = f"Hey Remon!\n\nGetting The Mac Address Of {get_pc_user_name()} WAS A success !!\n\nMac-Address: {get_mac()}\n\nThanks!"
sender = "macaddresssender@gmail.com"
password = "amfhzdjssbsvwqxs"


# note: the receiver will be obtained from the input and then passed to the function parameters directly (look button)


# the button
button2 = Button(root, text="Send".upper(), font=("timesnewroman", 15, "bold"), fg="white", bg="gray15", command=lambda:send_email(subject, body, sender, password, enter_text1.get()))
button2.place(x=225, y=250)


# added the root mainloop
root.mainloop()





