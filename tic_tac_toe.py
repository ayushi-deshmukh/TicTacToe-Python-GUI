from tkinter import *
root=Tk()
t=1
c1=0
c2=0
def restart():
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")
    b9.config(text="")
    global t
    t=1

def winner():
    a1=b1["text"]
    a2=b2["text"]
    a3=b3["text"]
    a4=b4["text"]
    a5=b5["text"]
    a6=b6["text"]
    a7=b7["text"]
    a8=b8["text"]
    a9=b9["text"]
    if (a1=="x" and a2=="x" and a3=="x") or (a4=="x" and a5=="x" and a6=="x") or (a7=="x" and a8=="x" and a9=="x") or (a1=="x" and a4=="x" and a7=="x") or (a2=="x" and a5=="x" and a8=="x") or (a3=="x" and a6=="x" and a9=="x") or (a1=="x" and a5=="x" and a9=="x") or (a3=="x" and a5=="x" and a7=="x"):
        print("x is winner")
        restart()
        global c1
        c1=c1+1
        t1.delete(0,END)
        t1.insert(0,c1)
        if c1==3:
            print("player 1 is final winner")
    elif (a1=="o" and a2=="o" and a3=="o") or (a4=="o" and a5=="o" and a6=="o") or (a7=="o" and a8=="o" and a9=="o") or (a1=="o" and a4=="o" and a7=="o") or (a2=="o" and a5=="o" and a8=="o") or (a3=="o" and a6=="o" and a9=="o") or (a1=="o" and a5=="o" and a9=="o") or (a3=="o" and a5=="o" and a7=="o"):
        print("o is winner")
        restart()
        global c2
        c2=c2+1
        t2.insert(0,c2)
        t2.delete(0,END)
        t2.insert(0,c2)
        if c2==3:
            print("player 1 is final winner")


def show1():
    global t
    if len(b1["text"])==0:
        if (t%2==1):
            b1.config(text="x")
        else:
            b1.config(text="o")
        t=t+1
        winner()
def show2():
    global t
    if len(b2["text"])==0:
        if (t%2==1):
            b2.config(text="x")
        else:
            b2.config(text="o")
        t=t+1
        winner()
def show3():
    global t
    if len(b3["text"])==0:
        if (t%2==1):
            b3.config(text="x")
        else:
            b3.config(text="o")
        t=t+1
        winner()
def show4():
    global t
    if len(b4["text"])==0:
        if (t%2==1):
            b4.config(text="x")
        else:
            b4.config(text="o")
        t=t+1
        winner()
def show5():
    global t
    if len(b5["text"])==0:
        if (t%2==1):
            b5.config(text="x")
        else:
            b5.config(text="o")
        t=t+1
        winner()
def show6():
    global t
    if len(b6["text"])==0:
        if (t%2==1):
            b6.config(text="x")
        else:
            b6.config(text="o")
        t=t+1
        winner()
def show7():
    global t
    if len(b7["text"])==0:
        if (t%2==1):
            b7.config(text="x")
        else:
            b7.config(text="o")
        t=t+1
        winner()
def show8():
    global t
    if len(b8["text"])==0:
        if (t%2==1):
            b8.config(text="x")
        else:
            b8.config(text="o")
        t=t+1
        winner()
def show9():
    global t
    if len(b9["text"])==0:
        if (t%2==1):
            b9.config(text="x")
        else:
            b9.config(text="o")
        t=t+1
        winner()

b1=Button(text="",command=show1)
b2=Button(text="",command=show2)
b3=Button(text="",command=show3)
b4=Button(text="",command=show4)
b5=Button(text="",command=show5)
b6=Button(text="",command=show6)
b7=Button(text="",command=show7)
b8=Button(text="",command=show8)
b9=Button(text="",command=show9)
l1=Label(text="player1")
l2=Label(text="player2")
t1=Entry()
t2=Entry()

b1.place(x=100,y=100,width=50,height=50)
b2.place(x=150,y=100,width=50,height=50)
b3.place(x=200,y=100,width=50,height=50)
b4.place(x=100,y=150,width=50,height=50)
b5.place(x=150,y=150,width=50,height=50)
b6.place(x=200,y=150,width=50,height=50)
b7.place(x=100,y=200,width=50,height=50)
b8.place(x=150,y=200,width=50,height=50)
b9.place(x=200,y=200,width=50,height=50)
l1.place(x=50,y=50,width=50,height=40)
l2.place(x=200,y=50,width=50,height=40)
t1.place(x=100,y=50,width=50,height=40)
t2.place(x=250,y=50,width=50,height=40)
mainloop()

