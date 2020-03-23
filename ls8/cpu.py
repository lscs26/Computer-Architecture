"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Create memory (256 bits)
        self.ram = [0] * 256

        # 8 general-purpose 8-bit numeric registers R0-R7
        # R5 is reserved as the interrupt mask (IM)
        # An internal switch setting that controls whether an interrupt can be processed or not. The mask is a bit that is turned on and off by the program.
        # R6 is reserved as the interrupt status (IS)
        # R7 is reserved as the stack pointer (SP)

        self.reg = [0] * 8

        self.SP = 7

        self.reg[self.SP] = 0xf4

        # Program Counter (PC)
        # Keep track of where you are on the memory stack
        self.pc = 0

        # Flag register (FL)
        # Holds the current flags status
        # These flags can change based on the operands given to the CMP opcode
        '''
        FL bits: 00000LGE
        L Less-than: during a CMP, set to 1 if registerA is less than registerB, zero otherwise.
        G Greater-than: during a CMP, set to 1 if registerA is greater than registerB, zero otherwise.
        E Equal: during a CMP, set to 1 if registerA is equal to registerB, zero otherwise.
        '''
        self.fl = 0b00000000

        # Used for generic functions for the CPU
        def LDI(operand_a, operand_b):
            self.reg[operand_a] = operand_b
            self.pc += 3

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
