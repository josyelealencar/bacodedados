import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importa o Pillow para trabalhar com imagens

def home_funcionario():
    root = tk.Tk()
    root.title("Sistema de Gerenciamento - Funcionário")
    root.geometry("800x600")

    frame_menu = tk.Frame(root, bg="#273b7a", width=200, height=600)
    frame_menu.pack(side="left", fill="y")

    label_menu_title = tk.Label(frame_menu, text="Menu", bg="#273b7a", fg="white", font=("Arial", 14))
    label_menu_title.pack(pady=20)

    buttons = ["Tarefas", "Projetos", "Atualizar Dados", "Notificações"]
    for button in buttons:
        btn = tk.Button(frame_menu, text=button, bg="#34495E", fg="white", width=20, height=2)
        btn.pack(pady=5)

    frame_main = tk.Frame(root, bg="#ECF0F1")
    frame_main.pack(side="right", expand=True, fill="both")

    label_dashboard_title = tk.Label(frame_main, text="Painel do Funcionário", font=("Arial", 18), bg="#ECF0F1")
    label_dashboard_title.pack(pady=20)

    img_path = r"C:\Users\Josy Alencar\OneDrive\Área de Trabalho\bd-front\images\funcionario0.jpg"
    img_pil = Image.open(img_path)
    img_pil = img_pil.resize((100, 100))  
    img = ImageTk.PhotoImage(img_pil)

    img_label = tk.Label(frame_main, image=img, bg="#ECF0F1")
    img_label.pack(pady=10)

    label_info = tk.Label(frame_main, text="Nome: João da Silva\nCargo: Desenvolvedor", font=("Arial", 12), bg="#ECF0F1")
    label_info.pack(pady=20)

    root.mainloop()

home_funcionario()
