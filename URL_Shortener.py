import pyperclip
import pyshorteners

from tkinter import *

root = Tk()

root.title("URL Shortener")
root.configure(bg="#FFFF69")

url = StringVar()
url_address = StringVar()

def url_shortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)

def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="URL Shortener Using Python", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=url_shortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command=copy_url).pack(pady=5)

root.mainloop()
