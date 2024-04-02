import tkinter as tk

window = tk.Tk()
window.title("Exemple de GUI")

window.geometry("800x600")

label = tk.Label(window, text="Hello World!")
label.config(font=("Arial", 40))
label.config(fg="blue")

label.pack()

window.mainloop()
