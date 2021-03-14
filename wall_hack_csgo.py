from tkinter import *
import pymem
import re


def button_action():
    if change_button["text"] == "Start":
        change_button.configure(text="Stop")
    else:
        change_button.configure(text="Start")
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb"\x83\xF8.\x8B\x45\x08\x0F", clientModule).start() + 2

        pm.write_uchar(address, 1)
        pm.close_process()
    except:
        change_button.configure(text="Start")


gui = Tk()
gui.title("shishido")
gui.geometry("500x300")
change_button = Button(gui, text="Start", command=button_action)
change_button.place(x=100, y=50, width=300, height=100)

mainloop()
