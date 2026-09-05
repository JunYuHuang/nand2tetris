# Project 6

## Todos

Complete the following:

- [x] `parser.py` (recommended but optional)
- [x] `code.py` (recommended but optional)
- [x] `symbol_table.py` (recommended but optional)
- [x] `main.py` (required)
- [x] `HackAssembler` executable binary (required)
- [_] Verify it creates the correct `.hack` binary output files for these programs:
    - [ ] `add/Add.asm`
    - [ ] `max/MaxL.asm`
    - [ ] `max/Max.asm`
    - [ ] `pong/pongL.asm`
    - [ ] `pong/Pong.asm`
    - [ ] `rect/RectL.asm`
    - [ ] `rect/Rect.asm`
- [ ] Fix `HackAssembler` bugs
    - [ ] Some text lines in output `.hack` files contain a dash `-` char as the 2nd char instead of a `1` or `0` bit char

## How to Build

See [HackAssembler README](./HackAssembler/README.md)

## How To Test

Run in a bash terminal:
```
cd projects/6/HackAssembler/dist

# Test assembly programs with no symbolic references
HackAssembler ../max/MaxL.asm
HackAssembler ../pong/PongL.asm
HackAssembler ../rect/RectL.asm

# Test assembly programs with symbolic references
HackAssembler ../add/Add.asm
HackAssembler ../max/Max.asm
HackAssembler ../pong/Pong.asm
HackAssembler ../rect/Rect.asm
```

## Notes

- PEDAC:
    - Problem:
        - input:
            - `assembly_file`: string
                - represents a path to a Hack assembly machine language program file
                - required suffix = `.asm`
        - output:
            - none
        - side effects:
            - `binary_file`: a file
                - required suffix = `.hack`
                - text contents:
                    - lines of 16-char lengthed of 1s and 0s
                    - 1s and 0s represent C or A instructions defined in the Hack machine language spec
                - binary executable file created from `assembly_file`
                - created in the same directory as `assembly_file`
    - Examples:
        - TODO
    - Data Structures & Algorithms:
        - TODO

- pseudocode: basic assembler, no symbolic references
    - if `assembly_file` doesn't exit,
        - exit
    - open the file `assembly_file`
    - create output file `Prog.hack` in same directory as `assembly_file`
    - while not at end of file in `assembly_file`:
        - go to the current line `line`
        - create empty string `outputLine`
        - if `line` is C-instruction,
            - get fields
            - translates fields to their bit codes
            - set `outputLine` to  16-digit bit char string
        - else (if `line` is A-instruction),
            - converts `xxx` into a 16-bit (`1` and `0` chars) string
            - set `outputLine` to  16-digit bit char string
        - append string to `Prog.hack`
        - go to next line in `assembly_file`
    - close file `assembly_file`
    - close file `Prog.hack`

- pseudocode: full assembler
    - if `assembly_file` doesn't exit,
        - exit
    - open the file `assembly_file`
    - create output file `Prog.hack` in same directory as `assembly_file`
    - create empty hashmap `symbolToAddress`
    - set `symbol_address` int to 16
    - while not at end of file in `assembly_file`:
        - if there is a symbol in the current line `line`,
            - means current line `line` is possibly an A-instruction or L-instruction
            - add key-value entry (`symbol`, `symbol_address`) to `symbolToAddress`
            - increment `symbol_address` by 1
        - go to next line
    - move file pointer in `assembly_file` to start of file
    - while not at end of file in `assembly_file`:
        - go to the current line `line`
        - create empty string `outputLine`
        - if `line` is a comment, is an empty line of only whitespace chars,
            - continue to next `line`
        - else if `line` is C-instruction,
            - get fields
            - translates fields to their bit codes
            - set `outputLine` to  16-digit bit char string
        - else (if `line` is A-instruction),
            - if `xxx` (from `@xxx`) is a symbol,
                - if `xxx` is a key in `symbolToAddress`,   
                    - replace it with its numeric value mapped to it in `symbolToAddress`
                - else (`xxx` is a new symbol),
                    - add key-value entry (`xxx`, `symbol_address`) to `symbolToAddress`
            - converts `xxx` into a 16-bit (`1` and `0` chars) string
            - set `outputLine` to  16-digit bit char string
        - append string to `Prog.hack`
        - go to next line in `assembly_file`
    - close file `assembly_file`
    - close file `Prog.hack`

- How to set up a Python 3.14 project with?
    - library test for writing unit / integration tests
    - pinned Python version and library dependencies defined in a config file
    - script / pipeline for building the Python program into an executable file
    - structure that:
        - allows an entry file named `main.py`
        - `main.py` to import and use custom, locally-defined modules
    - paths for `.gitignore` to exclude local package dependencies
