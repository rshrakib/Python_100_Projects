import tkinter
import pyshorteners

def sorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    short_entry.insert(0,short_url)



root = tkinter.Tk()
root.title("URL Shortener")
root.geometry('400x200')
longurl_label = tkinter.Label(root, text = "Enter Long url")
longurl_entry = tkinter.Entry(root)
short_label = tkinter.Label(root, text = "Output Short URL")
short_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text="Shorten URL", bg='black', fg ="white",  command=sorten)
longurl_label.pack()
longurl_entry.pack(pady =20)

short_label.pack()
short_entry.pack(pady = 20)

shorten_button.pack()


root.mainloop()
