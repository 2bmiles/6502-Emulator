import convert
import opcodes
import ram
pc = [["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"]] # program counter
ac = ["0", "0", "0", "0", "0", "0", "0", "0"] # accumulator
x = ["0", "0", "0", "0", "0", "0", "0", "0"] # x register
y = ["0", "0", "0", "0", "0", "0", "0", "0"] # y register
sr = ["0", "0", "0", "0", "0", "0", "0", "0"] # status register [NV-BDIZC]
sp = ["0", "0", "0", "0", "0", "0", "0", "0"] # stack pointer

def set_reg(reg, val):
    global pc, ac, x, y, sr, sp
    match reg:
        case "pc":
            pc = convert.htb_pc(val)
        case "ac":
            ac = convert.htb_byte(val)
        case "x":
            x = convert.htb_byte(val)
        case "y":
            y = convert.htb_byte(val)
        case "sr":
            sr = convert.htb_byte(val)
        case "sp":
            sp = convert.htb_byte(val)

def inc_reg(reg):
    joined = []
    match reg:
        case "pc":
            joined.extend(pc[0])
            joined.extend(pc[1])
        case "ac":
            joined.extend(ac)
        case "x":
            joined.extend(x)
        case "y":
            joined.extend(y)
        case "sr":
            joined.extend(sr)
        case "sp":
            joined.extend(sp)
    joined = "".join(joined)
    print(joined)
    joined = int(joined) + 1
    set_reg(reg, convert.bth(joined))

def hex_math(n1, n2, op, d = False):
    if not d:
        n1 = convert.htd(n1)
        n2 = convert.htd(n2)
    return convert.dth_byte(eval(f"{int(n1)} {op} {int(n2)}"))

def display_ram():
    print("address|value")
    for address, byte in ram.ram.items():
        print(address + "  |  " + byte)

def run_program():
    for byte in ram.ram.values():
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
                
                set_reg("pc", "0000")
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