from tkinter import *
import random
l=[]
final=[]
sym=['@','#','$','%']
ambi=['(', '{',' }','[',' ]',' (',' )', '/', '~']
numbers=['1','2','3','4','5','6','7','8','9']
lc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
root = Tk()
root.geometry("1000x1000")
a = Label(text="Do u want symbols in your password",fg="Steel BLUE",font=('arial',10,'bold'))
a.pack()
var1 = IntVar()
Checkbutton(text="yes", variable=var1).pack()
var2 = IntVar()
Checkbutton(text="no", variable=var2).pack()
b = Label(text="Do u want lowercase character in your password",fg="Steel BLUE",font=('arial',10,'bold'))
b.pack()
var3 = IntVar()
Checkbutton(text="yes", variable=var3).pack()
var4 = IntVar()
Checkbutton(text="no", variable=var4).pack()
b = Label(text="Do u want uppercase character in your password",fg="Steel BLUE",font=('arial',10,'bold'))
b.pack()
var5 = IntVar()
Checkbutton(text="yes", variable=var5).pack()
var6 = IntVar()
Checkbutton(text="no", variable=var6).pack()
b = Label(text="Do u want ambigous character in your password",fg="Steel BLUE",font=('arial',10,'bold'))
b.pack()
var7 =IntVar()
Checkbutton(text="yes", variable=var7).pack()
var8 = IntVar()
Checkbutton(text="no", variable=var8).pack()
b = Label(text="Do u want digit character in your password",fg="Steel BLUE",font=('arial',10,'bold'))
b.pack()
var9 = IntVar()
q=Checkbutton(text="yes", variable=var9)
q.pack()
var10= IntVar()
Checkbutton(text="no", variable=var10).pack()
var11=Label(text="Exit window for password",fg="Steel BLUE",font=('arial',10,'bold'))
var11.pack()
root.mainloop()
sum=var1.get()+var7.get()+var9.get()+var5.get()+var3.get()
root=Tk()
root.geometry("1000x1000")
k=Label(text="YOUR PASSWORD IS ",fg="RED",font=('arial',10,'bold'))
k.pack()
var11=Entry()
var11.pack()
if(sum>2):
    for i in range(2):
        if(var1.get()==1):
            choice=random.choice(sym)
            var11.insert(0,choice)
        if(var9.get()==1):
            choice=random.choice(numbers)
            var11.insert(0,choice)
        if(var7.get()==1):
            choice=random.choice(ambi)
            var11.insert(0,choice)
        if(var5.get()==1):
            choice=random.choice(uc)
            var11.insert(0,choice)
        if(var3.get()==1):
            choice=random.choice(lc)
            var11.insert(0,choice)
else:
    for i in range(5):
        if(var1.get()==1):
            choice=random.choice(sym)
            var11.insert(0,choice)
        if(var9.get()==1):
            choice=random.choice(numbers)
            var11.insert(0,choice)
        if(var7.get()==1):
            choice=random.choice(ambi)
            var11.insert(0,choice)
        if(var5.get()==1):
            choice=random.choice(uc)
            var11.insert(0,choice)
        if(var3.get()==1):
            choice=random.choice(lc)
            var11.insert(0,choice)
root.mainloop()