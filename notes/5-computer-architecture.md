# 5. Computer Architecture

## 5.1 Computer Architecture Fundamentals

### 5.1.1 The Stored Program Concept

- stored program = lets a computer run differently depending on the loaded software program code

### 5.1.2 The von Neumann Architecture

- TODO

### 5.1.3 Memory

- memory: a series of registers
- register: stores a single binary value at a unique address
- addressing: get or set a register by address
- Random Access Memory (RAM): can access any register instantly in 1 clock cycle
- data memory: read + write to registers
- instruction memory: stores the compiled or executable version of a software program

### 5.1.4 Central Processing Unit

- Central Processing Unit (CPU):
  - runs current loaded program's instructions
  - CPU = ALU + registers + control unit
- Arithmetic Logic Unit (ALU):
  - does all basic arithmetic and logical operations
    - e.g., add(x, y), And(x, y), Equals(x, y), etc.
- Registers:
  - faster and smaller capacity memory for the CPU
  - register types:
    - data register: store values
    - address register: stores addreses that point to values in RAM
    - program counter: stores address of next instruction
    - instruction register: stores current instruction
  - Hack computer uses only 3 registers
- Control:
  - decodes microcodes of computer instructions into 1+ control bites?
- Fetch-Execute Cycle:
  - 1 ) CPU gets binary machine instruction
  - 2 ) CPU decodes instruction
  - 3 ) CPU executes instructions & gets the next instruction

### 5.1.5 Input and Output

- todo