# Project 5

## Todos

Complete all HDL program implementations for all logic gates or chips in chapter 5:

- [ ] `Memory`
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

  2^15   | 2^14   | 2^13  | 2^12  | 2^13  | ...
  -------+--------+-------+-------+-------+-----
  32,768 | 16,384 | 8,192 | 4,096 | 2,048 | ... 

  0      = 0 (address[0] or 2^0 == 0)
  16,383 = 2^13 + 2^12 + 2^11 + ... + 2^1
  16,384 = 2^14
  24,575 = 2^14 + 2^12 + 2^11 + 2^10 + ... + 2^0
  24,576 = 2^14 + 2^13 = 16,384 + 8,192
  24,577 = 2^14 + 2^13 + 2^1 = 16,384 + 8,192 + 1
  32,768 = 2^15

  Pseudocode logic:
  - if (
      `address[15]` == 1 OR
      (`address[14]` == 1 AND `address[13]` == 1 AND `address[0]` == 1)
    ),
    - `address` is out-of-bounds (i.e., in range [24577, 32768])
    - set `out` to 0 or some value to indicate `address` is invalid?
  - else if (
      `address[14]` == 1 AND 
      `address[13]` == 1 AND
      (`address[0]` thru `address[12]` == 0)
    ),
    - `address` == 24,576 -> access from `Keyboard` chip
    - set `out` to `Keyboard`'s `out`
  - else if (
      `address[14]` == 1 AND
      `address[13]` == 0
    ),
    - `address` is in range [16384, 24575] -> access from `Screen` chip
    - if `load` == 1,
      - set `Screen[address - 16384]` to `in`
    - set `out` to `Screen[address - 16384]`    
  - else if (
      `address[14]` == 0
    ),
    - `address` is in range [0, 16383] -> access from `RAM16K` chip
    - if `load` == 1,
      - set `RAM16K[address]` to `in`
    - set `out` to `RAM16K[address]`
  ```
  - component chips:
    - `RAM16K` (built-in)
    - `Screen` (built-in)
    - `Keyboard` (built-in)
  - component chips & their interfaces:
    - `RAM16K(in= ,load= ,address= ,out= )`
    - `Screen(in= ,load= ,address= ,out= )`
    - `Keyboard(out= )`

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
