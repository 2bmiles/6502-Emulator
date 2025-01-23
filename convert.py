hex_characters = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def btd(binary):
    binary = str(binary)
    result = 0
    for i in range(len(binary)):
        if binary[-1-i] == "1":
            result += 2**i
    return result
def htd(hexadecimal):
    hexadecimal = str(hexadecimal)
    result = 0
    for i in range(len(hexadecimal)):
        result += 16**i * hex_characters[hexadecimal[-1-i]]
    return result
def dtb(decimal):
    result = ""
    powers_of_two = 1
    if decimal == 0:
        result = "0"
    else:
        while powers_of_two <= decimal:
            powers_of_two *= 2
        while powers_of_two != 1:
            powers_of_two /= 2
            if powers_of_two <= decimal:
                decimal -= powers_of_two
                result += "1"
            else:
                result += "0"
    return result
def dth(decimal):
    result = ""
    powers_of_sixteen = 1
    if decimal == 0:
        result = "0"
    else:
        while powers_of_sixteen <= decimal:
            powers_of_sixteen *= 16
        while powers_of_sixteen != 1:
            powers_of_sixteen /= 16
            power_counter = 0
            while decimal >= 0:
                decimal -= powers_of_sixteen
                power_counter += 1
            decimal += powers_of_sixteen
            power_counter -= 1
            result += hex_characters[power_counter]
    return result
def bth(binary):
    return dth(btd(binary))
def htb(hexadecimal):
    return dtb(htd(hexadecimal))
def add_zeroes(str, target_len):
    return "0"*(target_len-len(str)) + str
def dth_address(decimal):
    decimal = dth(decimal)
    decimal = "$" + add_zeroes(decimal, 4)
    return decimal
def dth_byte(decimal):
    decimal = dth(decimal)
    decimal = add_zeroes(decimal, 2)
    return decimal
def htb_pc(address):
    pc = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]]
    if address[0] == "$":
        address = address[1:]
    address_bin = add_zeroes(htb(address), 16)
    for i in range(2):
        for j in range(8):
            pc[i][j] = address_bin[i*8+j]
    return pc
def htb_byte(byte):
    return_byte = ["", "", "", "", "", "", "", ""]
    if byte[0] == "$":
        byte = byte[1:]
    byte_bin = add_zeroes(htb(byte), 8)
    for j in range(8):
        return_byte[j] = byte_bin[j]
    return return_byte