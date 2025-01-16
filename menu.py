import tkinter as tk
from tkinter import ttk, messagebox

class Menu:
    def __init__(self, master):
        # Inicjalizacja menu
        self.frame_left = ttk.Frame(master, borderwidth=10, relief=tk.GROOVE)
        self.frame_left.pack(side='left', fill=tk.Y)

        #### Elementy menu ####
        # Etykiety
        self.entry_first = self.create_label_entry(self.frame_left, "Wartość początkowa")
        self.entry_last = self.create_label_entry(self.frame_left, "Wartość końcowa")

        # Lista wykresów
        self.label_type_of_char = ttk.Label(self.frame_left, text="Rodzaj wykresu")
        self.label_type_of_char.pack(pady=(3, 0))

        items = ('Wykres liniowy', 'Wykres kwadratowy')
        chart_list = tk.StringVar(value=items[0])
        self.combo = ttk.Combobox(master=self.frame_left, textvariable=chart_list, state='readonly')
        self.combo['values'] = items
        self.combo.pack(pady= (5, 30))

        # Przycisk do generowania wykresów
        self.button = ttk.Button(master=self.frame_left, text='Rysuj wykres')
        self.button.pack()

        #Autorzy
        self.authors_label = ttk.Label(
            self.frame_left, 
            text="Projekt wykonali:\nSzymon Kamiński \nAdrian Kowalewski \nFranciszek Szarwiła", 
            justify="center", 
            font=("Arial", 10, "italic")
        )
        self.authors_label.pack(side='bottom', pady=(10, 0))

    def create_label_entry(self, frame, label_text):
        #Tworzenie etykiet
        label = ttk.Label(master=frame, text=label_text)
        label.pack()
        
        entry = ttk.Entry(master=frame)
        entry.pack()

        return entry
    
    def get_values(self):
        try:
            start_value = float(self.entry_first.get())
            end_value = float(self.entry_last.get())
            chart_type = self.combo.get()
            return start_value, end_value, chart_type
        except ValueError:
            messagebox.showerror("Błąd", "Błąd danych wejściowych! Upewnij się, że podałeś poprawne liczby.")
            return None
        