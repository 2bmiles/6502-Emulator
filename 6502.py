import convert
import ram
pc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # program counter
ac = [0, 0, 0, 0, 0, 0, 0, 0] # accumulator
x = [0, 0, 0, 0, 0, 0, 0, 0] # x register
y = [0, 0, 0, 0, 0, 0, 0, 0] # y register
sr = [0, 0, 1, 0, 0, 0, 0, 0] # status register [NV-BDIZC]
sp = [0, 0, 0, 0, 0, 0, 0, 0] # stack pointer