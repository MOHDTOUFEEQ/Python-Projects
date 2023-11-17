#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:

    def __init__(self, master):    
        master.title('California Feedback')
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.logo = PhotoImage(file='C:/Users/toufe/Downloads/tour_logo.gif')
        self.h1 = ttk.Label(self.frame_header, image=self.logo)
        self.h2 = ttk.Label(self.frame_header, text='Feedback',font=('Arial',15,'bold'))
        self.h3 = ttk.Label(self.frame_header, text='How was your Experience')

        self.h1.grid(row=0,column=0,rowspan=2,columnspan=2,padx=10)
        self.h2.grid(row=0,column=5,rowspan=2,padx=10)
        self.h3.grid(row=1,column=5,rowspan=2,padx=10,pady=5)
        self.name = ttk.Label(self.frame_header,text='Name:',font=('Arial',10,'bold'))
        self.Email = ttk.Label(self.frame_header,text='Email:',font=('Arial',10,'bold'))
        self.name.grid(row =3,column=0)
        self.Email.grid(row =3,column=5)
        self.Name_entry = ttk.Entry(self.frame_header,width=20)
        self.Email_entry = ttk.Entry(self.frame_header,width=20)
        self.Name_entry.grid(row = 4,column=0,columnspan=4)
        self.Email_entry.grid(row = 4,column=4,columnspan=4)
        self.comment = ttk.Label(self.frame_header,text='Comments:')
        self.comment.grid(row=5,column=0)
        self.text =Text(self.frame_header,height=8,width=37)
        self.text.grid(row = 6,column=0,columnspan=10,padx=20,pady=20)
        self.submit = ttk.Button(self.frame_header,text='Submit',command= lambda: self.submit1())
        self.clear = ttk.Button(self.frame_header,text='Clear',command= lambda: self.clear1())
        self.clear.grid(row=7,column=1,columnspan=2,ipadx=2.5,ipady=2.5)
        self.submit.grid(row=7,column=5,columnspan=2,ipadx=2.5,ipady=2.5)

    def submit1(self):
        print("Done")
        print("Name : {}".format(self.Name_entry.get()))
        print("Email : {}".format( self.Email_entry.get()))
        print("feedback:{}".format(self.text.get(1.0,'end')))
        self.clear1()
        messagebox.showinfo(title='feedback',message='thankyou for your comment')
    def clear1(self):
        self.Name_entry.delete(0,'end')
        self.Email_entry.delete(0,'end')
        self.text.delete(1.0,'end')
def main():            
    root = Tk()
    style = ttk.Style()
    root.config(background='#e1db89')
    style.configure('TButton',background='#e1db89')
    style.configure('TLabel',background='#e1db89')
    style.configure('TFrame',background='#e1db89')
    root.geometry('360x360+500+200')
    root.maxsize('360','360')
    root.minsize('360','360')
    feedback = Feedback(root)
    root.mainloop()
    ttk.Frame
if __name__ == "__main__": main()
