# Project 4

## Todos

Complete all Hack Assembly implementations for the programs below chapter 3:

- [x] `Mult`
- [ ] `Fill`

## How To Test

Run the CPU simulator script against the test script for the Hack Assembly program. Example for testing the `Fill.asm` program in a Linux Bash terminal:
```
cd nand2tetris/tools
CPUSimulator.sh ../projects/4/Fill.tst
```

## Notes

### `Mult.asm` program

- problem:
  - prereqs:
    - input an integer value at `RAM[0]` for variable `R0`
    - input an integer value at `RAM[1]` for variable `R1`
  - inputs:
    - `R0`: an integer variable in the range [0, 32768]
    - `R1`: an integer variable the range [0, 32768]
  - output:
    - `R2`: the multiplication product of `R0` and `R1`
  - constraints:
    - can only use:
      - add arithmetic operator
      - loops
    - cannot use:
      - multiply arithmetic operator (doesn't exist)
- pseudocode:
  - set variable `R2` to integer value `0`
  - set variable `i` to integer value `0`
  - while `i` < `R0`,
    - set `R2` to itself plus `R1`
    - set `i` to itself plus `1`
  - end program with an infinite loop

### `Fill.asm` program

- problem:
  - inputs:
    - any key press
  - outputs:
    - none
  - side effects:
    - todo
