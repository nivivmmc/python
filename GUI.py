from tkinter import *
"""
1.there are basically two main things
1.1. window (that is actully what we see on our desktop)
1.2. widgets(this buttons..)
2. we  write everything inside window and mainloop()
"""

def km_to_miles():
    #print("succeed")
    #print(e1_value.get())
    miles=float(e1_value.get())*1.6
    #t1.insert(END,e1_value.get() # 'END' help to append the text without overwriting
    t1.insert(END,miles)
    
    
def km_to_miles(): 
    input=input("enter number")
    result=input*30
    
    
def m_to_km():    
    



window=Tk() # it ll create window
b1=Button(window,text='send',command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=StringVar() #StringVar is a class which holds the string
e1=Entry(window,textvariable=e1_value)# Entry is used to display the text in the widget
e1.grid(row=0,column=1)

t1=Text(window,height='10',width='20')
t1.grid(row=1,column=0)


window.mainloop() # it ll make infinite loop untill we close the window
