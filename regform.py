from tkinter import *
root = tk()
root.geometry("500X300")

def getvals():
    print("Accepted")

Label(root, text="python registration form" , font="ar 15 bold").grid(row=0,column=3)

root.mainloop()

name= Label(root, text="name")
phone= Label(root, text="phone")
gender= Label(root, text="gender")
emergency= Label(root, text="emergency")
payment mood= Label(root, text="payment mood")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment mood.grid(row=5, column=2)

nameValue= stringvar
phoneValue= stringvar
genderValue= stringvar
emergencyValue= stringvar
paymentmoodValue= stringvar
chechValue= intvar

nameentry = Entry(root, textvariable = nameValue)
phoneentry = Entry(root, textvariable = phonneValue)
genderentry = Entry(root, textvariable = genderValue)
paymentmoodentry = Entry(root, textvariable = paymentmoodValue)
emergencyentry = Entry(root, textvariable = emergencyValue)

nameentry.grid(row=1,column=2)
phoneentry.grid(row=2,column=2)
genderentry.grid(row=3,column=2)
emergencyentry.grid(row=4,column=2)
paymentmoodentry.grid(row=5,column=2)

checkbtn = checkbutton(text="remember me" Variable=checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="submit", command=getvals).grid(row=7,column=3)



root.mainloop()