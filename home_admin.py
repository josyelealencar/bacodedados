import tkinter as tk
from tkinter import ttk

def mostrar_dashboard():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dashboard_title = tk.Label(frame_main, text="Painel do Administrador", font=("Arial", 18), bg="#ECF0F1")
    label_dashboard_title.pack(pady=20)

    label_graph = tk.Label(frame_main, text="Gráfico de Produtividade (Placeholder)", bg="#ECF0F1")
    label_graph.pack(pady=50)

    stats_frame = tk.Frame(frame_main, bg="#ECF0F1")
    stats_frame.pack(pady=20)

    stats = [
        ("Funcionários Ativos", "120"),
        ("Projetos Ativos", "35"),
        ("Salário Médio", "R$ 5000")
    ]
    
    for stat_name, stat_value in stats:
        stat_label = tk.Label(stats_frame, text=f"{stat_name}: {stat_value}", font=("Arial", 12), bg="#ECF0F1")
        stat_label.pack(pady=5)

def gerenciar_funcionarios():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_func_title = tk.Label(frame_main, text="Gerenciar Funcionários", font=("Arial", 18), bg="#ECF0F1")
    label_func_title.pack(pady=20)

    btn_cadastrar = tk.Button(frame_main, text="Cadastrar Novo Funcionário", bg="#27AE60", fg="white", width=25, height=2)
    btn_cadastrar.pack(pady=10)

    btn_deletar = tk.Button(frame_main, text="Deletar Funcionário", bg="#C0392B", fg="white", width=25, height=2)
    btn_deletar.pack(pady=10)

def gerenciar_projetos():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_proj_title = tk.Label(frame_main, text="Gerenciar Projetos", font=("Arial", 18), bg="#ECF0F1")
    label_proj_title.pack(pady=20)

    btn_cadastrar_proj = tk.Button(frame_main, text="Cadastrar Novo Projeto", bg="#27AE60", fg="white", width=25, height=2)
    btn_cadastrar_proj.pack(pady=10)

    btn_editar_proj = tk.Button(frame_main, text="Editar Projeto Existente", bg="#F39C12", fg="white", width=25, height=2)
    btn_editar_proj.pack(pady=10)

    btn_excluir_proj = tk.Button(frame_main, text="Excluir Projeto", bg="#C0392B", fg="white", width=25, height=2)
    btn_excluir_proj.pack(pady=10)

    btn_listar_proj = tk.Button(frame_main, text="Listar Projetos", bg="#2980B9", fg="white", width=25, height=2)
    btn_listar_proj.pack(pady=10)

def gerenciar_departamentos():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dept_title = tk.Label(frame_main, text="Gerenciar Departamentos", font=("Arial", 18), bg="#ECF0F1")
    label_dept_title.pack(pady=20)

    btn_cadastrar_dept = tk.Button(frame_main, text="Cadastrar Novo Departamento", bg="#27AE60", fg="white", width=25, height=2)
    btn_cadastrar_dept.pack(pady=10)

    btn_editar_dept = tk.Button(frame_main, text="Editar Departamento Existente", bg="#F39C12", fg="white", width=25, height=2)
    btn_editar_dept.pack(pady=10)

    btn_excluir_dept = tk.Button(frame_main, text="Excluir Departamento", bg="#C0392B", fg="white", width=25, height=2)
    btn_excluir_dept.pack(pady=10)

    btn_listar_dept = tk.Button(frame_main, text="Listar Departamentos", bg="#2980B9", fg="white", width=25, height=2)
    btn_listar_dept.pack(pady=10)

def home_admin():
    global frame_main  
    root = tk.Tk()
    root.title("Sistema de Gerenciamento - Admin")
    root.geometry("800x600")

    frame_menu = tk.Frame(root, bg="#273b7a", width=200, height=600)
    frame_menu.pack(side="left", fill="y")

    label_menu_title = tk.Label(frame_menu, text="Menu", bg="#273b7a", fg="white", font=("Arial", 14))
    label_menu_title.pack(pady=20)

    buttons = [
        ("Dashboard", mostrar_dashboard),
        ("Gerenciar Funcionários", gerenciar_funcionarios),
        ("Gerenciar Projetos", gerenciar_projetos),
        ("Gerenciar Departamentos", gerenciar_departamentos),
        ("Relatórios", None)
    ]

    for button_text, command in buttons:
        btn = tk.Button(frame_menu, text=button_text, bg="#34495E", fg="white", width=20, height=2, command=command)
        btn.pack(pady=5)

    frame_main = tk.Frame(root, bg="#ECF0F1")
    frame_main.pack(side="right", expand=True, fill="both")

    mostrar_dashboard()

    root.mainloop()

home_admin()
