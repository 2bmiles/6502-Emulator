import program
import opcodes
import convert
import re
from collections import defaultdict

def get_addressing_mode(line, symbols):
    first = line[0]
    if first == "ASL" or first == "ROL" or first == "LSR" or first == "ROR":
        return "A"
    elif first[0] == "B" and first != "BIT" and first != "BRK":
        return "rel"
    elif len(line) == 1:
        return "impl"
    second = line[1]
    if "#" in second:
        return "#"
    elif first == "JMP" and second[0] == "(":
        return "ind"
    if second[0] != "$" and second[0] != "(": # this is logic for forward references
        return "re-eval" #with just name of symbol, how do i know if it is absolute or zeropage?!?!?
                         #assume absolute,  reserve full space, flag symbol for re-evaluation :O
    # abs and zpg
    if second[0] == "$" and len(line) == 2:
        if len(second) == 3:
            return "zpg"
        elif len(second) == 5:
            return "abs"
    third = line[2]
    if second[0] == "(":
        if third[-1] == "Y":
            return "ind,Y"
        elif third[-1] == ")":
            return "X,ind"
    elif len(second) == 3 or second[3] == ",":
        if third[0] == "X":
            return "zpg,X"
        elif third[0] == "Y":
            return "zpg,Y"
    else:
        if third[0] == "X":
            return "abs,X"
        elif third[0] == "Y":
            return "abs,Y"

def parse_program(program):
    program = program.split("\n")[1:-1]
    for i, line in enumerate(program):
        program[i] = re.split(',|, | ', line)
    return program

def assemble(program):
    program = parse_program(program)
    hex_code = []
    symbols = defaultdict(str)
    current_location = 0
    re_evals = set()
    for line in program:
        if "=" in line:
            symbols[line[0]] = line[2]
        elif line[0][-1] == ":":
            symbols[line[0][:-1]] = convert.dth_address(current_location)
        else:
            for token in line:
                if token in symbols.keys():
                    line[line.index(token)] = symbols[token]
            addressing_mode = get_addressing_mode(line, symbols)
            match addressing_mode:
                case "impl":
                    current_location += 1
                case "#"|"zpg"|"zpg,X"|"zpg,Y"|"rel"|"ind,X"|"Y,ind":
                    current_location += 2
                case "abs"|"abs,X"|"abs,Y"|"ind":
                    current_location += 3
                case "re-eval":
                    current_location += 3
                    re_evals.add(line[1])
    current_location = 0
    for line in program:
        # reminder to take care of comments
        if "=" not in line and line[0][-1] != ":":
            for token in line:
                if token in symbols.keys():
                    line[line.index(token)] = symbols[token]
            first = line[0]
            if first == "JMP" or first == "JSR":
                if len(line[1]) == 3:
                    line[1] = line[1][0] + "00" + line[1][1:]
            addressing_mode = get_addressing_mode(line, symbols)
            hex_code.append(opcodes.opcodes[(line[0], addressing_mode)])
            match addressing_mode:
                case "#":
                    if line[1][1] == "$":
                        hex_code.append(convert.add_zeroes(line[1][2:], 2))
                    else:
                        hex_code.append(convert.dth_byte(int(line[1][1:]))[1:])
                    current_location += 2
                case "impl":
                    current_location += 1
                case "ind":
                    hex_code.append(line[1][4:6])
                    hex_code.append(line[1][2:4])
                    current_location += 3
                case "abs"|"abs,X"|"abs,Y":
                    hex_code.append(line[1][3:5])
                    hex_code.append(line[1][1:3])
                    current_location += 3
                case "zpg"|"zpg,X"|"zpg,Y"|"rel":
                    hex_code.append(line[1][1:3])
                    current_location += 2
                case "X,ind"|"ind,Y":
                    hex_code.append(line[1][2:4])
                    current_location += 2
    if program[-1] != ["BRK"]:
        current_location += 1
    return hex_code, current_location

print(assemble(program.program))