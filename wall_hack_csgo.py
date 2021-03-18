from tkinter import *
import pymem
import re


def wallhack_action():
    if wallhack_button["text"] == "Start Wallhack":
        wallhack_button.configure(text="Stop Wallhack")
    else:
        wallhack_button.configure(text="Start Wallhack")
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')
        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb"\x83\xF8.\x8B\x45\x08\x0F", clientModule).start() + 2
        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()
    except:
        wallhack_button.configure(text="Start Wallhack")


def radar_action():
    if radar_button["text"] == "Start Radar":
        radar_button.configure(text="Stop Radar")
    else:
        radar_button.configure(text="Start Radar")
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')
        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb"\x80\xB9.{5}\x74\x12\x8B\x41\x08", clientModule).start() + 6
        pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
        pm.close_process()
    except:
        radar_button.configure(text="Start Radar")


gui = Tk()
gui.title("shishido")
gui.geometry("500x300")
wallhack_button = Button(gui, text="Start Wallhack", command=wallhack_action)
wallhack_button.place(x=100, y=50, width=300, height=100)

radar_button = Button(gui, text="Start Radar", command=radar_action)
radar_button.place(x=100, y=150, width=300, height=100)

mainloop()
