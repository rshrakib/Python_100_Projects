import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)

    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"Text Editor - {filepath}")

def save_file():
    file_path = asksaveasfilename(
        defaultextension='txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not file_path:
        return
    with open(file_path, 'w') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {file_path}")

window = tk.Tk()
window.title("Text Editor")
window.geometry("600x400")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


txt_edit = tk.Text(window, wrap=tk.WORD, font=("Arial", 12), bg="#f9f9f9", fg="#333")
txt_edit.grid(row=0, column=1, sticky="nsew")

fr_buttons = tk.Frame(window, bg="#d9d9d9", relief=tk.RAISED, bd=2)
fr_buttons.grid(row=0, column=0, sticky="ns")

btn_open = tk.Button(fr_buttons, text="Open", command=open_file, font=("Arial", 10), bg="#4CAF50", fg="white")
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save = tk.Button(fr_buttons, text="Save As", command=save_file, font=("Arial", 10), bg="#2196F3", fg="white")
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

btn_exit = tk.Button(fr_buttons, text="Exit", command=window.quit, font=("Arial", 10), bg="#f44336", fg="white")
btn_exit.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


for i in range(3):
    fr_buttons.rowconfigure(i, minsize=40)

window.mainloop()
