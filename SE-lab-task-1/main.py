import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def read_coefficients_from_file(filename):
     """Read coefficients (a, b, c) from a text file."""
     coefficients = []
     with open(filename, 'r') as file:
         for line in file:
             try:
                 a, b, c = map(float, line.strip().split())
                 coefficients.append((a, b, c))
             except ValueError:
                 print(f"Skipping invalid line in file: {line.strip()}")
     return coefficients

def plot_temperature_model(coefficients):
     """Plot temperature models based on coefficients."""
     x = np.linspace(0, 24, 100)
     for idx, (a, b, c) in enumerate(coefficients):
         y = a * x**2 + b * x + c
         plt.plot(x, y, label=f'Temperature Model {idx + 1}')

     plt.xlabel('Time (hours)')
     plt.ylabel('Temperature (°C)')
     plt.title('Temperature Over Time')
     plt.legend()
     plt.grid(True)
     plt.show()

def open_file():
     """Open a file dialog to select coefficients file and plot temperature models."""
     filename = filedialog.askopenfilename(title="Select coefficients file", filetypes=[("Text files", "*.txt")])
     if filename:
         coefficients = read_coefficients_from_file(filename)
         if coefficients:
             plot_temperature_model(coefficients)
         else:
             print("No valid coefficients found in the file.")

def main():
     """Main function to initialize the GUI."""
     root = tk.Tk()
     root.title("Temperature Modeling Software")

     open_button = tk.Button(root, text="Open Coefficients File", command=open_file)
     open_button.pack(pady=20)

     root.mainloop()

if __name__ == "__main__":
     main()