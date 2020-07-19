import tkinter as t 
root=t.Tk()
root.title("Calculator")
root.geometry("315x300")
root.maxsize(315,300)
root.minsize(315,300)

#Entry Widget
Entry_Widget=t.Entry(root,width=50,borderwidth=5)

# Functions
first=0
second=0
sign=''
def button_clicked(number):
    first=Entry_Widget.get()
    Entry_Widget.delete(0,'end')
    Entry_Widget.insert(0,str(first)+str(number))
    # first=int(Entry_Widget.get())
def add():
    global first
    global sign
    first=Entry_Widget.get()
    sign='+'
    Entry_Widget.delete(0,'end')
    

def sub():
    global first
    global sign
    first=Entry_Widget.get()
    sign='-'
    Entry_Widget.delete(0,'end')
    

def mult():
    global first
    global sign
    first=Entry_Widget.get()
    sign='*'
    Entry_Widget.delete(0,'end')
    

def div():
    global first
    global sign
    first=Entry_Widget.get()
    sign='/'
    Entry_Widget.delete(0,'end')
    

def intequal():
    if sign=='+':
        Entry_Widget.insert(0,int(first)+int(second))
    elif sign=='-':
        Entry_Widget.insert(0,int(first)-int(second))
    elif sign=='*':
        Entry_Widget.insert(0,int(first)*int(second))
    elif sign=='/':
        if int(second)==0:
            Entry_Widget.insert(0,"infinity")
        else :
            Entry_Widget.insert(0,int(first)/int(second))


def equal():
    global first
    global second
    second=Entry_Widget.get() 
    Entry_Widget.delete(0,'end')
    f=float(first)
    s=float(second)
    if f.is_integer() and s.is_integer():
        intequal()
    else :
        if sign=='+':
            Entry_Widget.insert(0,float(first)+float(second))
        elif sign=='-':
            Entry_Widget.insert(0,float(first)-float(second))
        elif sign=='*':
            Entry_Widget.insert(0,float(first)*float(second))
        elif sign=='/':
            Entry_Widget.insert(0,float(first)/float(second))

def button_clearf():
    Entry_Widget.delete(0,'end')
# buttons in calculator
button_1=t.Button(root,text="1",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(1))
button_2=t.Button(root,text="2",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(2))
button_3=t.Button(root,text="3",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(3))
button_4=t.Button(root,text="4",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(4))
button_5=t.Button(root,text="5",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(5))
button_6=t.Button(root,text="6",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(6))
button_7=t.Button(root,text="7",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(7))
button_8=t.Button(root,text="8",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(8))
button_9=t.Button(root,text="9",padx=20,pady=20,borderwidth=3,command=lambda : button_clicked(9))
button_0=t.Button(root,text="0",padx=50,pady=20,borderwidth=3,command=lambda : button_clicked(0))
button_clear=t.Button(root,text="Clear",padx=50,pady=20,command=button_clearf)
button_add=t.Button(root,text="+",padx=30,pady=54,borderwidth=3,command=add)        #padx=30,pady=50
button_sub=t.Button(root,text="-",padx=20,pady=20,borderwidth=3,command=sub)
button_mult=t.Button(root,text="X",padx=20,pady=20,borderwidth=3,command=mult)
button_div=t.Button(root,text="/",padx=20,pady=20,borderwidth=3,command=div)
button_equal=t.Button(root,text='=',padx=30,pady=20,borderwidth=3,command=equal)
button_decimal=t.Button(root,text='.',padx=20,pady=20,borderwidth=3,command=lambda : button_clicked('.'))

#Packing all widgets
Entry_Widget.grid(row=0,column=0,columnspan=9,padx=2)
button_clear.grid(row=1,column=3,pady=1,columnspan=2)
button_7.grid(row=1,column=0,pady=1)
button_8.grid(row=1,column=1,pady=1)
button_9.grid(row=1,column=2,pady=1)
button_4.grid(row=2,column=0,pady=1)
button_5.grid(row=2,column=1,pady=1)
button_6.grid(row=2,column=2,pady=1)
button_1.grid(row=3,column=0,pady=1)
button_2.grid(row=3,column=1,pady=1)
button_3.grid(row=3,column=2,pady=1)
button_0.grid(row=4,column=0,pady=2,columnspan=2)
button_add.grid(row=2,column=3,rowspan=2,pady=0)
button_sub.grid(row=2,column=4,pady=1)
button_mult.grid(row=3,column=4,pady=1)
button_div.grid(row=4,column=4,pady=1)
button_decimal.grid(row=4,column=2,pady=1)
button_equal.grid(row=4,column=3,pady=1)

root.mainloop()