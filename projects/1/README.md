# Project 1

## Todos

Complete all HDL program implementations for all 15 logic gates or chips (excluding `NAND`) in chapter 1:

- [x] `Not`
- [x] `And`
- [x] `Or`
- [x] `Xor`
- [x] `Mux`
- [x] `DMux`
- [x] `Not16`
- [x] `And16`
- [x] `Or16`
- [x] `Mux16`
- [x] `Or8Way`
- [x] `Mux4Way16`
- [x] `Mux8Way16`
- [x] `DMux4Way`
- [x] `DMux8Way`

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

- `Not16` gate:
  ```
  Chip Name: Not16
  Input:     in[16]
  Output:    out[16]
  Function:  for i = 0..15 out[i] = Not(in[i])

  Not16(a, b, ..., p) = apply Not() gate to all 16 input bits
  ```

- `Or8Way` gate:
  ```
  Chip Name: Or8Way
  Input:     in[8]
  Output:    out
  Function:  out = Or(in[0], in[1], ..., in[7])
  ```

- `Mux4Way16` gate:
  ```
  Chip Name: Mux4Way16
  Input:     a[16], b[16], c[16], d[16], sel[2]
  Output:    out[16]
  Function:  if (sel==00,01,10, or 11) then out = a,b,c, or d
  Comment:   The assignment is a 16-bit operation.
             For example, "out = a" means "for i = 0..15 out[i] = a[i]".

   sel[1] | sel[0] | out
  --------+--------+-----
   0      | 0      | a
   0      | 1      | b
   1      | 0      | c
   1      | 1      | d

  ```

- `Mux8Way16` gate:
  ```
  Chip Name: Mux8Way16
  Input:     a[16], b[16], c[16], d[16], e[16], f[16], g[16], h[16], sel[3]
  Output:    out[16]
  Function:  if (sel==000,001,010, ..., or 111) then out = a,b,c,d, ..., or h
  Comment:   The assignment is a 16-bit operation.
             For example, "out = a" means "for i = 0..15 out[i] = a[i]".

   sel[2] | sel[1] | sel[0] | out
  --------+--------+--------+-----
   0      | 0      | 0      | a
   0      | 0      | 1      | b
   0      | 1      | 0      | c
   0      | 1      | 1      | d
   1      | 0      | 0      | e
   1      | 0      | 1      | f
   1      | 1      | 0      | g
   1      | 1      | 1      | h

  ```
  - N-way multiplexor gates rules:
    - at each level, the inputs pair must differ only in the selector bit used at that level
    - selector bit order determines how inputs must be grouped
  - general multiplexor tree rule:
    - for an N-way mux with k selector bits:
      - inputs = 2^k
      - levels = k
    - must use selector bit `sel[i]` at level `i`
    - each level halves the number of signals
  - N-way mux is a binary decision tree e.g.,
    ```
             sel[2]
           /        \
       sel[1]      sel[1]
       /    \      /    \
    sel[0] sel[0] sel[0] sel[0]
    ```

- `DMux4Way` gate

- `DMux8Way` gate:
  ```
  8-way demultiplexor:
  [a, b, c, d, e, f, g, h] = [in, 0,  0,  0,  0,  0,  0,  0] if sel = 000
                             [0, in,  0,  0,  0,  0,  0,  0] if sel = 001
                             [0,  0, in,  0,  0,  0,  0,  0] if sel = 010
                             [0,  0,  0, in,  0,  0,  0,  0] if sel = 011
                             [0,  0,  0,  0, in,  0,  0,  0] if sel = 100
                             [0,  0,  0,  0,  0, in,  0,  0] if sel = 101
                             [0,  0,  0,  0,  0,  0, in,  0] if sel = 110
                             [0,  0,  0,  0,  0,  0,  0, in] if sel = 111

  a = in & ~sel[2] & ~sel[1] & ~sel[0]
  b = in & ~sel[2] & ~sel[1] & sel[0]
  c = in & ~sel[2] & sel[1] & ~sel[0]
  d = in & ~sel[2] & sel[1] & sel[0]
  e = in & sel[2] & ~sel[1] & ~sel[0]
  f = in & sel[2] & ~sel[1] & sel[0]
  g = in & sel[2] & sel[1] & ~sel[0]
  h = in & sel[2] & sel[1] & sel[0]
  ```

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```
