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

- `Nand` gate specs:
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

- `Not` gate specs:
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

## Todos

Complete all HDL program implementations for all 15 logic gates / chips in chapter 1:

1. [x] `And`
2. [ ] `And16`
3. [ ] `DMux`
4. [ ] `Dmux4Way`
5. [ ] `Dmux8Way`
6. [ ] `Mux`
7. [ ] `Mux4Way16`
8. [ ] `Mux8Way16`
9. [ ] `Mux16`
10. [x] `Not`
11. [ ] `Not16`
12. [ ] `Or`
13. [ ] `Or8Way`
14. [ ] `Or16`
15. [ ] `Xor`
