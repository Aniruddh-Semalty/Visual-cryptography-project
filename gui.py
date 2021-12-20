import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import os
import RGB
import AES_EncAndDec


parent_dir=os.getcwd()+"/Database/"
global enc_file
global enc_key
global enc_v
global dec_v
global dec_key
global dec_file

def mk():
    if(not(os.path.isdir("Database"))):
        os.mkdir("Database")
        os.mkdir(os.path.join(parent_dir,"input"))
        os.mkdir(os.path.join(parent_dir,"encrypt"))
        os.mkdir(os.path.join(parent_dir,"decrypt"))
mk()

def e():
    exit()

def openfileEnc():
    global enc_file
    path=os.path.join(parent_dir,"input")
    filename=filedialog.askopenfile(initialdir=path,title="Select file",filetype=(("image files",".jpg"),("image files",".png"),("all files","*.*")))
    if filename is None:
        enc_file=""
        i.set("No File Selected")
    else:
        enc_file=filename.name
        i.set(enc_file)

def openfileDec():
    global dec_file
    path=os.path.join(parent_dir,"encrypt")
    filename=filedialog.askopenfile(initialdir=path,title="Select file",filetype=(("image files",".jpg"),("image files",".png"),("all files","*.*")))
    if filename is None:
        dec_file=""
        j.set("No File Selected")
    else:
        dec_file=filename.name
        j.set(dec_file)

def key():
    global enc_v
    global enc_key
    if(enc_v.get()=="AES-256"):
        enc_key=simpledialog.askstring("password","Enter the password")
    elif(enc_v.get()=="RGB"):
        enc_key=simpledialog.askinteger("password","Enter the block size(ps:50-100)")
    else:
        messagebox.showwarning("warning","No method selected")

def Deckey():
    global dec_v
    global dec_key
    if(dec_v.get()=="AES-256"):
        dec_key=simpledialog.askstring("password","Enter the password")

    elif(dec_v.get()=="RGB"):
        dec_key=simpledialog.askinteger("password","Enter the block size(ps:50-100)")
    else:
        messagebox.showwarning("warning","No method selected")

def encrypt():
    global enc_v
    global enc_file
    global enc_key
    if(enc_v.get()=="AES-256"):
        AES_EncAndDec.aes_encrypt(parent_dir,enc_key,enc_file)
        tk.messagebox.showinfo("Success","Encryption Successful")
    elif(enc_v.get()=="RGB"):
        parent_=os.path.join(parent_dir,"encrypt/output.jpg")
        RGB.SHUFFLE_PIXEL(parent_,enc_key,enc_file)
        tk.messagebox.showinfo("Success","Encryption Successful")
    else:
        print(enc_v.get())

def decrypt():
    global dec_v
    global dec_file
    global dec_key
    if(dec_v.get()=="AES-256"):
        AES_EncAndDec.aes_decrypt(parent_dir,dec_key,dec_file)
        tk.messagebox.showinfo("success","Decryption Successful")
    elif(enc_v.get()=="RGB"):
        parent_=os.path.join(parent_dir,"decrypt/output.jpg")
        RGB.SHUFFLE_PIXEL(parent_,dec_key,dec_file)
        tk.messagebox.showinfo("success","Decryption Successful")
    else:
        print(dec_v.get())


def frame():
    top = tk.Tk()
    top.geometry("490x400")
    top.configure(bg="black")
    top.title("Image Cryptography")
    labelframe2=tk.LabelFrame(top,text="Image Encryption: ",height=175,width=470,bg="light blue").place(x=10,y=10)
    labelframe3=tk.LabelFrame(top,text="Image Decryption: ",height=185,width=470,bg="light blue").place(x=10,y=205)
    
    global i
    global enc_v
    global enc_key
    global enc_file
    listus=["AES-256","RGB"]
    enc_v=tk.StringVar()
    enc_v.set("None")
    i=tk.StringVar()
    
    inputEncFile = tk.Label(labelframe2, text="1. Select the Image:").place(x=10,y=50)
    inputEncFileEntry = tk.Entry(labelframe2,width=42,textvariable=i).place(x=135,y=50)
    inputEncBtn = tk.Button(labelframe2, text="Browse ...",width=10, height=1,bg="green yellow",command=openfileEnc).place(x=395,y=46)
    recEncFile = tk.Label(labelframe2, text="2. Select the Method:").place(x=10,y=90)
    reclistBtn=tk.OptionMenu(labelframe2,enc_v,*listus).place(x=135,y=87,width=100)
    keyEncFile = tk.Label(labelframe2, text="3. Generate Key:").place(x=10,y=130)
    keyBtn=tk.Button(labelframe2,text="Input Key", height=1,activebackground="cyan",command=key).place(x=135,y=130,width=100)
    EncryptBTN=tk.Button(labelframe2,text="Encrypt",width=20, height=3,activebackground="green",command=encrypt).place(anchor="e",relx=.85,rely=.35)

    global j
    global dec_key
    global dec_file
    global dec_v
    j=tk.StringVar()
    dec_v=tk.StringVar()
    dec_v.set("None")


    inputDecFile = tk.Label(labelframe2, text="1. Select the Image:").place(x=10,y=245)
    inputDecFileEntry = tk.Entry(labelframe2,width=42,textvariable=j).place(x=135,y=245)
    inputDecBtn = tk.Button(labelframe2, text="Browse ...",width=10, height=1,bg="green yellow",command=openfileDec).place(x=395,y=241)
    recDecFile = tk.Label(labelframe2, text="2. Select the Method:").place(x=10,y=285)
    reclistBtn=tk.OptionMenu(labelframe2,dec_v,*listus).place(x=135,y=282,width=100)
    keyEncFile = tk.Label(labelframe2, text="3. Select secret:").place(x=10,y=325)
    keyBtn=tk.Button(labelframe2,text="Input Key", height=1,activebackground="cyan",command=Deckey).place(x=135,y=325,width=100)
    EncryptBTN=tk.Button(labelframe2,text="Decrypt",width=20, height=3,activebackground="red",command=decrypt).place(anchor="e",relx=.85,rely=.85)

    top.mainloop()

frame()