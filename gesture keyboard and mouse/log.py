import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="#BFEFFF")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("login Form")

Login_frame=tk.Frame(root,bg="pink")
Login_frame.place(x=300,y=220)


username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('g1.jpeg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()
        
         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


#bg1_icon=ImageTk.PhotoImage(file="E:\30%-face-mask\\b.jpg")
      
# bg_lbl=tk.Label(root,image=bg1_icon, width=600,height=550)
# bg_lbl.place(x=50,y=40)
# title=tk.Label(root, text="Defective Gear \n Detection System", font=("Times New Roman", 35, "bold"),bd=5,bg="black",fg="white")
# title.place(x=100,y=300,width=500)


    
title=tk.Label(root, text="Login Here", font=("Times New Roman", 25),bd=5,bg="black",fg="white")
title.place(x=300,y=200,width=250)
        
 
l2 = tk.Label(root, text="username :", width=10, font=("Times new roman", 20, "bold"), bg="snow")
l2.place(x=200, y=300)
t1 = tk.Entry(root, textvar=username, width=14, font=('', 20))
t1.place(x=400, y=300)
# that is for label 2 (full name)

# that is for label 4(blood group)

l5 = tk.Label(root, text="password :", width=10, font=("Times new roman", 20, "bold"), bg="snow")
l5.place(x=200, y=400)
t4 = tk.Entry(root, textvar=password, width=14, font=('', 20))
t4.place(x=400, y=400)    
        
    
       
        # Login Function       




    
def window():
  root.destroy()
  
  



button1 = tk.Button(root, text="Login", command=login, width=13, height=1,font=('times', 18, ' bold '), bg="#336699", fg="white")
button1.place(x=300, y=490)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)




root.mainloop()