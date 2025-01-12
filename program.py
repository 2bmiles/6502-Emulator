# DO NOT INDENT, WILL BREAK
program = """
ZERO_PAGE = $80
ABS_ADDR = $2000
JMP START
SUBROUTINE:
LDA #$05
STA ZERO_PAGE
RTS
START:
LDX #$00
LOOP:
LDA $0002,X
STA ABS_ADDR,X
INX
CPX #$02
BNE LOOP
JSR SUBROUTINE
LDY #$01
LDA ($80),Y
JMP ($2000)
BRK
"""
"""
NUM2 = $6001
RESULT = $6002
JMP AFTER
ADD:
STX NUM1
STY NUM2
LDX #$2
LDA NUM1
ADC NUM2
STA RESULT,X
RTS
AFTER:
LDX #50
LDY #90
JSR ADD
TAY
NUM1 = $70
"""
"""
STA FOO
JMP BAR
FOO = $60
BAR:
BRK
"""