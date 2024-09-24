import tkinter as tk
from tkinter import ttk, messagebox  
from PIL import Image, ImageTk 

def home_funcionario():
    root = tk.Tk()
    root.title("Sistema de Gerenciamento - Funcionário")
    root.geometry("800x600")

    frame_menu = tk.Frame(root, bg="#273b7a", width=200, height=600)
    frame_menu.pack(side="left", fill="y")

    label_menu_title = tk.Label(frame_menu, text="Menu", bg="#273b7a", fg="white", font=("Arial", 14))
    label_menu_title.pack(pady=20)

    frame_main = tk.Frame(root, bg="#ECF0F1")
    frame_main.pack(side="right", expand=True, fill="both")

    label_dashboard_title = tk.Label(frame_main, text="Painel do Funcionário", font=("Arial", 18), bg="#ECF0F1")
    label_dashboard_title.pack(pady=20)

    img_path = r"images/employees.png"
    img_pil = Image.open(img_path)
    img_pil = img_pil.resize((100, 100))  
    img = ImageTk.PhotoImage(img_pil)

    img_label = tk.Label(frame_main, image=img, bg="#ECF0F1")
    img_label.pack(pady=10)

    label_info = tk.Label(frame_main, text="Nome: João da Silva\nCargo: Desenvolvedor", font=("Arial", 12), bg="#ECF0F1")
    label_info.pack(pady=20)


    def mostrar_tarefas():
        for widget in frame_main.winfo_children():
            widget.destroy() 

        label_tarefas_title = tk.Label(frame_main, text="Tarefas Designadas", font=("Arial", 18), bg="#ECF0F1")
        label_tarefas_title.pack(pady=20)

        #lógica para listar as tarefas do funcionário
        label_tarefa_1 = tk.Label(frame_main, text="Tarefa 1: Completar relatório", font=("Arial", 12), bg="#ECF0F1")
        label_tarefa_1.pack(pady=5)
        

    def mostrar_projetos():
        for widget in frame_main.winfo_children():
            widget.destroy()

        label_projetos_title = tk.Label(frame_main, text="Projetos Designados", font=("Arial", 18), bg="#ECF0F1")
        label_projetos_title.pack(pady=20)

        # lógica para listar os projetos do funcionário
        label_projeto_1 = tk.Label(frame_main, text="Projeto 1: Desenvolvimento de App", font=("Arial", 12), bg="#ECF0F1")
        label_projeto_1.pack(pady=5)


    def atualizar_dados():
        for widget in frame_main.winfo_children():
            widget.destroy()

        label_atualizar_title = tk.Label(frame_main, text="Atualizar Dados", font=("Arial", 18), bg="#ECF0F1")
        label_atualizar_title.pack(pady=20)

        # Aqui você pode adicionar campos para o funcionário atualizar seus dados
        label_nome = tk.Label(frame_main, text="Nome:", font=("Arial", 12), bg="#ECF0F1")
        label_nome.pack(pady=5)
        entry_nome = tk.Entry(frame_main)
        entry_nome.pack(pady=5)

        btn_salvar = tk.Button(frame_main, text="Salvar", command=lambda: messagebox.showinfo("Info", "Dados atualizados!"), bg="#34495E", fg="white")
        btn_salvar.pack(pady=10)

    buttons = [
        ("Tarefas", mostrar_tarefas),
        ("Projetos", mostrar_projetos),
        ("Atualizar Dados", atualizar_dados),
        ("Notificações", lambda: messagebox.showinfo("Info", "Notificações não implementadas ainda.")),
    ]

    for button_text, command in buttons:
        btn = tk.Button(frame_menu, text=button_text, bg="#34495E", fg="white", width=20, height=2, command=command)
        btn.pack(pady=5)

    root.mainloop()

home_funcionario()
