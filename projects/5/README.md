# Project 5

## Todos

Complete all HDL program implementations for all logic gates or chips in chapter 5:

- [x] `Memory`
- [ ] `CPU`
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
  TODO
  ```
  - component chips:
    - `ALU` (built-in)
    - `ARegister` (built-in)
    - `DRegister` (built-in)
    - `PC` (built-in)

- `Computer` chip:
  ```
  TODO
  ```
  - component chips:
    - `ROM32K` (built-in)
    - `CPU`
    - `Memory`
