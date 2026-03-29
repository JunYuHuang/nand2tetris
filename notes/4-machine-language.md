# 4. Machine Language

## 4.1 Machine Language: Overview

### 4.1.1 Hardware Elements

- `machine language` = code that controls memory via a processor + a register set
- `memory` = continuous cell series in hardware that stores data in a computer
  - AKA locations, memory registers accessible by address
- `processor` = device that does certain primitive operations
  - AKA CPU = Central Processing Unit
  - CPU = ALU + a register set + gate logic
- `registers` = faster and lower capacity memory chips within a CPU
  - 2 types:
    - `data registers` = holds data values
    - `address registers` = holds data or memory address values

### 4.1.2 Languages

- can write machine programs in binary or symbolic language
- `assembly languages`: symbolic language for writing machine programs
  - are highly CPU chip hardware specific
- `assemblers`: programs that translate assembly language programs into binary code
- example:
  ```
  Addition Operation  -> 101011
  Register R1         -> 00001
  Register R2         -> 00010
  set R1 to (R1 + R2) -> 1010110001000001
  ```

### 4.1.3 Instructions:

- arithmetic and logical operations:
  - e.g., +, -, AND, OR, NOT
    ```
    // Adds up two numbers
    load R1,17    // R1 <- 17
    load R2,4     // R2 <- 4
    add  R1,R1,R2 // R1 <- R1 + R2

    // Computes a logical opreation:
    load R1,true    // R1 <- binary representation of true
    load R2,false   // R2 <- binary representation of false
    and  R1,R1,R2   // R1 <- R1 And R2 (bit-wise And)
    ```  
- memory access: access and update memory locations
  - e.g., set memory location 17 to the value 1 =
    ```
    load A,17
    load M,1
    ```
- flow control: sequential execution + jumps (i.e., goto)
- symbols
  - relocatable: low-level code that omits physical addresses
  - e.g., symbolic addresses
    ```
    // Sets R1 to 0+1+2, ...
      load R1,0
    (LOOP)
      add R1,R1,1
      ...
      goto LOOP
      ...
    ```

## 4.2 The Hack Machine Language

### 4.2.1 Background

- Hack computer design:
  - follows the von Neumann architecture hardware pattern
  - is 16-bit; works with chunks of 16-bit values
- `memory`:
  - Hack memory = data memory + instruction memory
  - each memory unit:
    - is 16-bits wide; each memory address stores a 16-bit binary value or number
    - has a 15-bit address space; contains 2^15 = ~32K 16-bit words / binary values
  - `data memory` = RAM; Random Access Memory
    - a read / write device
    - always has 1 selected register `M`
  - `instruction memory` = ROM; Read Only Memory
    - a read-only device
    - always has 1 selected register `instruction`
- `registers`:
  - 3 16-bit registers are controlled by Hack instructions:
    - `D` = data register; stores a 16-bit value
    - `A` = address register; is an address + data register
    - `M` = data memory register
  - e.g.,
    ```
    // set `D` register to value 17
    @17
    D=A
    ```
- `addressing`:
  - setting the `A` register to value `xxx`:
    - -> sets `M` and `instruction` registers to `xxx`
  - example Hack instructions:
    ```
    // Set `RAM[100]` to 17:
    @17
    D=A
    @100
    M=D

    // Set `RAM[100]` to `RAM[200]`'s value:
    @200
    D=M
    @100
    M=D
    ```
- `branching`:
  - Hack supports both unconditional and conditional branching (i.e., if statements)
  - e.g.,
    ```
    // Execute instruction number 29
    @29
    0;JMP

    // if D == 0, goto 52
    @62
    D;JEQ
    ```
  - `A` register does 2 things:
    - 1 ) uses `M` + ignores `instruction` register OR
    - 2 ) uses `instruction` + ignores `m` register
- `variables`:
  - Hack supports constants and symbols (variables)
  - Hack assembly language syntax:
    ```
    // sets register `A` to the constant value or variable `xxx`
    @xxx
    ```
  - e.g., 
    ```
    // set x = 17
    // "select RAM register at address equal to symbol `x`'s bound value"
    // "set that RAM register to the value `17`"
    @17
    D=A,
    @x
    M=D

    // increment `count` by 1
    @count
    M=M+1
    ```
  - has 16 virtual registers / variables set to values corresponding to their numbering e.g., `R0 = 0`:
    - `R0, R1, ..., R15` 
- memory access examples:
  ```
  // D = 17
  @17
  D=A

  // RAM[100] = 17
  @17
  D=A
  @100
  M=D

  // RAM[100] = RAM[200]
  @200
  D=M
  @100
  M=D
  ```
- branching examples:
  ```
  // goto 29
  @29
  0;JMP

  // if D>0 goto 63
  @63
  D;JGT
  ```
- variables use examples:
  ```
  // x = -1
  @x
  M=-1

  // count = count - 1
  @count
  M=M-1

  // sum = sum + x
  @sum
  D=M
  @x
  D=D+M
  @sum
  M=D
  ```

### 4.2.2 Program Example

- algorithm for brute-force addition for calculating the sum:
  - 1 + 2 + 3 + ... + n, for a value `n`
- pseudocode:
  ```
  // Program: Sum1ToN
  // Computes RAM[1] = 1 + 2 + 3 + ... + RAM[0]
  // Usage: put a value >= 1 in RAM[0]
    i = 1
    sum = 0
  LOOP:
    if (if > R0) goto STOP
    sum = sum + i
    i = i + 1
    goto LOOP
  STOP:
    R1 = sum
  ```
- Hack assembly coded:
  ```asm
  // File: Sum1ToN.asm
  // Computes RAM[1] = 1 + 2 + 3 + ... + RAM[0]
  // Usage: put a value >= 1 in RAM[0]
    // i = 1
    @i
    M=1
    
    // sum = 0
    @sum
    M=0
  (LOOP)
    // if (i > R0) goto STOP
    @i
    D=M
    @R0
    D=D-M
    @STOP
    D;JGT
    
    // sum = sum + i
    @sum
    D=M
    @i
    D=D+M
    @sum
    M=D
  
    // i = i + 1
    @i
    M=M+1

    // goto LOOP
    @LOOP
    0;JMP
  (STOP)
    // R1 = sum
    @sum
    D=M
    @R1
    M=D
  (END)
    @END
    0;JMP
  ```
- `RAM[0]` = `R0`, `RAM[1]` = `R1`

### 4.2.3 The Hack Language Specification

- A-instruction:
  - syntax:
    ```
    Symbolic:
    @xxx              (xxx is a decimal value ranging from 0 to
                      32767, or a symbol bound to such a 
                      decimal value)
    
    Binary:
    0 vvvvvvvvvvvvvvv (vv ... v = 15-bit value of xxx)
    ```
  - sets `A` register to a 16-bit value composed of:
    - 1 ) an operation code (AKA op-code) via the leftmost bit
    - 2 ) a 15-bit non-negative binary number value
  - 3 functions:
    - 1 ) allows inputting constant values
    - 2 ) sets `A` register to a RAM register's address -> sets up prereqs for a C-instruction
    - 3 ) sets `A` register to jump destination's address -> sets up prereq for another C-instruction

- C-instruction:
  - syntax:
    ```
    Symbolic:
    dest = comp ; jump     (comp is mandatary.
                           If dest is empty, the = is omitted;
                           If jump is empty, the ; is omitted)

    Binary:
    111accccccdddjjj


         comp      c c c c c c
    -------+-----+------------
    0      |     | 1 0 1 0 1 0
    1      |     | 1 1 1 1 1 1
    -1     |     | 1 1 1 0 1 0
    D      |     | 0 0 1 1 0 0
    A      | M   | 1 1 0 0 0 0
    !D     |     | 0 0 1 1 0 1
    !A     | !M  | 1 1 0 0 0 1
    -D     |     | 0 0 1 1 1 1
    -A     | -M  | 1 1 0 0 1 1
    D+1    |     | 0 1 1 1 1 1
    A+1    | M+1 | 1 1 0 1 1 1
    D-1    |     | 0 0 1 1 1 0
    A-1    | M-1 | 1 1 0 0 1 0
    D+A    | D+M | 0 0 0 0 1 0
    D-A    | D-M | 0 1 0 0 1 1
    A-D    | M-D | 0 0 0 1 1 1
    D&A    | D&M | 0 0 0 0 0 0
    D|A    | D|M | 0 1 0 1 0 1
    -------+-----+------------
    a == 0  a == 1


    dest   d d d  Effect: store comp in:
    -----+-------+-------------------------
    null | 0 0 0 | the value is not stored 
    M    | 0 0 1 | RAM[A]
    D    | 0 1 0 | D register (reg)
    DM   | 0 1 1 | D reg and RAM[A]
    A    | 1 0 0 | A reg
    AM   | 1 0 1 | A reg and RAM[A]
    AD   | 1 1 0 | A reg and D reg
    ADM  | 1 1 1 | A reg, D reg, and RAM[A]
    -----+-------+-------------------------


    jump   j j j  Effect:
    -----+-------+-------------------
    null | 0 0 0 | no jump
    JGT  | 0 0 1 | if comp > 0 jump
    JEQ  | 0 1 0 | if comp = 0 jump
    JGE  | 0 1 1 | if comp >= 0 jump
    JLT  | 1 0 0 | if comp < 0 jump
    JNE  | 1 0 1 | if comp != 0 jump
    JLE  | 1 1 0 | if comp <= 0 jump
    JMP  | 1 1 1 | unconditional jump
    -----+-------+-------------------
    ```
  - does 3 things:
    - 1 ) `comp`: what to compute (i.e., ALU operation)
    - 2 ) `dest`: where to store computed value
    - 3 ) `jump`: what to do next
  - computation specification (comp):
    - are these 7 bits in the C-instruction binary:
      ```
      111accccccdddjjj
         ^     ^
         |_____|
          comp 
      ```
    - how the memory / registers feed into the ALU:
      ```
      D register -----------------------> x -\
                                             |
      A register ---------------------\      |-> ALU -> out
      (if C-instruction's a-bit is 0) |      |
                                      |-> y -/
      M register ---------------------/
      (if C-instruction's a-bit is 1)
      ```
    - example assembly language operations:
      - `D-1` does `D`-register's value minus 1
      - `D|M` does `D`-register's value OR'd with `M`-register's value
  - destination specification (dest):
    - are these 3 bits in the C-instruction binary:
      ```
      111accccccdddjjj
                ^ ^
                |_|
                dest 
      ```
    - sets where to store the output of the ALU: 0 to 3 options
      - if 1st `d` bit is 1 -> stores output in `A` register
      - if 2nd `d` bit is 1 -> stores output in `D` register
      - if 3rd `d` bit is 1 -> stores output in `M` register
  - jump directive (jump):
    - are these 3 bits in the C-instruction binary:
      ```
      111accccccdddjjj
                   ^ ^
                   |_|
                   jump 
      ```
    - sets what do next:
      - 1 ) read + run the next instruction OR
      - 2 ) read + run another instruction (stored in `A`-register)
    - if 1st `j` bit is 1 -> jump (option 2) if output < 0
    - if 2nd `j` bit is 1 -> jump (option 2) if output = 0
    - if 3rd `j` bit is 1 -> jump (option 2) if output > 0
    - unconditional goto syntax: `0;JMP`
  - preventing A register use conflicts:
    - because running `@n` sets both `RAM[n]` and `ROM[n]`
    - best practice:
      - 1 ) set `M`-register referenced C-instruction with no jump OR
      - 2 ) set C-instruction with jump and no `M`-register ref

### 4.2.4 Symbols

- 3 symbol types:
  - predefined symbols = special memory addresses
  - label symbols = goto instruction destinations
  - variable symbols = variables
- predefined symbols:
  - `R0`, `R1`, ..., `R15`:
    - constants bound to integer values 0 to 15
    - use as ready-made working variables AKA virtual registers
  - `SP`, `LCL`, `ARG`, `THIS`, `THAT`:
    - are constants bound to integers 0, 1, ..., 4 respectively
  - `SCREEN`, `KBD`:
    - for reading (input) and displaying (output) data
    - bounds to integers 16384 and 24576 respectively
- label symbols: like keyword functions
  - the set: `LOOP`, `STOP`, `END`
  - writing convention: all uppercase
  - syntax: `(xxx)`
- variable symbols: normal variables
  - writing convention: all lowercase
  - syntax: `xxx`

### 4.2.5 Input / Output Handling

- how input/ouput connects to the Hack computer hardware:
  ```
  input -> keyboard ->\
                      | <-> memory maps <-> Hack hardware
  output <- screen <--/
  ```
- screen:
  - color:                       black and white
  - resolution (width x height): 512 x 256 pixels
  - each row = 32 x 16-bit values (i.e., words)
  - screen origin (row 0, col 0) = top-left corner
  - pixel at (row, col) mapping:
    - = RAM[SCREEN + row * 32 + col / 16]
  - if pixel bit = 1 -> black
  - if pixel bit = 0 -> white
  - `RAM[SCREEN] = SCREEN[16384] = 1st row of screen`
  - Hack cannot access individual pixels / bites directly
- keyboard:
  - referenced by symbol `KBD`
  - gets input via the word memory map at `RAM[24576]`
  - no key press -> code 0

### 4.2.7 Syntax Conventions and File Formats

- binary code files:
  - binary Hack programs stored with `.hack` file extension
  - of 16-bit binary numbers per line separated by newline chars
  - `n`th line in code is stored in the Hack computer at address `n` in instruction memory
  - 0-indexed
- assembly language files:
  - symbolic Hack programs stored with `.asm` file extension
  - of text lines separated by newline chars
  - each line is 1 of the 4:
    - A-instruction OR
    - C-instruction OR
    - label declaration: AKA pseudo-instructions; symbol OR
    - comment
  - assembler binds a symbol to the next instruction's address
- constants and symbols:
  - constant: a non-negative integer in the range [0, 2^15=1]
  - symbol: a series of letters, digits, _, ., $, :, that is non-digit starting
- comments: prefix with double slash `//`
- white space: is ignored
- case conventions:
  - uppercase: assembly mnemonics, label symbols
  - lowercase: variable symbols

## 4.3 Hack Programming

### Example 1: `Add.asm`

- user inputs values at `RAM[0]` and `RAM[1]` before running program
- sums up values at `RAM[0]` and `RAM[1]` and 17
- stores result in third register `RAM[2]`
- program ends with an infinite loop

- Hack assembly code:
```asm
// Program: Add.asm
// Computes: RAM[2] = RAM[0] + RAM[1] + 17
// Usage: put values in RAM[0] and in RAM[1]
  // D = RAM[0]
  // R0 = 0 -> A = 0 -> M = RAM[0] -> instruction = ROM[0]
  @R0
  // D = M -> D = RAM[0] -> D = x (some non-negative integer)
  D=M

  // D = D + RAM[1]
  // R1 = 1 -> A = 1 -> M = RAM[1] -> instruction = ROM[1]
  @R1
  // D = RAM[0] + RAM[1] 
  // -> D = x + y (another non-negative integer)
  D=D+M

  // D = D + 17
  // A = 17 -> M = RAM[17] -> instruction = ROM[17]
  @17
  // D = (x + y) + 17
  D=D+A

  // RAM[2] = D
  // R2 = 2 -> A = 2 -> M = RAM[2] -> instruction = ROM[2]
  @R2
  // M = (x + y) + 17
  M=D

// binds label symbol `END` to address of next instruction
(END)
  // END = an address x -> M = RAM[x] -> instruction = ROM[x]
  @END

  // 
  0;JMP
```

### Example 2: `Sum1ToN.asm`

- TODO

- Hack assembly code:
```asm
// File: Sum1ToN.asm
// Computes RAM[1] = 1 + 2 + 3 + ... + RAM[0]
// Usage: put a value >= 1 in RAM[0]
  // i = 1
  // Declares a variable symbol `i`
  // A = i -> M = RAM[i] -> instruction = ROM[i]
  @i
  // M = 1 -> RAM[i] = 1
  M=1
  
  // sum = 0
  // Declares a variable symbol `sum`
  // A = sum -> M = RAM[sum] -> instruction = ROM[sum]
  @sum
  // M = 0 -> RAM[sum] = 0
  M=0

// declares a label `LOOP`
(LOOP)
  // if (i > R0) goto STOP
  @i
  D=M
  @R0
  D=D-M
  @STOP
  D;JGT
  
  // sum = sum + i
  @sum
  D=M
  @i
  D=D+M
  @sum
  M=D

  // i = i + 1
  @i
  M=M+1

  // goto LOOP
  @LOOP
  0;JMP
(STOP)
  // R1 = sum
  @sum
  D=M
  @R1
  M=D
(END)
  @END
  0;JMP
```

### Example 3: `PointerDemo.asm`

- TODO

- pseudocode:
```
// Program: PointerDemo
// Starting at base address R0,
// sets the first R1 words to -1
  n = 0
LOOP:
  if (n == R1) goto END
  *(R0 + n) = -1
  n = n + 1
  goto LOOP
END:
```

- Hack assembly code:
```asm
// Program: PointerDemo
// Starting at base address R0,
// sets the first R1 words to -1
  // n = 0
  @n
  M=0
(LOOP)
  // if (n == R1) goto END
  @n
  D=M
  @R1
  D=D-M
  @END
  D;JEQ
  // *(R0 + n) = -1
  @R0
  D=M
  @n
  A=D+M
  M=-1
  // n = n + 1
  @n
  M=M+1
  // goto LOOP
  @LOOP
  0;JMP
(END)
  @END
  0;JMP
```
