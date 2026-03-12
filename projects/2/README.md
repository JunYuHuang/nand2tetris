# Project 2

## Todos

Complete all HDL program implementations for all 6 logic gates or chips in chapter 2:

- [x] `HalfAdder`
- [x] `FullAdder`
- [x] `Add16`
- [x] `Inc16`
- [ ] `ALU-basic`
- [ ] `ALU`

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

- `ALU-basic` gate
- `ALU` gate
