# Project 2

## Todos

Complete all HDL program implementations for all 6 logic gates or chips in chapter 2:

- [x] `HalfAdder`
- [x] `FullAdder`
- [ ] `Add16`
- [ ] `Inc16`
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
- `Inc16` gate
- `ALU-basic` gate
- `ALU` gate
