from tkinter import Tk, Frame, Label
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1000x600')
root.title('Tkinter Hub (Sistema de Gerenciamento de Funcionários)')

bg_color = '#273b7a'

def load_image(file_path, size):
    img = Image.open(file_path)
    img = img.resize(size, Image.LANCZOS) 
    return ImageTk.PhotoImage(img)

login_employee_icon = load_image('images/employees (1).png', (100, 100))
company_logo = load_image('images/logo3.png', (300, 100)) 
locked_icon = load_image('images/locked.png', (30, 30))  
unlocked_icon = load_image('images/unlocked.png', (30, 30)) 

def show_hide_password():
    if senha_ent['show'] == '*':
        senha_ent.config(show='')
        show_hide_btn.config(image=unlocked_icon)

    else:
        senha_ent.config(show='*')
        show_hide_btn.config(image=locked_icon)

login_page_fm = Frame(root, highlightbackground=bg_color, highlightthickness=3)

heading_lb = Label(login_page_fm, text='Seja Bem-Vindo ao Sistema', bg=bg_color, fg='white', font=('Bold', 18))
heading_lb.place(x=0, y=0, width=800)

employee_icon_lb = Label(login_page_fm, image=login_employee_icon)
employee_icon_lb.place(x=340, y=100)  

email_lb=Label(login_page_fm, text='Email', font=('Bold, 15'), fg=bg_color)
email_lb.place(x=255, y=220)

email_ent = tk.Entry(login_page_fm,font=('Bold', 15), justify=tk.CENTER)
email_ent.place(x=260, y=260)

senha_lb = Label(login_page_fm, text='Senha', font=('Bold', 15), fg=bg_color)
senha_lb.place(x=255, y=310)  

senha_ent = tk.Entry(login_page_fm, font=('Bold', 15), justify=tk.CENTER, show="*")
senha_ent.place(x=260, y=350)

show_hide_btn=tk.Button(login_page_fm, image=locked_icon, bd=0, command=show_hide_password )
show_hide_btn.place(x=490, y=345)

company_logo_lb = Label(login_page_fm, image=company_logo)
company_logo_lb.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10) 

login_btn=tk.Button(login_page_fm, text='Login', font=('Bold', 15), bg=bg_color, fg='white')
login_btn.place(x=290, y=400, width=150, height=30)

login_page_fm.pack(pady=30)
login_page_fm.pack_propagate(False)
login_page_fm.configure(width=800, height=600)

root.mainloop()
