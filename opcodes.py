# (instruction, addressing mode): opcode
opcodes = {
    ("BRK", "impl"): "00", # break / interrupt
    ("ORA", "X,ind"): "01", # or with accumulator
    ("ORA", "zpg"): "05", # or with accumulator
    ("ASL", "zpg"): "06", # arithmetic shift left
    ("PHP", "impl"): "08", # push processor status onto stack
    ("ORA", "#"): "09", # or with accumulator
    ("ASL", "A"): "0A", # arithmetic shift left
    ("ORA", "abs"): "0D", # or with accumulator
    ("ASL", "abs"): "0E", # arithmetic shift left
    ("BPL", "rel"): "10", # branch on plus
    ("ORA", "ind,Y"): "11", # or with accumulator
    ("ORA", "zpg,X"): "15", # or with accumulator
    ("ASL", "zpg,X"): "16", # arithmetic shift left
    ("CLC", "impl"): "18", # clear carry
    ("ORA", "abs,Y"): "19", # or with accumulator
    ("ORA", "abs,X"): "1D", # or with accumulator
    ("ASL", "abs,X"): "1E", # arithmetic shift left
    ("JSR", "abs"): "20", # jump subroutine
    ("AND", "X,ind"): "21", # and
    ("BIT", "zpg"): "24", # bit test
    ("AND", "zpg"): "25", # and
    ("ROL", "zpg"): "26", # rotate left
    ("PLP", "impl"): "28", # pull processor status from stack
    ("AND", "#"): "29", # and
    ("ROL", "A"): "2A", # rotate left
    ("BIT", "abs"): "2C", # bit test
    ("AND", "abs"): "2D", # and
    ("ROL", "abs"): "2E", # rotate left
    ("BMI", "rel"): "30", # branch on minus
    ("AND", "ind,Y"): "31", # and
    ("AND", "zpg,X"): "35", # and
    ("ROL", "zpg,X"): "36", # rotate left
    ("SEC", "impl"): "38", # set carry
    ("AND", "abs,Y"): "39", # and
    ("AND", "abs,X"): "3D", # and
    ("ROL", "abs,X"): "3E", # rotate left
    ("RTI", "impl"): "40", # return from interrupt
    ("EOR", "X,ind"): "41", # exclusive or
    ("EOR", "zpg"): "45", # exclusive or
    ("LSR", "zpg"): "46", # logical shift right
    ("PHA", "impl"): "48", # push accumulator onto stack
    ("EOR", "#"): "49", # exclusive or
    ("LSR", "A"): "4A", # logical shift right
    ("JMP", "abs"): "4C", # jump
    ("EOR", "abs"): "4D", # exclusive or
    ("LSR", "abs"): "4E", # logical shift right
    ("BVC", "rel"): "50", # branch on oVerflow clear
    ("EOR", "ind,Y"): "51", # exclusive or
    ("EOR", "zpg,X"): "55", # exclusive or
    ("LSR", "zpg,X"): "56", # logical shift right
    ("CLI", "impl"): "58", # clear interrupt disable
    ("EOR", "abs,Y"): "59", # exclusive or
    ("EOR", "abs,X"): "5D", # exclusive or
    ("LSR", "abs,X"): "5E", # logical shift right
    ("RTS", "impl"): "60", # return from subroutine
    ("ADC", "X,ind"): "61", # add with carry
    ("ADC", "zpg"): "65", # add with carry
    ("ROR", "zpg"): "66", # rotate right
    ("PLA", "impl"): "68", # pull accumulator from stack
    ("ADC", "#"): "69", # add with carry
    ("ROR", "A"): "6A", # rotate right
    ("JMP", "ind"): "6C", # jump
    ("ADC", "abs"): "6D", # add with carry
    ("ROR", "abs"): "6E", # rotate right
    ("BVS", "rel"): "70", # branch on overflow set
    ("ADC", "ind,Y"): "71", # add with carry
    ("ADC", "zpg,X"): "75", # add with carry
    ("ROR", "zpg,X"): "76", # rotate right
    ("SEI", "impl"): "78", # set interrupt disable
    ("ADC", "abs,Y"): "79", # add with carry
    ("ADC", "abs,X"): "7D", # add with carry
    ("ROR", "abs,X"): "7E", # rotate right
    ("STA", "X,ind"): "81", # store accumulator
    ("STY", "zpg"): "84", # store Y
    ("STA", "zpg"): "85", # store accumulator
    ("STX", "zpg"): "86", # store X
    ("DEY", "impl"): "88", # decrement Y
    ("TXA", "impl"): "8A", # transfer X to accumulator
    ("STY", "abs"): "8C", # store Y
    ("STA", "abs"): "8D", # store accumulator
    ("STX", "abs"): "8E", # store X
    ("BCC", "rel"): "90", # branch on carry clear
    ("STA", "ind,Y"): "91", # store accumulator
    ("STY", "zpg,X"): "94", # store Y
    ("STA", "zpg,X"): "95", # store accumulator
    ("STX", "zpg,Y"): "96", # store X
    ("TYA", 'impl'): "98", # transfer Y to accumulator
    ("STA", "abs,Y"): "99", # store accumulator
    ("TXS", "impl"): "9A", # transfer X to stack pointer
    ("STA", "abs,X"): "9D", # store accumulator
    ("LDY", "#"): "A0", # load Y
    ("LDA", "X,ind"): "A1", # load accumulator
    ("LDX", "#"): "A2", # load X
    ("LDY", "zpg"): "A4", # load Y
    ("LDA", "zpg"): "A5", # load accumulator
    ("LDX", "zpg"): "A6", # load X
    ("TAY", "impl"): "A8", # transfer accumulator to Y
    ("LDA", "#"): "A9", # load accumulator
    ("TAX", "impl"): "AA", # transfer accumulator to X
    ("LDY", "abs"): "AC", # load Y
    ("LDA", "abs"): "AD", # load accumulator
    ("LDX", "abs"): "AE", # load X
    ("BCS", "rel"): "B0", # branch on carry set
    ("LDA", "ind,Y"): "B1", # load accumulator
    ("LDY", "zpg,X"): "B4", # load Y
    ("LDA", "zpg,X"): "B5", # load accumulator
    ("LDX", "zpg,Y"): "B6", # load X
    ("CLV", "impl"): "B8", # clear oVerflow
    ("LDA", "abs,Y"): "B9", # load accumulator
    ("TSX", "impl"): "BA", # transfer stack pointer to X
    ("LDY", "abs,X"): "BC", # load Y
    ("LDA", "abs,X"): "BD", # load accumulator
    ("LDX", "abs,Y"): "BE", # load X
    ("CPY", "#"): "C0", # compare with Y
    ("CMP", "X,ind"): "C1", # compare with accumulator
    ("CPY", "zpg"): "C4", # compare with Y
    ("CMP", "zpg"): "C5", # compare with acccumulator
    ("DEC", "zpg"): "C6", # decrement
    ("INY", "impl"): "C8", # increment Y
    ("CMP", "#"): "C9", # compare with accumulator
    ("DEX", "impl"): "CA", # decrement X
    ("CPY", "abs"): "CC", # compare with Y
    ("CMP", "abs"): "CD", # compare with accumulator
    ("DEC", "abs"): "CE", # decrement
    ("BNE", "rel"): "D0", # branch on not equal
    ("CMP", "ind,Y"): "D1", # compare with accumulator
    ("CMP", "zpg,X"): "D5", # compare with accumulator
    ("DEC", "zpg,X"): "D6", # decrement
    ("CLD", "impl"): "D8", # clear decimal
    ("CMP", "abs,Y"): "D9", # compare with accumulator
    ("CMP", "abs,X"): "DD", # compare with accumulator
    ("DEC", "abs,X"): "DE", # decrement
    ("CPX", "#"): "E0", # compare with X
    ("SBC", "X,ind"): "E1", # subtract with carry
    ("CPX", "zpg"): "E4", # compare with X
    ("SBC", "zpg"): "E5", # subtract with carry
    ("INC", "zpg"): "E6", # increment
    ("INX", "impl"): "E8", # increment X
    ("SBC", "#"): "E9", # subtract with carry
    ("NOP", "impl"): "EA", # no operation
    ("CPX", "abs"): "EC", # compare with X
    ("SBC", "abs"): "ED", # subtract with carry
    ("INC", "abs"): "EE", # increment
    ("BEQ", "rel"): "F0", # branch on equal
    ("SBC", "ind,Y"): "F1", # subtract with carry
    ("SBC", "zpg,X"): "F5", # subtract with carry
    ("INC", "zpg,X"): "F6", # increment
    ("SED", "impl"): "F8", # set decimal
    ("SBC", "abs,Y"): "F9", # subtract with carry
    ("SBC", "abs,X"): "FD", # subtract with carry
    ("INC", "abs,X"): "FE", # increment
}