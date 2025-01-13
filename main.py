import tkinter as tk
from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from menu import Menu
from chart import Chart


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Program do generowania wykresów")
        
        # Utworzenie obiektów menu i wykresu
        self.menu = Menu(self.root)
        self.chart = Chart(self.root, self.menu)

        #Ustawienie funkcji przycisku
        self.menu.button.config(command=self.chart.draw_chart)

        # Ustawienie funkcji zamykania okna
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """Zamyka aplikację przy kliknięciu na przycisk X."""
        self.root.quit()
        self.root.destroy()


# Ustawienia okna
root = tk.Tk()

# Tworzymy aplikację
app = Application(root)

# Pętla do uruchamiania okna
root.mainloop()