import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import loader
import assembler
import ram
import CPU
from convert import dth_address

def display_ram():
    ram_display.config(state=tk.NORMAL)
    ram_display.delete(1.0, tk.END)
    for i in range(4096):
        ram_display.insert(tk.END, dth_address(i * 16) + " ")   
        for j in range(2):
            for k in range(8):
                ram_display.insert(tk.END, f" {ram.ram[dth_address((i * 16) + (k + (8 * j)))]}")
            ram_display.insert(tk.END, " ")
        ram_display.insert(tk.END, "\n")
    ram_display.config(state=tk.DISABLED)

def assemble_program():
    where_to_load = location.get()
    pc_initialize = reset_vector.get()
    loader.load_program(assembler.assemble(f"\n{code_window.get(0.0, tk.END)}"), where_to_load, pc_initialize)
    display_ram()

def limit_location_text(var, index, mode):
    if len(location_text.get()) > 4:
        location_text.set(location_text.get()[:4])

def limit_reset_vector_text(var, index, mode):
    if len(reset_vector_text.get()) > 4:
        reset_vector_text.set(reset_vector_text.get()[:4])

window = tk.Tk()
window.title("6502 Emulator")
code_frame = tk.Frame()
buttons = tk.Frame()

# toolbar
run = tk.Button(master=buttons, command=CPU.run_program, text="Run program")
run.pack(side=tk.LEFT)

assemble = tk.Button(master=buttons, command=assemble_program, text="Assemble and load")
assemble.pack(side=tk.LEFT)

location_label = tk.Label(master=buttons, text="Location $", font=("Courier", 11))
location_label.pack(side=tk.LEFT)
location_text = tk.StringVar()
location_text.set("0000")
location_text.trace_add("write", limit_location_text)
location = tk.Entry(master = buttons, width=4, textvariable=location_text, font=("Courier", 11))
location.pack(side=tk.LEFT)

reset_vector_label = tk.Label(master=buttons, text="Reset Vector $", font=("Courier", 11))
reset_vector_label.pack(side=tk.LEFT)
reset_vector_text = tk.StringVar()
reset_vector_text.set("0000")
reset_vector_text.trace_add("write", limit_reset_vector_text)
reset_vector = tk.Entry(master = buttons, width=4, textvariable=reset_vector_text, font=("Courier", 11))
reset_vector.pack(side=tk.LEFT)

# code interface
code_window = ScrolledText(master=code_frame, width=50, height=26)
code_window.pack(side=tk.LEFT)

ram_display = ScrolledText(master=code_frame, width=56, font=("Courier", 11), state=tk.DISABLED)
ram_display.pack(side=tk.RIGHT)

buttons.pack(fill="x")
code_frame.pack(side=tk.BOTTOM)

display_ram()
window.mainloop()