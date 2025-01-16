import convert
import opcodes
from ram import ram
pc = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]] # program counter
ac = [0, 0, 0, 0, 0, 0, 0, 0] # accumulator
x = [0, 0, 0, 0, 0, 0, 0, 0] # x register
y = [0, 0, 0, 0, 0, 0, 0, 0] # y register
sr = [0, 0, 1, 0, 0, 0, 0, 0] # status register [NV-BDIZC]
sp = [0, 0, 0, 0, 0, 0, 0, 0] # stack pointer

def display_ram():
    print("address|value")
    for address, byte in ram.items():
        print(address + "  |  " + byte)

def run_program():
    for byte in ram.values():
        instruction = opcodes.reversed_opcodes[byte]
        print(instruction)
        match instruction[1]:
            case "A":
                pass
            case "abs":
                pass
            case "abs,X":
                pass
            case "abs,Y":
                pass
            case "#":
                pass
            case "impl":
                pass
            case "ind":
                pass
            case "X,ind":
                pass
            case "ind,Y":
                pass
            case "rel":
                pass
            case "zpg":
                pass
            case "zpg,X":
                pass
            case "xpg,Y":
                pass