# 5. Computer Architecture

## 5.1 Computer Architecture Fundamentals

### 5.1.1 The Stored Program Concept

- stored program = lets a computer run differently depending on the loaded software program code

### 5.1.2 The von Neumann Architecture

- diagram:
```
         +------------------------------------------------+
         | Memory                   CPU                   |
         | +------------------+     +-------------------+ |
         | | +--------------+ |     | registers +---    | |
         | | | instructions | |     |  _______  |   \   | |
input -> | | + +------------+ | <-> | |_______| |    \  | | -> output
         | | +--------------+ |     |  _______  |     | | |
         | | | data         | |     | |_______| | ALU | | | 
         | | +--------------+ |     |    ...    |     | | |
         | +------------------+     |  _______  |    /  | |
         |                          | |_______| |   /   | |
         |                          |           +---    | |
         |                          +-------------------+ |
         +------------------------------------------------+
```

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

- computers talk to input and output (i.e., I/O) devices via memory-mapped I/O
- I/O device examples: screens, keyboards, storage devices, etc.
- memory-mapped I/O:
  - makes any I/O device look the same to the computer by translating into a binary emulation as a section in the computer memory
  - requirements:
    - 1 ) input data to I/O device is serialized onto computer memory
    - 2 ) I/O device supports an interaction protocol that programs can use to manage the device
- mental model of computer to I/O device connections:
  ```
  I/O device <-> memory map <-> device driver <-> computer
  ```

## 5.2 The Hack Hardware Platform: Specification

### 5.2.1 Overview

- Hack computer platform:
  - 16-bit von Neumann machine
  - runs Hack assembly machine language programs
  - composition =
    - CPU +
    - instruction memory +
    - data memory +
    - screen +
    - keyboard
- instruction memory: loads Hack program
  - composition = ROM (Read-Only Memory) chip 
- CPU:
  - composition = 
    - ALU +
    - Data register (D) +
    - Address register (A) +
    - Program Counter (PC)

### 5.2.2 Central Processing Unit

- CPU logic gate diagram:
```
                             +-----\
data memory -> inM --------->|     | -> outM  ----\
               (16-bit)      |     |    (16-bit)  |
instruction -> instruction ->|     | -> writeM ---|-> data memory
memory         (16-bit)      | CPU |    (1-bit)   |
                             |     | -> addressM -/
               reset ------> |     |    (15-bit)
               (1-bit)       |     | -> pc -> instruction memory
                             +-----/    (15-bit)
```

- Hack CPU interface:
```
Chip Name: CPU
Input:
  instructions[16]  // Instruction to execute
  inM[16]           // The instruction's M input (contents of RAM[A])
  reset             // Signals whether to restart the program (if
                    // reset == 1)
                    // or continue executing the program (if
                    // reset == 0)
Output:
  outM[16]          // Written to RAM[addressM], the instruction's M
                    // output
  addressM[15]      // At which address to write?
  writeM            // Write to the memory?
  pc[15]            // Address of next instruction
```

### 5.2.3 Instruction Memory

- Hack instruction memory interface:
```
Chip Name: ROM32K
Input:     address[15]
Output:    out[16]
Function:  Emits the 16-bit value stored in the address selected by
           the `address` input. It is assumed that the chip is preloaded
           with a program written in the Hack machine language.
```

### 5.2.4 Input / Output

- overview:
```
keyboard <-> keyboard memory map <-\
                                   |-> data memory (RAM) <-> CPU
screen <-> screen memory map <-----/
```
  - built-in `Screen` chip is the screen memory map
  - built-in `Keyboard`chip is the keyboard memmory map

- `Screen`: an 8K (8192) memory chip of 16-bit registers
  - resolution: 512 x 256 (width x height) pixels
  - pixels are in chunks of 16-bit words
- Hack `Screen` chip interface:
```
Chip Name: Screen       // Screen memory map
Input:     in[16]       // What to write
           address[13]  // Were to read / write
           load         // Write-enable bit
Output:    out[16]      // Screen value at the given address
Function:  Exactly like a 16-bit, 8K RAM, plus a screen refresh 
           side effect.
           Emits the value stored at the memory location specified
           by `address`.
           If `load` == 1, then the memory address specified by 
           `address` is set to the value of `in`.
           The loaded value will be omitted by `out` from the next
           time step onward.
           In addition, the chip continuously refreshes a physical
           screen, consisting of 256 rows and 512 columns of black
           and white pixels.com
           The pixel at row r from the top and the column c from the
           left (0 <= r <= 255, 0 <= c <= 511) is mapped onto the 
           c % 16 bit (count from LSB to MSB) of the 16-bit word stored
           in `Screen`[r * 32 + c / 16].
           (Simulators of the Hack computer are expeceted to simulate
           the physical screen, the mapping, and the refresh contract).
```

- `Keyboard`: a read-only, 16-bit register
  - keyboard key press -> `Keyboard` chip sets `output` to a 16-bit code

- Hack `keyboard` chip interface:
```
Chip Name: Keyboard // Keyboard memory map
Output:    out[16]
Function:  Emits the 16-bit character code of the currently pressed
           key on the physical keyboard or 0 if no key is pressed
(Simulators of the Hack computer are expected to simulate this refresh
contract).
```

### 5.2.5 Data Memory

- `Memory` chip: stores the address + values in the Hack data memory
  - chip composition = `RAM16K` + `Screen` + `Keyboard`
- Hack `Memory` chip interface:
```
Chip Name: Memory       // Data memory
Input:     in[16]       // What to write
           address[15]  // Where to read / write
           load         // Write-enable bit
Output:    out[16]      // Value at the given address
Function:  The complete address space of the Hack computer's data
           memory.
           Only the top 16K + 8K + 1 words of the address space are 
           used.
           Accessing an address in the range 0 - 16383 results in 
           accessing `RAM16K`;
           Accessing an address in the range 16384 - 24575 results in
           accessing `Screen`;
           Accessing the address 24576 results in accessing `Keyboard`;
           Accessing any other address is invalid.
```

### 5.2.6 Computer

- mental model:
```
reset -> Computer <-+-> Screen
                    |
                    \-- Keyboard
```

- Hack `Computer`chip interface:
```
Chip Name: Computer
Input:     reset
Function:  When `reset` == 0, the program stored in the computer
           executes.
           When `reset` == 1, the execution of the program restarts.
           To start the program's execution, set `reset` to 1, and
           then to 0.
           (It is assumed that the computer's instruction memory is
           loaded with a program written in the Hack manchine
           language).
```

- starting the program is "booting the computer"
- computer boot process / order:
  - 1 ) boot machine
  - 2 ) machine runs firmware program in ROM
  - 3 ) firmware loads OS kernel in RAM
  - 4 ) OS kernel runs a process that manages I/O devices
  - 5 ) user input triggers OS to run some other process
- compiler:
  - a program that translates a high level programming language into a lower level machine language

## 5.3 Implementation

### 5.3.1 The Central Processing Unit

- CPU functions:
  - runs a Hack instruction
  - gets & finds next instruction to run
- sub-chip composition:
  - ALU
  - A register
  - D register
  - 2 x Mux16
  - PC
- instruction decoding:
  - TODO
- instruction execution:
  - TODO
- instruction fetching:
  - TODO

### 5.3.2 Memory

- `Memory` chip is in figure 5.6 (from section 5.2.5 Data Memory)

### 5.3.3 Computer

- sub-chip composition:
  - ALU
  - Memory
  - ROM32K
