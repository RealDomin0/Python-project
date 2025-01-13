import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Chart:
    def __init__(self, master, menu_instance):

        self.menu = menu_instance

        # Inicjalizacja okna wykresu
        self.frame_right = ttk.Frame(master)
        self.frame_right.pack(side='right', fill=tk.BOTH, expand=True)

        # Tworzenie wykresu
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_right)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Dodanie paska narzędzi
        self.toolbar_frame = ttk.Frame(master=self.frame_right)
        self.toolbar_frame.pack(fill=tk.X)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()

    def draw_chart(self):
        # Pobranie danych
        values = self.menu.get_values()
        if values:
            x_start, x_end, chart_type = values

            x = [x_start + i * (x_end - x_start) / 100 for i in range(101)]
            if chart_type == 'Wykres liniowy':
                y = x
            elif chart_type == 'Wykres kwadratowy':
                y = [xi ** 2 for xi in x]

            # Rysowanie wykresu
            self.ax.clear()
            self.ax.plot(x, y)
            self.canvas.draw()

        else:
            print("Błąd w danych wejściowych")