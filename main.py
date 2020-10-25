from tkinter import Tk, Label
import ctypes


fenster = Tk()
fenster.title("no_screensaver")
info_label = Label(fenster, text="Programm geöffnet lassen, um no_screensaver zu verwenden.")
info_label.pack()
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
fenster.mainloop()
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
