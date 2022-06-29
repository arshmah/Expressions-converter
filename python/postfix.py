from tkinter import *
root=Tk()
root.geometry("620x150")
root.configure(bg="black")
import infix_postfix





eq=""
exp1=""

def convert():
    global eq
    global exp1
    buttonpushed()
    t1= var1.get()
    t2= var2.get()
    if(t1=="infix" and t2=="postfix"):
        eq=infix_postfix.infix_to_postfix(exp1)
        v2.set(eq)
    elif(t1=="postfix" and t2=="infix"):
        eq=infix_postfix.postfix_to_infix(exp1)
        v2.set(eq)
   
    else:
        print("ERROR")
    
def buttonpushed():
    global txtb
    global exp1
    exp1= txtb.get()







var1= StringVar(root)
var1.set("expression")
option1 = OptionMenu(root,var1,"infix","postfix")
option1.grid(row=0,column=0,padx=5,pady=5)
#option1.pack()
txtb = Entry(root,bg="yellow",fg="black",font=("Comic Sans MS",15),width=40)
txtb.grid(row=0,column=1,padx=5,pady=5)
#txtb.pack()

var2= StringVar(root)
var2.set("converter")
option2 = OptionMenu(root,var2,"infix","postfix")
option2.grid(row=1,column=0,padx=5,pady=5)
#option2.pack()
v2=StringVar()
label2 = Label(root,textvariable=v2,width="40",bg="yellow",fg="red",padx=1,pady=1,font=("Comic Sans MS",15)).grid(row=1,column=1,padx=5,pady=5)
#label2.pack()
b = Button(root,text="CONVERT",relief=GROOVE,command=convert).place(x=120,y=90)





root.mainloop()


# In[ ]: