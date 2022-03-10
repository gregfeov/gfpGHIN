import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk
from comp import *
def faq():
    n = texte.get()
    p = waa.get()
    erte=vf(n, p, lab,de,root)
    if erte==True:
        root.destroy()
        w=tk.Tk()
        w.geometry("700x800")
        w.configure(background='#242424')
        whou=Label(w,text="User: ",bg="#242424", fg="#de0000",font=(8))
        whou.place(x=10,y=10)
        who=Label(w,text=n,bg="#242424", fg="#002aff",font=(8))
        who.place(x=60,y=10)
        f = Font(who, who.cget("font"))
        f.configure(underline=True)
        who.configure(font=f)
        t = Label(w, text="", bg="#242424", fg="#de0000", font=(8))
        t.place(x=600, y=750)
        #
        bla=StringVar()
        bl=Label(w,textvariable=bla,bg="#242424", fg="#15ff00")
        bl.place(x=100,y=40)
        #
        #bla.set(str(getbalance(n)))
        #
        Label(w,text="Balance: ",bg="#242424", fg="#de0000",font=(8)).place(x=10,y=40)
        #
        Label(w,text="To:",bg="#242424", fg="#002aff",font=(8)).place(x=10,y=100)
        trt=Entry(w,bg="#242424",fg="#15ff00")
        trt.place(x=100,y=100)
        Label(w, text="Sum:", bg="#242424", fg="#002aff", font=(8)).place(x=10, y=140)
        trs = Entry(w, bg="#242424", fg="#15ff00")
        trs.place(x=100, y=140)
        Button(w,text="Transact",bg="#242424", fg="#002aff",command=lambda:transaction(n,trt.get(),trs.get())).place(x=10,y=170)
        def update_clock():
            now = time.strftime("%H:%M:%S")
            t.configure(text=now)
            bl.configure(text=str(getbalance(n)))
            root.after(10, update_clock)
        update_clock()
        def update_balance():
            bla.set(str(gb(n)))
            root.after(100, update_balance)
        update_balance()
        w.mainloop()


root=tk.Tk()
root.geometry("500x500+300+250")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
#root.wm_attributes("-transparentcolor", "white")
#root.configure(background='#242424')
#
root.resizable(height = None, width = None)
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection
image = Image.open('C:\\Users\\user\\desktop\\imgp.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

#
Label(root, text="Login:", bg="#242424", fg="#de0000",font=(12)).place(x=10,y=10)
Label(root, text="Password:", bg="#242424", fg="#de0000",font=(12)).place(x=10,y=60)
texte = Entry(root,bg="#242424",fg="#15ff00")
texte.place(x=100,y=10)
waa = Entry(root,show="*",bg="#242424", fg="#15ff00")
waa.place(x=100,y=60)
n=texte.get()
p=waa.get()
lab = StringVar()
de = Label(root, textvariable=lab,bg="#242424", fg="#de0000",font=(9))
de.place(x=10,y=170)
de.pack_forget()
b=Button(root,text="Sign in",bg="#242424", fg="#de0000",height=2,width=20,command=lambda:faq()).place(x=10,y=120)
#
be=Button(root,text="Exit",bg="#242424", fg="#de0000",font=(12),command=lambda:root.destroy()).place(x=450,y=10)
#
root.mainloop()
