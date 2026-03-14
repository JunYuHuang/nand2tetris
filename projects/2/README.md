# Project 2

## Todos

Complete all HDL program implementations for all 6 logic gates or chips in chapter 2:

- [x] `HalfAdder`
- [x] `FullAdder`
- [x] `Add16`
- [x] `Inc16`
- [ ] `ALU`
  - [x] pass `ALU-basic.tst` tests
  - [ ] pass `ALU.tst` tests

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```

## Notes

- `HalfAdder` gate: add 2 bits together
  ```
  inputs        outputs
    a  |  b  | carry | sum 
  -----+-----+-------+-----
  0    | 0   | 0     | 0
  0    | 1   | 0     | 1
  1    | 0   | 0     | 1
  1    | 1   | 1     | 0

  Chip name: HalfAdder
  Input:     a, b
  Output:    sum, carry
  Function:  sum   = LSB of a + b
             carry = MSB of a + b

  carry = a & b
  sum = a XOR b
  ```

- `FullAdder` gate: add 3 bits together
  ```
  Chip Name: FullAdder
  Input:     a, b, c
  Output:    sum, carry
  Function:  sum   = LSB of a + b + c
             carry = MSG of a + b + c

   a | b | c | carry | sum
  ---+---+---+-------+-----
  0  | 0 | 0 | 0     | 0
  0  | 0 | 1 | 0     | 1
  0  | 1 | 0 | 0     | 1
  0  | 1 | 1 | 1     | 0
  1  | 0 | 0 | 0     | 1
  1  | 0 | 1 | 1     | 0
  1  | 1 | 0 | 1     | 0
  1  | 1 | 1 | 1     | 1

  carry = (a AND b) OR ((a XOR b) AND c)
  sum = (a XOR b) XOR c
  ```

- `Add16` gate
  ```
  Chip Name: Add16
  Input:     a[16], b[16]
  Output:    out[16]
  Function:  Adds two 16-bit numbers.
             The overflow bit is ignored.

  ```
  - chain 1 `HalfAdder` with 15 following `FullAdder` gates

- `Inc16` gate
  ```
  Chip Name: Add16
  Input:     in[16]
  Output:    out[16]
  Function:  out = in + 1
  Comment:   The overflow bit is ignored
  ```
  - 16 chained `HalfAdder` gates that is intially fed by `in[0]` and the 1 constant (i.e., `true`)

- `ALU-gate` gate
  ```
  Chip Name: ALU
  Input:     x[16], y[16],  // Two 16-bit data inputs
             zx,            // Zero the x input
             nx,            // Negate the x input
             zy,            // Zero the y input
             ny,            // Negate the y input
             f,             // if f==1 out=add(x,y) else out=and(x,y)
             no,            // Negate the out output
  Output:    out[16],       // 16-bit output
             zr,            // if out==0 zr=1 else zr=0
             ng             // if out<0  ng=1 else ng=0
  Function:
             if zx x=0      // 16-bit zero constant
             if nx x=!x     // Bit-wise negation
             if zy y=0      // 16-bit zero constant
             if ny y=!y     // Bit-wise negation
             if f out=x+y   // Integer two's complement addition
             else out=x&y   // Bit-wise And
             if no out=!out // Bit-wise negation
             if out==0 zr=1 else zr=0 // 16-bit equality comparison
             if out<0 ng=1  else ng=0 // two's complement comparison
  Comment:   The overflow bit is ignored.
  ```
  - possibly useful chips:
    - `And16`
    - `Mux16`
    - `Not16`
    - `Or16`
    - `Add16`
    - `Inc16`
  - Zero Function = x & ~zx
  - Not Function = (~x & nx) v (x & ~nx)
  - And Function = x & y
  - Add Function = x ADD y