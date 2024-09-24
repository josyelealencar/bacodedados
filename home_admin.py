import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox 

def mostrar_dashboard():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dashboard_title = tk.Label(frame_main, text="Painel do Administrador", font=("Arial", 18), bg="#ECF0F1")
    label_dashboard_title.pack(pady=20)

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

    btn_cadastrar = tk.Button(frame_main, text="Cadastrar Novo Funcionário", bg="#27AE60", fg="white", width=25, height=2, command=cadastrar_funcionario)
    btn_cadastrar.pack(pady=10)

    btn_deletar = tk.Button(frame_main, text="Deletar Funcionário", bg="#C0392B", fg="white", width=25, height=2, command=deletar_funcionario)
    btn_deletar.pack(pady=10)

def cadastrar_funcionario():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_cadastro_title = tk.Label(frame_main, text="Cadastrar Novo Funcionário", font=("Arial", 18), bg="#ECF0F1")
    label_cadastro_title.pack(pady=20)

    labels = ["Nome", "CPF", "Telefone", "E-mail", "Idade", "Salário", "Departamento"]
    entries = {}
    
    for label_text in labels:
        frame = tk.Frame(frame_main, bg="#ECF0F1")
        frame.pack(pady=5)
        
        label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ECF0F1")
        label.pack(side="left", padx=10)

        entry = tk.Entry(frame)
        entry.pack(side="left", padx=10)
        entries[label_text] = entry

    btn_salvar = tk.Button(frame_main, text="Salvar Funcionário", bg="#27AE60", fg="white", width=20, height=2)
    btn_salvar.pack(pady=20)

def deletar_funcionario():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_deletar_title = tk.Label(frame_main, text="Deletar Funcionário", font=("Arial", 18), bg="#ECF0F1")
    label_deletar_title.pack(pady=20)

    frame = tk.Frame(frame_main, bg="#ECF0F1")
    frame.pack(pady=5)
    
    label = tk.Label(frame, text="ID do Funcionário", font=("Arial", 12), bg="#ECF0F1")
    label.pack(side="left", padx=10)

    entry_id = tk.Entry(frame)
    entry_id.pack(side="left", padx=10)

    btn_deletar = tk.Button(frame_main, text="Deletar Funcionário", bg="#C0392B", fg="white", width=20, height=2)
    btn_deletar.pack(pady=20)

def gerenciar_projetos():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_proj_title = tk.Label(frame_main, text="Gerenciar Projetos", font=("Arial", 18), bg="#ECF0F1")
    label_proj_title.pack(pady=20)

    btn_cadastrar_proj = tk.Button(frame_main, text="Cadastrar Novo Projeto", command=cadastrar_projeto, bg="#27AE60", fg="white", width=25, height=2)
    btn_cadastrar_proj.pack(pady=10)

    btn_editar_proj = tk.Button(frame_main, text="Editar Projeto Existente", command=editar_projeto, bg="#F39C12", fg="white", width=25, height=2)
    btn_editar_proj.pack(pady=10)

    btn_excluir_proj = tk.Button(frame_main, text="Excluir Projeto", command=excluir_projeto, bg="#C0392B", fg="white", width=25, height=2)
    btn_excluir_proj.pack(pady=10)

    btn_listar_proj = tk.Button(frame_main, text="Listar Projetos", command=listar_projetos, bg="#2980B9", fg="white", width=25, height=2)
    btn_listar_proj.pack(pady=10)

def cadastrar_projeto():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame_main, text="Cadastrar Novo Projeto", font=("Arial", 18), bg="#ECF0F1")
    label_title.pack(pady=20)

    tk.Label(frame_main, text="Nome do Projeto:", bg="#ECF0F1").pack(pady=5)
    entry_nome = tk.Entry(frame_main)
    entry_nome.pack(pady=5)

    tk.Label(frame_main, text="Descrição:", bg="#ECF0F1").pack(pady=5)
    entry_desc = tk.Entry(frame_main)
    entry_desc.pack(pady=5)

    btn_salvar = tk.Button(frame_main, text="Salvar", command=lambda: salvar_projeto(entry_nome.get(), entry_desc.get()), bg="#27AE60", fg="white")
    btn_salvar.pack(pady=20)

def salvar_projeto(nome, descricao):
    # Aqui você pode implementar a lógica para salvar o projeto (ex.: adicionar a um banco de dados)
    messagebox.showinfo("Sucesso", f"Projeto '{nome}' cadastrado com sucesso!")

def editar_projeto():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame_main, text="Editar Projeto Existente", font=("Arial", 18), bg="#ECF0F1")
    label_title.pack(pady=20)

    tk.Label(frame_main, text="Nome do Projeto:", bg="#ECF0F1").pack(pady=5)
    entry_nome = tk.Entry(frame_main)
    entry_nome.pack(pady=5)

    tk.Label(frame_main, text="Nova Descrição:", bg="#ECF0F1").pack(pady=5)
    entry_desc = tk.Entry(frame_main)
    entry_desc.pack(pady=5)

    btn_salvar = tk.Button(frame_main, text="Salvar Alterações", command=lambda: salvar_alteracoes(entry_nome.get(), entry_desc.get()), bg="#F39C12", fg="white")
    btn_salvar.pack(pady=20)

def salvar_alteracoes(nome, nova_descricao):
    # Aqui você pode implementar a lógica para editar o projeto
    messagebox.showinfo("Sucesso", f"Projeto '{nome}' editado com nova descrição: '{nova_descricao}'!")

def excluir_projeto():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame_main, text="Excluir Projeto", font=("Arial", 18), bg="#ECF0F1")
    label_title.pack(pady=20)

    tk.Label(frame_main, text="Nome do Projeto:", bg="#ECF0F1").pack(pady=5)
    entry_nome = tk.Entry(frame_main)
    entry_nome.pack(pady=5)

    btn_excluir = tk.Button(frame_main, text="Excluir", command=lambda: confirmar_exclusao(entry_nome.get()), bg="#C0392B", fg="white")
    btn_excluir.pack(pady=20)

def confirmar_exclusao(nome):
    #implementar a lógica para excluir o projeto
    messagebox.showinfo("Sucesso", f"Projeto '{nome}' excluído com sucesso!")

def listar_projetos():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame_main, text="Projetos Cadastrados", font=("Arial", 18), bg="#ECF0F1")
    label_title.pack(pady=20)

    #implementar a lógica para listar os projetos 
    projetos = ["Projeto 1", "Projeto 2", "Projeto 3"]  # Exemplo de lista de projetos

    for projeto in projetos:
        tk.Label(frame_main, text=projeto, font=("Arial", 12), bg="#ECF0F1").pack(pady=5)

departamentos = []

def cadastrar_departamento():
    def cadastrar():
        nome_depto = entry_nome.get()
        if nome_depto:
            departamentos.append(nome_depto)
            entry_nome.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Departamento cadastrado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira o nome do departamento.")

    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dept_title = tk.Label(frame_main, text="Cadastrar Novo Departamento", font=("Arial", 18), bg="#ECF0F1")
    label_dept_title.pack(pady=20)

    label_nome = tk.Label(frame_main, text="Nome do Departamento:", bg="#ECF0F1")
    label_nome.pack(pady=10)

    entry_nome = tk.Entry(frame_main, width=30)
    entry_nome.pack(pady=10)

    btn_cadastrar = tk.Button(frame_main, text="Cadastrar", bg="#27AE60", fg="white", command=cadastrar)
    btn_cadastrar.pack(pady=10)

def editar_departamento():
    def editar():
        novo_nome = entry_novo_nome.get()
        index = listbox_departamentos.curselection()
        if index and novo_nome:
            departamentos[index[0]] = novo_nome
            listar_departamentos()
            entry_novo_nome.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Departamento editado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, selecione um departamento e insira o novo nome.")

    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dept_title = tk.Label(frame_main, text="Editar Departamento Existente", font=("Arial", 18), bg="#ECF0F1")
    label_dept_title.pack(pady=20)

    label_select = tk.Label(frame_main, text="Selecione um Departamento:", bg="#ECF0F1")
    label_select.pack(pady=10)

    listbox_departamentos = tk.Listbox(frame_main, selectmode=tk.SINGLE)
    listbox_departamentos.pack(pady=10)

    listar_departamentos()

    label_novo_nome = tk.Label(frame_main, text="Novo Nome:", bg="#ECF0F1")
    label_novo_nome.pack(pady=10)

    entry_novo_nome = tk.Entry(frame_main, width=30)
    entry_novo_nome.pack(pady=10)

    btn_editar = tk.Button(frame_main, text="Editar", bg="#F39C12", fg="white", command=editar)
    btn_editar.pack(pady=10)

def excluir_departamento():
    def excluir():
        index = listbox_departamentos.curselection()
        if index:
            departamentos.pop(index[0])
            listar_departamentos()
            messagebox.showinfo("Sucesso", "Departamento excluído com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, selecione um departamento para excluir.")

    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dept_title = tk.Label(frame_main, text="Excluir Departamento", font=("Arial", 18), bg="#ECF0F1")
    label_dept_title.pack(pady=20)

    label_select = tk.Label(frame_main, text="Selecione um Departamento:", bg="#ECF0F1")
    label_select.pack(pady=10)

    listbox_departamentos = tk.Listbox(frame_main, selectmode=tk.SINGLE)
    listbox_departamentos.pack(pady=10)

    listar_departamentos()

    btn_excluir = tk.Button(frame_main, text="Excluir", bg="#C0392B", fg="white", command=excluir)
    btn_excluir.pack(pady=10)

def listar_departamentos():
    for widget in frame_main.winfo_children():
        if isinstance(widget, tk.Listbox):
            widget.destroy()

    listbox_departamentos = tk.Listbox(frame_main, selectmode=tk.SINGLE)
    listbox_departamentos.pack(pady=10)

    for depto in departamentos:
        listbox_departamentos.insert(tk.END, depto)

def gerenciar_departamentos():
    for widget in frame_main.winfo_children():
        widget.destroy()

    label_dept_title = tk.Label(frame_main, text="Gerenciar Departamentos", font=("Arial", 18), bg="#ECF0F1")
    label_dept_title.pack(pady=20)

    btn_cadastrar_dept = tk.Button(frame_main, text="Cadastrar Novo Departamento", bg="#27AE60", fg="white", width=25, height=2, command=cadastrar_departamento)
    btn_cadastrar_dept.pack(pady=10)

    btn_editar_dept = tk.Button(frame_main, text="Editar Departamento Existente", bg="#F39C12", fg="white", width=25, height=2, command=editar_departamento)
    btn_editar_dept.pack(pady=10)

    btn_excluir_dept = tk.Button(frame_main, text="Excluir Departamento", bg="#C0392B", fg="white", width=25, height=2, command=excluir_departamento)
    btn_excluir_dept.pack(pady=10)

    btn_listar_dept = tk.Button(frame_main, text="Listar Departamentos", bg="#2980B9", fg="white", width=25, height=2, command=listar_departamentos)
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
    ]

    for button_text, command in buttons:
        btn = tk.Button(frame_menu, text=button_text, bg="#34495E", fg="white", width=20, height=2, command=command)
        btn.pack(pady=5)

    frame_main = tk.Frame(root, bg="#ECF0F1")
    frame_main.pack(side="right", expand=True, fill="both")

    mostrar_dashboard()

    root.mainloop()

home_admin()
