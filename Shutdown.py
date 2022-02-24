import tkinter
import tkinter as tk
import os
import sys
from tkinter import *
import subprocess
from tkinter import simpledialog

def OnClick1():
   tk = Tk()
   a = Frame(tk)
   os.system("shutdown /s /t 3600")  
   myLabel = Label(tk, text="Desligando em 1 hora") 
   myLabel.pack()
def OnClick6():
   os.system('shutdown -s -t 7200')  
   tk = Tk()
   a = Frame(tk)
   myLabel = Label(tk, text="Desligando em 2 horas") 
   myLabel.pack()   
   
def OnClick2(): 
   subprocess.call(["shutdown", "/a"])
   tk = Tk()
   a = Frame(tk)
   myLabel = Label(tk, text="Agendamento cancelado") 
   myLabel.pack()
def OnClick3():
      tk = Tk()
      a = Frame(tk)
      shutdown()
      p = subprocess.Popen("ipconfig", stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()
      p_status = p.wait()
      myLabel = Label(tk, text=output) 
      myLabel.pack()
def OnClick4():
      tk = Tk()
      a = Frame(tk)
      
      p = subprocess.Popen("ipconfig", stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()
      p_status = p.wait()
      myLabel = Label(tk, text=output) 
      myLabel.pack()
        
def OnClick5():
   tk = Tk()
   a = Frame(tk)
   tk.withdraw()
   e = simpledialog.askinteger(title="Desligamento agendado",  # condicao/permitir somente numero
                                  prompt="Minutos:")
   e *= 60
   cmd = "cmd /c shutdown -s -t {0}".format(e)                               
   os.system(cmd)
   #myLabel = Label(root, text="") 
   #myLabel.pack()
          

def shutdown():
   subprocess.call(["shutdown", "/s", "/t", "900"])
   tk = Tk()
   a = Frame(tk)
   myLabel = Label(tk, text=f"Desligando em {900/60} minutos" ) 
   myLabel.pack()
if __name__ == "__main__":
   root = tkinter.Tk()
   root.title("Shutdown Schedule")
   root.geometry("600x350")
   myButton1 = tkinter.Button(root, text= "Desligar em 1 hora", command= OnClick1)
   myButton1.pack(expand = tkinter.TRUE)
   myButton6 = tkinter.Button(root, text= "Desligar em 2 horas", command= OnClick6)
   myButton6.pack(expand = tkinter.TRUE)
   myButton5 = Button(root, text= "Customizado", command= OnClick5)
   myButton5.pack(expand = tkinter.TRUE)
   myButton2 = Button(root, text= "Cancelar", command= OnClick2)
   myButton2.pack(expand = tkinter.TRUE)
   myButton4 = Button(root, text= "VerIP", command= OnClick4)
   myButton4.pack(expand = tkinter.TRUE)
   myButton3 = Button(root, text= "Click", command= shutdown) #OnClick3
   myButton3.pack(expand = tkinter.TRUE)

   root.mainloop()







