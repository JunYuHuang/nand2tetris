# Project 3

## Todos

Complete all HDL program implementations for all 8 logic gates or chips in chapter 3:

- [x] `Bit`
- [x] `Register`
- [x] `RAM8`
- [ ] `RAM64`
- [ ] `RAM512`
- [ ] `RAM4K`
- [ ] `RAM16K`
- [ ] `PC`

## How To Test

Run the hardware simulator script against the test script for the chip. Example for testing the `Not.hdl` chip / gate in a Linux Bash terminal:
```
cd nand2tetris/tools
sh HardwareSimulator.sh ../projects/1/Not.tst
```

## Notes

- `Bit` chip:
  - TODO

- `Register` chip:
  - TODO

- `RAM8` chip:
  ```
  Chip Name: RAMn
  Input:     in[16], load, address[k] (k = log2n)
  Output:    out[16]
  Function:
  `out` emits the value stored a the memory location 
  (register) specified by `address`. If `load == 1`,
  then the memory location specified by `address` is 
  set to the value of `in`. The loaded value will be 
  emitted by `out` from the next time step onward.
  ```
  - components:
    - 8 x `Register` chips for storing the 8 16-bit values
    - 1 x `DMux`-variant chip for storing a value at register `address` if `load` is 1
    - 1 x `Mux`-variant chip for reading the value at register `address` if `load` is 0
