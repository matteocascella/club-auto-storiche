import tkinter as tk
from tkinter import ttk, messagebox
from database import init_db, get_db
from views import GestioneSoci, GestioneAuto, GestioneEventi, GestioneTesseramenti
from datetime import date
import sqlite3

class GestionaleClubAutoStoriche:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionale Club Auto Storiche")
        self.root.geometry("800x600")

        # Inizializza il database
        init_db()

        # Crea i tab
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # Tab Soci
        self.tab_soci = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_soci, text="Soci")
        self.crea_tab_soci()

        # Tab Auto
        self.tab_auto = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_auto, text="Auto")
        self.crea_tab_auto()

        # Tab Eventi
        self.tab_eventi = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_eventi, text="Eventi")
        self.crea_tab_eventi()

    def crea_tab_soci(self):
        # Frame per l'inserimento dei soci
        frame_inserimento = ttk.LabelFrame(self.tab_soci, text="Aggiungi Socio")
        frame_inserimento.pack(padx=10, pady=10, fill="x")

        # Campi di input
        ttk.Label(frame_inserimento, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = ttk.Entry(frame_inserimento)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_inserimento, text="Cognome:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_cognome = ttk.Entry(frame_inserimento)
        self.entry_cognome.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_inserimento, text="Data Nascita:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_data_nascita = ttk.Entry(frame_inserimento)
        self.entry_data_nascita.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(frame_inserimento, text="(AAAA-MM-GG)").grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(frame_inserimento, text="Email:").grid(row=1, column=3, padx=5, pady=5)
        self.entry_email = ttk.Entry(frame_inserimento)
        self.entry_email.grid(row=1, column=4, padx=5, pady=5)

        ttk.Label(frame_inserimento, text="Telefono:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_telefono = ttk.Entry(frame_inserimento)
        self.entry_telefono.grid(row=2, column=1, padx=5, pady=5)

        # Bottone Aggiungi
        btn_aggiungi = ttk.Button(frame_inserimento, text="Aggiungi Socio", command=self.aggiungi_socio)
        btn_aggiungi.grid(row=2, column=3, padx=5, pady=5)

        # Tabella Soci
        self.tree_soci = ttk.Treeview(self.tab_soci, columns=("Nome", "Cognome", "Data Nascita", "Email", "Telefono"), show="headings")
        for col in self.tree_soci["columns"]:
            self.tree_soci.heading(col, text=col)
        self.tree_soci.pack(padx=10, pady=10, fill="both", expand=True)

        # Bottone Aggiorna Lista
        btn_aggiorna_soci = ttk.Button(self.tab_soci, text="Aggiorna Lista Soci", command=self.aggiorna_lista_soci)
        btn_aggiorna_soci.pack(padx=10, pady=5)

    def aggiungi_socio(self):
        try:
            db = next(get_db())
            nuovo_socio = GestioneSoci.aggiungi_socio(
                db, 
                self.entry_nome.get(), 
                self.entry_cognome.get(), 
                date.fromisoformat(self.entry_data_nascita.get()),
                self.entry_email.get(), 
                self.entry_telefono.get()
            )
            messagebox.showinfo("Successo", f"Socio {nuovo_socio.nome} {nuovo_socio.cognome} aggiunto!")
            self.aggiorna_lista_soci()
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def aggiorna_lista_soci(self):
        # Pulisce la tabella
        for i in self.tree_soci.get_children():
            self.tree_soci.delete(i)
        
        # Ottiene la lista dei soci
        db = next(get_db())
        soci = GestioneSoci.lista_soci
