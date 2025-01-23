import opcodes
import convert
import re
from collections import defaultdict

def get_addressing_mode(line):
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
    elif first == "JMP" or first == "JSR":
        return "abs"
    if second[0] != "$" and second[0] != "(":
        return "label"
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
    labels = defaultdict(str)
    variables = defaultdict(str)
    current_location = 0
    # first pass
    for line in program:
        if "=" in line:
            variables[line[0]] = line[2]
    # second pass
    for line in program:
        if line[0][-1] == ":":
            labels[line[0][:-1]] = convert.dth_address(current_location)
        elif "=" not in line:
            for token in line:
                if token in labels.keys():
                    line[line.index(token)] = labels[token]
                if token in variables.keys():
                    line[line.index(token)] = variables[token]
            addressing_mode = get_addressing_mode(line)
            match addressing_mode:
                case "impl"|"A":
                    current_location += 1
                case "#"|"zpg"|"zpg,X"|"zpg,Y"|"rel"|"ind,X"|"Y,ind":
                    current_location += 2
                case "abs"|"abs,X"|"abs,Y"|"ind"|"label":
                    current_location += 3
    # third pass
    current_location = 0
    for line in program:
        # reminder to take care of comments
        if "=" not in line and line[0][-1] != ":":
            for token in line:
                if token in labels.keys():
                    line[line.index(token)] = labels[token]
                if token in variables.keys():
                    line[line.index(token)] = variables[token]
            first = line[0]
            if first == "JMP" or first == "JSR":
                if len(line[1]) == 3:
                    line[1] = line[1][0] + "00" + line[1][1:]
            addressing_mode = get_addressing_mode(line)
            hex_code.append(opcodes.opcodes[(line[0], addressing_mode)])
            match addressing_mode:
                case "#":
                    if line[1][1] == "$":
                        hex_code.append(convert.add_zeroes(line[1][2:], 2))
                    else:
                        hex_code.append(convert.dth_byte(int(line[1][1:])))
                    current_location += 2
                case "impl"|"A":
                    current_location += 1
                case "ind":
                    if line[1][1] == "$":
                        hex_code.append(line[1][4:6])
                        hex_code.append(line[1][2:4])
                    else:
                        hex_code.append(variables[line[1][1:-1]][3:5])
                        hex_code.append(variables[line[1][1:-1]][1:3])
                    current_location += 3
                case "X,ind":
                    if line[1][1] == "$":
                        hex_code.append(line[1][2:4])
                    else:
                        hex_code.append(variables[line[1][1:]][1:3])
                    current_location += 2
                case "ind,Y":
                    if line[1][1] == "$":
                        hex_code.append(line[1][2:4])
                    else:
                        hex_code.append(variables[line[1][1:-1]][1:3])
                    current_location += 2
                case "abs"|"abs,X"|"abs,Y":
                    hex_code.append(line[1][3:5])
                    hex_code.append(line[1][1:3])
                    current_location += 3
                case "zpg"|"zpg,X"|"zpg,Y":
                    hex_code.append(line[1][1:3])
                    current_location += 2
                case "rel": # insert placeholder for loader
                    hex_code.append(line[1])
                    current_location += 2
    return hex_code