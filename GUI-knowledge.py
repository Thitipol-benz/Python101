from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรเเกรม
GUI.title('โปรเเกรมบันทึกข้อมูล') #นี่คือชื่อของโปรเเกรม
GUI.geometry('500x400')

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

#################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showerror('เงินในบัญชี',text)

FB1 = LableFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
################


GUI.mainloop()
