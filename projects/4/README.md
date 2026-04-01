# Project 4

## Todos

Complete all Hack Assembly implementations for the programs below chapter 3:

- [x] `Mult`
- [x] `Fill`

## How To Test

Run the CPU simulator script against the test script for the Hack Assembly program. Example for testing the `Fill.asm` program in a Linux Bash terminal:
```
cd nand2tetris/tools
CPUSimulator.sh ../projects/4/FillAutomatic.tst
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
    - `keyPressed`: variable that represents the character pressed on the keyboard as a 16-bit integer
      - `0` = no key pressed
      - any integer != `0` = some key pressed
  - outputs:
    - none
  - side effects:
    - sets all 512 x 256 (width x height) pixels of the screen resolution to be all black or all white depending on if the key pressed by the user
      - any key pressed -> make screen all black
      - no key pressed -> make screen all white
  - notes:
    - screen resolution 512 x 256 pixels = 131072 pixels
    - pixels are represented in 16 pixel chunks by a 16-bit integer in memory starting at the RAM address bound to the symbol label / constant `@SCREEN`
      - traverse 16-pixels at a time for a total of 131072 / 16 = 8192 times
- pseudocode: 
  - `pixelColor`: variable that represents the colour of a pixel as a 16-bit integer
    - `1` = black
    - `0` = white
  - `screen`: 16-bit integer = `SCREEN` + `screenOffset`
  - `screenOffset`: variable that tracks the current row of the screen we are traversing as a 16-bit integer
    - is an integer in the range [0, 8191]
  - while true:
    - if `keyPressed` is `0`,
      - set `pixelColor` to `0`
    - else,
      - set `pixelColor` to a 16-bit binary value of all `1`'s
        - i.e., set it to `-1`
    - set `screenOffset` to `8192 - 1`
    - while `screenOffset` >= `0`,
      - set `screen` = `SCREEN` + `screenOffset`
      - set `RAM[screenOffset]` to `pixelColor`
      - decrement `screenOffset` by 1
