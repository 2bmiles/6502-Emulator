import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import loader
import assembler
import ram
from convert import dth_address

def display_ram():
    ram_display.config(state=tk.NORMAL)
    for i in range(4096):
        ram_display.insert(tk.END, dth_address(i * 16) + " ")
        for j in range(2):
            for k in range(8):
                ram_display.insert(tk.END, f" {ram.ram[dth_address((i * 16) + (k + (8 * j)))]}")
            ram_display.insert(tk.END, " ")
        ram_display.insert(tk.END, "\n")
    ram_display.config(state=tk.DISABLED)

def assemble_program():
    loader.load_program(assembler.assemble(f"\n{code_window.get(0.0, tk.END)}"), "$0000")
    display_ram()

window = tk.Tk()
window.title("6502 Emulator")
code_frame = tk.Frame(highlightbackground="black", highlightthickness=1)

assemble = tk.Button(command=assemble_program, text="Assemble")
assemble.pack(side=tk.TOP)

code_window = tk.Text(master=code_frame, width=50)
code_window.pack(side=tk.LEFT)

ram_display = ScrolledText(master=code_frame, width=56, font=("Courier", 11), state=tk.DISABLED)
ram_display.pack(side=tk.RIGHT)

code_frame.pack(side=tk.BOTTOM)

window.mainloop()