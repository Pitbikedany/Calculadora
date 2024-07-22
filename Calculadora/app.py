import tkinter as tk
from tkinter import *

def button_click(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equal():
    try:
        inputs = input_text.get()
        result = str(eval(inputs))
        input_text.set(result)
    except:
        input_text.set('ERRO')

def clear():
    global expression
    expression = ""
    input_text.set('')

root = Tk()
root.title('Calculadora')
root.configure(background="white")
root.iconbitmap('img/icon.ico')
root.geometry('320x471')

expression = ''
input_text = StringVar()
input_frame = tk.Frame(root,bg="white")
input_frame.pack()

input_field = tk.Entry(input_frame,bg="white" ,textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=24, borderwidth=0)
input_field.grid(row=0, column=0)
input_field.pack(padx=0,pady=5)

btns_frame = tk.Frame(root,bg="white")
btns_frame.pack()

btn_c = Button(btns_frame,bg="orange",height=5,width=10,text='C', command=clear)
btn_c.pack(side=LEFT, padx=0,pady=0)
btn_x = Button(btns_frame,bg="orange",height=5,width=10,text='TBD')
btn_x.pack(side=LEFT, padx=0,pady=0)
btn_per = Button(btns_frame,bg="orange",height=5,width=10,text='%',command=lambda: button_click('%'))
btn_per.pack(side=LEFT, padx=0,pady=0)
btn_bar = Button(btns_frame,bg="orange",height=5,width=10,text='/',command=lambda: button_click('/'))
btn_bar.pack(side=LEFT, padx=0,pady=0)


btns_frame1 = tk.Frame(root)
btns_frame1.pack()

btn_7 = Button(btns_frame1,height=5,width=10,text='7',command=lambda: button_click(7))
btn_7.pack(side=LEFT, padx=0,pady=0)
btn_8 = Button(btns_frame1,height=5,width=10,text='8',command=lambda: button_click(8))
btn_8.pack(side=LEFT, padx=0,pady=0)
btn_9 = Button(btns_frame1,height=5,width=10,text='9',command=lambda: button_click(9))
btn_9.pack(side=LEFT, padx=0,pady=0)
btn_x = Button(btns_frame1,bg="orange",height=5,width=10,text='x',command=lambda: button_click('*'))
btn_x.pack(side=LEFT, padx=0,pady=0)

btns_frame2 = tk.Frame(root)
btns_frame2.pack()

btn_4 = Button(btns_frame2,height=5,width=10,text='4',command=lambda: button_click(4))
btn_4.pack(side=LEFT, padx=0,pady=0)
btn_5 = Button(btns_frame2,height=5,width=10,text='5',command=lambda: button_click(5))
btn_5.pack(side=LEFT, padx=0,pady=0)
btn_6 = Button(btns_frame2,height=5,width=10,text='6',command=lambda: button_click(6))
btn_6.pack(side=LEFT, padx=0,pady=0)
btn_x = Button(btns_frame2,bg="orange",height=5,width=10,text='-',command=lambda: button_click('-'))
btn_x.pack(side=LEFT, padx=0,pady=0)

btns_frame3 = tk.Frame(root)
btns_frame3.pack()

btn_1 = Button(btns_frame3,height=5,width=10,text='1',command=lambda: button_click(1))
btn_1.pack(side=LEFT, padx=0,pady=0)
btn_2 = Button(btns_frame3,height=5,width=10,text='2',command=lambda: button_click(2))
btn_2.pack(side=LEFT, padx=0,pady=0)
btn_3 = Button(btns_frame3,height=5,width=10,text='3',command=lambda: button_click(3))
btn_3.pack(side=LEFT, padx=0,pady=0)
btn_plus = Button(btns_frame3,bg="orange",height=5,width=10,text='+',command=lambda: button_click('+'))
btn_plus.pack(side=LEFT, padx=0,pady=0)

btns_frame4 = tk.Frame(root)
btns_frame4.pack()

btn_0 = Button(btns_frame4,height=5,width=10,text='0',command=lambda: button_click(0))
btn_0.pack(side=LEFT, padx=0,pady=0)
btn_dot = Button(btns_frame4,height=5,width=10,text='.',command=lambda: button_click('.'))
btn_dot.pack(side=LEFT, padx=0,pady=0)
btn_bar = Button(btns_frame4,height=5,width=10,text='TBD')
btn_bar.pack(side=LEFT, padx=0,pady=0)
btn_equal = Button(btns_frame4,bg="orange",height=5,width=10,text='=', command=equal)
btn_equal.pack(side=LEFT, padx=0,pady=0)


root.mainloop()