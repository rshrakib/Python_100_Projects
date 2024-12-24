from tkinter import *
import calendar

def showCalender():
    gui = Tk()
    gui.config(background='lightgrey')
    gui.title("Calendar for Year")
    gui.geometry('880x800')

    year = int(year_field.get())

    months = [calendar.month_name[i] for i in range(1, 13)]
    months_content = [calendar.month(year, i) for i in range(1, 13)]

    row, col = 0, 0

    for month_name, month_content in zip(months, months_content):
        month_frame = LabelFrame(gui, text=month_name, bg='lightyellow', font=('Arial', 12), padx=10, pady=10)
        month_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        month_label = Label(month_frame, text=month_content, bg='lightyellow', font=('Courier', 10), justify=LEFT)
        month_label.pack()

        col += 1
        if col == 3:
            col = 0
            row += 1

    for i in range(4):
        gui.grid_rowconfigure(i, weight=1)
    for i in range(3):
        gui.grid_columnconfigure(i, weight=1)

    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background='darkslategray')
    new.title('Calendar')
    new.geometry('350x200')

    header = Label(new, text="Calendar", bg='darkslategray', fg='white', font=('Arial', 28, 'bold'))
    header.pack(pady=10)

    instruction = Label(new, text="Enter Year:", bg='slategray', fg='white', font=('Arial', 12))
    instruction.pack(pady=5)

    year_field = Entry(new, font=('Arial', 14), justify='center', width=10)
    year_field.pack(pady=5)

    button = Button(new, text='Show Calendar', bg="mediumturquoise", fg="white", font=('Arial', 12, 'bold'), command=showCalender)
    button.pack(pady=5)

    exit_button = Button(new, text="Exit", bg="indianred", fg="white", font=('Arial', 12, 'bold'), command=new.destroy)
    exit_button.pack(pady=10)

    new.mainloop()
