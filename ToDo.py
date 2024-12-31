import customtkinter as ctk

def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text= todo)
    label.pack()
    entry.delete(0,ctk.END)

root = ctk.CTk()
root.geometry('854x580')
root.title("ToDo App")
title_label = ctk.CTkLabel(root, text = "Daily Task", font=ctk.CTkFont(size=30,weight='bold'))
title_label.pack(padx = 10, pady = (40,20))

scrollable_frame = ctk.CTkScrollableFrame (root, width=500, height= 350)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text=" Add ToDo ", width = 400 )
entry.pack(fill = 'x')

add_button = ctk.CTkButton(root, text= 'Add', width= 400, command= add_todo)
add_button.pack(pady = 30)
root.mainloop()