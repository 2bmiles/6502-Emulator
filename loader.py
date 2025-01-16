import convert
from ram import ram

def load_program(program, location):
    program_counter = convert.htd(location[1:])
    for byte in program:
        if len(byte) == 2: # normal byte
            ram[convert.dth_address(program_counter)] = byte
        else: # relative addressing
            offset = convert.htd(byte[1:]) - (program_counter + 1)
            if 0 <= offset <= 127:
                ram[convert.dth_address(program_counter)] = convert.dth_byte(offset)
            elif -128 <= offset <= -1:
                ram[convert.dth_address(program_counter)] = convert.dth_byte(256 + offset)
            else:
                raise Exception("Relative addressing offset outside of valid range")
        program_counter += 1
    return ram