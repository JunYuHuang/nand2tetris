# Project 1

## Todos

Complete all HDL program implementations for all 15 logic gates or chips (excluding `NAND`) in chapter 1:

- [x] `Not`
- [x] `And`
- [x] `Or`
- [x] `Xor`
- [x] `Mux`
- [x] `DMux`
- [ ] `And16`
- [ ] `Dmux4Way`
- [ ] `Dmux8Way`
- [ ] `Mux4Way16`
- [ ] `Mux8Way16`
- [ ] `Mux16`
- [ ] `Not16`
- [ ] `Or8Way`
- [ ] `Or16`

## Tips

- `Nand`: can skip
- `Not`: use 1 Nand gate
- `And`: use Nand + Not gates
- `Or`: use And + Not gates
- `Xor`: use And, Not, + Or gates
- `Multiplexer / Demultiplexer`: use Nand, Not, And, Or, + Xor gates
- `Multi-bit Not / And / Or gates`: arrange arrays of n basic gates and having each gate operate separately on its
single-bit inputs
- `Multi-bit multiplexer`: feed same selection bit to every one of `n` binary multiplexer
- `Multi-way gates`: use forks

## Notes

- `Nand` gate:
  ```
  Chip Name: Nand
  Input:     a, b
  Output:    out
  Function:  if ((a==1) and (b==1)) then out = 0, else out = 1

  a | b | Nand(a, b)
  --|---|-----------
  0 | 0 | 1
  0 | 1 | 1
  1 | 0 | 1
  1 | 1 | 0
  ```

- `Not` gate:
  ```
  Chip Name: Not
  Input:     in
  Output:    out
  Function:  if (in==1) then out = 0, else out = 1

  in | Not(in)
  ---|--------
  0  | 1
  1  | 0
  ```
  - Not(a) = Nand(a, a)

- `And` gate:
  ```
  Chip Name: And
  Input:     a, b
  Output:    out
  Function:  if ((a==1) and (b==1)) then out = 1, else out = 0

  a | b | And(a, b)
  --|---|-----------
  0 | 0 | 0
  0 | 1 | 0
  1 | 0 | 0
  1 | 1 | 1
  ```
  - And(a, b) = Not(Nand(a, b))

- `Or` gate:
  ```
  Chip Name: Or
  Input:     a, b
  Output:    out
  Function:  if ((a==0) and (b==0)) then out = 0, else out = 1

  a | b | Or(a, b)
  --|---|-----------
  0 | 0 | 0
  0 | 1 | 1
  1 | 0 | 1
  1 | 1 | 1

    a || b
  = ~~(a || b)
  = ~(~a & ~b)

  a -> NOT -+
            +-> AND -> NOT -> out
  b -> NOT -+
  ```
  - Or(a, b) = Not(And(Not(a), Not(b)))

- `Xor` gate:
  ```
  Chip Name: Xor
  Input:     a, b
  Output:    out
  Function:  if (a!=b) then out = 1, else out = 0

  a | b | Xor(a, b)
  --|---|-----------
  0 | 0 | 0
  0 | 1 | 1
  1 | 0 | 1
  1 | 1 | 0

    a ⊕ b
  = (~a & b) || (a & ~b)

  a -> NOT -+
    |       +-> AND -+
    +-------+        +-> OR -> out
    |       +-> AND -+
  b -> NOT -+
  ```
  - Xor(a, b) = Or(And(Not(a), b), And(a, Not(b)))

- `Mux` gate:
  ```
  Chip Name: Mux
  Input:     a, b, sel
  Output:    out
  Function:  if (sel==0) then out = a, else out = b

  sel | out
  ----|-----
  0   | a
  1   | b

  a | b | sel | out
  --|---|-----|-----
  0 | 0 | 0   | 0
  0 | 1 | 0   | 0
  1 | 0 | 0   | 1
  1 | 1 | 0   | 1
  0 | 0 | 1   | 0
  0 | 1 | 1   | 1
  1 | 0 | 1   | 0
  1 | 1 | 1   | 1
  ```
  - Mux(a, b, sel) = (
    (a & ~b & ~sel) | (a & b & ~sel) | (~a & b & sel) | 
    (a & b & sel)
  )
  - F = a & ~sel & (~b | b) | b & sel (~a & a)
  - F = a & ~sel (1) | b & sel (1)
  - F = (a & ~sel) | (b & sel)

- `DMux` gate:
  ```
  Chip Name: DMux
  Input:     in, sel
  Output:    a, b
  Function:  if (sel==0) then {a, b} = {in, 0},
             else             {a, b} = {0, in}

  in | sel | a | b
  ---+-----+---+---
  0  | 0   | 0 | 0
  1  | 0   | 1 | 0
  0  | 1   | 0 | 0
  1  | 1   | 0 | 1

  sel | a  | b
  ----+----+----
  0   | in | 0
  1   | 0  | in

  DMux(in, sel) = 
    a = in & ~sel
    b = in & sel
  ``` 

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```

