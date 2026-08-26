# Project 5

## Todos

Complete all HDL program implementations for all logic gates or chips in chapter 5:

- [x] `Memory`
- [x] `CPU`
- [ ] `Computer`

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```

## Notes

- `Memory` chip:
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

  Memory address ranges to Chip Device mappings:
  - [0, 16383] -> RAM16K
  - [16384, 24575] -> Screen
  - [24576, 24576] -> Keyboard
  - [24577, Infinity] -> Invalid address

  How does the chip deal with an invalid memory address?
  - based on `Memory.tst`: 
    - read (`load` = 0): `out[16]` is 0
    - write (`load` = 1): `out[16]` is N/A (no such test cases)

  How to make chip detect if any bits in `address[0..12]` are 1 while both `address[13]` and `address[14]` are 1?
  - use `Or8Way` or `Or` chips?

  2^14   | 2^13  | 2^12  | 2^11  | ...
  -------+-------+-------+-------+-----
  16,384 | 8,192 | 4,096 | 2,048 | ... 
  0      | ...   | ...   | ...   | ... -> RAM16K address [0, 16383]
  1      | 0     | ...   | ...   | ... -> Screen address [16384, 24575]
  1      | 1     | 0     | 0     | ... -> Keyboard address [24576, 24576]

  0      = 0 (address[0] or 2^0 == 0)
  16,383 = 2^13 + 2^12 + 2^11 + ... + 2^1
  16,384 = 2^14
  24,575 = 2^14 + 2^12 + 2^11 + 2^10 + ... + 2^0
  24,576 = 2^14 + 2^13 = 16,384 + 8,192
  24,577 = 2^14 + 2^13 + 2^1 = 16,384 + 8,192 + 1

  - component chips:
    - `RAM16K` (built-in)
    - `Screen` (built-in)
    - `Keyboard` (built-in)
  - component chips & their interfaces:
    - `RAM16K(in= ,load= ,address= ,out= )`
      - `in[16]`
      - `load`
      - `address[14]`
      - `out[16]`
    - `Screen(in= ,load= ,address= ,out= )`
      - `in[16]`
      - `load`
      - `address[13]`
      - `out[16]`
    - `Keyboard(out= )`
      - `out[16]`
  - possible helper chips:
    - `DMux(in= ,sel= ,a= ,b= )`
      - IN:
        - `in`
        - `sel`
      - OUT:
        - `a`
        - `b`
    - `DMux4Way(in= ,sel= ,a= ,b= ,c= ,d= )`
      - IN:
        - `in`
        - `sel[2]`
      - OUT:
        - `a`
        - `b`
        - `c`
        - `d`
    - `Mux16(a= ,b= ,sel= ,out= )`
      - IN:
        - `a[16]`
        - `b[16]`
        - `sel`
      - OUT:
        - `out[16]`
    - `Mux4Way16(a= ,b= ,c= ,d= ,sel= ,out= )`
      - IN:
        - `a[16]`
        - `b[16]`
        - `c[16]`
        - `d[16]`
        - `sel[2]`
      - OUT:
        - `out[16]`
    - `Or(a= , b= , out= )`
      - IN:
        - `a`
        - `b`
      - OUT:
        - `out`
    - `Or8Way(in= ,out= )`
      - IN:
        - `in[8]`
      - OUT:
        - `out`

- `CPU` chip:
  ```
  Chip Name: CPU
  Input:     instructions[16] // Instruction to execute
             inM[16]          // The instruction's M input (contents
                              // of RAM[A])
             reset            // Signals whether to restart the program (
                              // if reset==1) or continue executing the
                              // program (if reset==0).
  Output:    outM[16]         // Written to RAM[addressM], the instruction's
                              // M output
             addressM[15]     // At which address to write?
             writeM           // Write to the memory?
             pc[15]           // Address of next instruction
  ```
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
  - questions:
    - What determines whether `ARegister` loads the instruction or the ALU result?
      - `instruction` input's MSB (i.e., `instruction[15]`)
      - if `instruction` is an A-instruction, load it into `ARegister`
        - A-instruction if `instruction[15]` == 0
      - else if `instruction` is a C-instruction, load ALU result into `ARegister`
        - C-instruction if `instruction[15]` == 1
    - What determines whether `DRegister` loads?
      - `instruction` input
        - is C-instruction
        - 2nd `d` bit (i.e., `instruction[4]`)
      - if `instruction[4]` == 1, load ALU output in `DRegister`
      - else (`instruction[4]` == 0), do nothing
      - -> `And(instruction[15], instruction[4])`
    - What determines `writeM`?
      - `instruction` input
        - is C-instruction (i.e., `instruction[15]` == 1)
        - 3rd `d` bit (i.e., `instruction[3]`)
      - if 3rd `d` bit (`instruction[3]`) == 1,
        - sets `writeM` output to 1
      - else (`instruction[3]` == 0),
        - sets `writeM` output to 0
      - -> `And(instruction[15], instruction[3])`
    - What selects `A` vs `M` as the ALU's `y` input?
      - `instruction` input
        - assumes C-instruction
        - `a` bit i.e., `instruction[12]`
      - if C-instruction's `a` bit (`instruction[12]`) == 0,
        - `ARegister` output -> `ALU` Y input
      - else (`instruction[12]` == 1),
        - `RAM[A]` / `inM` / `M`-> `ALU` Y input
      - -> `And(instruction[15], instruction[12])`
    - Where should `outM` come from?
      - `ALU` output
    - What two ALU outputs are needed to implement all the jump conditions?
      - `zr` and `ng`
    - What value should be presented to the PC's `in` when a jump occurs?
      - `ARegister` output
  - C-instruction `comp` (6 `c`'s) bits to `ALU` mappings
    - where
      - `ALU.x` = `DRegister.out`
      - `ALU.y` = `ARegister.out` or `inM` (i.e., `RAM[A]`)
    - matches up directly:
      - `ALU.zx` = `instruction[11]`
      - `ALU.nx` = `instruction[10]`
      - `ALU.zy` = `instruction[9]`
      - `ALU.ny` = `instruction[8]`
      - `ALU.f` = `instruction[7]`
      - `ALU.no` = `instruction[6]`
  - when should `PC` reset, load `ARegister`, or increment its stored value?
    - select an option by setting it to 1 and the rest to 0
    - options: `CPU.reset`, `CPU.load`, `CPU.inc`
    - reset if `CPU.reset` == 1
    - load if are doing a jump:
      - `instruction` is C-instruction (`instruction[15]` == 1)
      - jump: not null
      - C-instruction `j` bits: not all 0's
      - `ALU.zr`: ?
      - `ALU.ng`: ?
    - increment if:
      - `instruction` is A-instruction (`instruction[15]` == 0) OR
      - `instruction` is C-instruction (`instruction[15]` == 1) +
        - jump: null; no jump
        - C-instruction `j` bits: 0 0 0
        - `ALU.zr` and `ALU.ng` values don't matter
  - mapping C-instruction `jump` commands to `PC` inputs:
    - no jump; increment `PC` if:
      - C-instruction + jump: null; no jump
        - 3 `j` bits: 0 0 0
        - `ALU.zr`: doesn't matter
        - `ALU.ng`: doesn't matter
        - ->
        `
        And(
          instruction[15],
          Not(And(And(instruction[0], instruction[1]), instruction[2]))
        )
        `
      - A-instruction
        - `instruction[15] == 0`
        - -> `Not(instruction[15])`
      - ->
        `
        Or(
          Not(instruction[15]),
          And(
            instruction[15],
            Not(And(And(instruction[0], instruction[1]), instruction[2]))
          )
        )
        `
        -> `CPU.inc`
    - for any valid jump (excluding no jump):
      - -> 
        `
        And(
          instruction[15],
          {jump bits + ALU.zr + ZLU.ng = 1 matching a jump cmd} OR'd w/ every
          other jump bit mask combo (3 `j` bits + ALU.zr + ALU.ng) evaluating to 1
        )
        `
      - decode combos of `ALU.zr` + `ALU.ng` + 3 `j` bits to set `PC.load` to 1
      - if 1st `j` bit is 1 -> jump (option 2) if output < 0
        - output < 0 if:
          - `ALU.zr` = 0
          - `ALU.ng` = 1
          - -> `instruction[2] AND NOT(ALU.zr) AND ALU.ng`
      - if 2nd `j` bit is 1 -> jump (option 2) if output = 0
        - output = 0 if:
          - `ALU.zr` = 1
          - `ALU.ng` = 0
          - -> `instruction[1] AND ALU.zr AND NOT(ALU.ng)`
      - if 3rd `j` bit is 1 -> jump (option 2) if output > 0
        - output > 0 if:
          - `ALU.zr` = 0
          - `ALU.ng` = 0
          - -> `instruction[0] AND NOT(ALU.zr) AND NOT(ALU.ng)`
          - -> `instruction[0] AND NOT(ALU.zr OR ALU.ng)`
      - all 3 `j` bits are 1 -> always jump
        - -> `instruction[0] AND instruction[1] AND instruction[2]`
      - ->
        `
        AND(
          instruction[15],
          OR(
            AND(
              instruction[2],
              AND(NOT(zr), ng)
            ),
            OR(
              AND(
                instruction[1],
                AND(zr, NOT(ng))
              ),
              OR(
                AND(
                  instruction[0],
                  NOT(OR(zr, ng))
                ),
                AND(
                  instruction[0],
                  AND(instruction[1], instruction[2])
                )
              )
            )
          )
        )
        `
  - component chips:
    - `ALU(x= ,y= , zx= ,nx= ,zy= ,ny= ,f= ,no= ,out= ,zr= ,ng= )` (built-in)
      - IN:
        - `x[16]`
          - = `DRegister` output
        - `y[16]`
          - = `ARegister` output or `inM`
        - see above
      - OUT:
        - `out[16]`
        - `zr`
        - `ng`
    - `ARegister(in= ,load= ,out= )` (built-in)
      - IN:
        - `in[16]`
          - = `ALU` output if `instruction` is C-instruction
            - C-instruction = `instruction[15]` is 1
          - = `instruction` output if `instruction` is A-instruction
            - A-instruction = `instruction[15]` is 0
        - `load`: stores `in[16]` if set to 1, else keeps old value if 0
          - stores `instruction` if it is A-instruction
            - `instruction[15]` == 0
            - -> `Not(instruction[15])`
          - stores `instruction` if:
            - is C-instruction; `instruction[15]` == 1
            - `dest` (3 `d`) bits in `instruction` = `A`, `AM`, `AD`, or `ADM`
              - 1st `d` bit (`instruction[5]`) is 1
              - other `d` bits don't matter
            - -> `And(instruction[15], instruction[5])
          - = `Xor(Not(instruction[15]), And(instruction[15], instruction[5]))`
      - OUT:
        - `out[16]`
    - `DRegister(in= ,load= ,out= )` (built-in)
      - IN:
        - `in[16]` = `ALU` output
        - `load`: stores `in[16]` if set to 1, else keeps old value if 0
          - set to 1 if:
            - `instruction` is C-instruction
              - `instruction[15]` is 1
            - `dest` (3 `d`) bits indicates `D`, `DM`, `AD`, or `ADM`
              - 2nd `d` (`instruction[4]`) is 1
              - other `d` bits don't matter
          - -> `And(instruction[15], instruction[4])`
      - OUT:
        - `out[16]` = `ALU` `x` input
    - `PC(in=, inc= ,load= ,reset= ,out= )` (built-in)
      - IN:
        - `in[16]`
        - `inc`
        - `load`
        - `reset`
      - OUT:
        - `out[16]`
    - `Mux16(a= ,b= ,sel= ,out= )`
      - IN:
        - `a[16]`
        - `b[16]`
        - `sel`
      - OUT:
        - `out[16]`

- `Computer` chip:
  ```
  TODO
  ```
  - component chips:
    - `ROM32K` (built-in)
    - `CPU`
    - `Memory`
