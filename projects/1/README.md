# Project 1

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

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```

## Todos

Complete all HDL program implementations for all 15 logic gates / chips in chapter 1:

1. [x] `And`
2. [ ] `And16`
3. [ ] `DMux`
4. [ ] `Dmux4Way`
5. [ ] `Dmux8Way`
6. [x] `Mux`
7. [ ] `Mux4Way16`
8. [ ] `Mux8Way16`
9. [ ] `Mux16`
10. [x] `Not`
11. [ ] `Not16`
12. [x] `Or`
13. [ ] `Or8Way`
14. [ ] `Or16`
15. [x] `Xor`
