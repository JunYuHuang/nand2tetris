# Project 6

## Todos

Complete the following:

- [ ] `Parser.py` (recommended but optional)
- [ ] `Code.py` (recommended but optional)
- [ ] `Symbol.py` (recommended but optional)
- [ ] `HackAssembler.py` (required)

## How to Build

TODO: steps to create an executable program from the Python program

## How To Test

Run in a bash terminal:
```
cd projects/6/HackAssembler
chmod +x HackAssembler
HackAssembler ../add/Add.asm
HackAssembler ../max/Max.asm
HackAssembler ../max/MaxL.asm
HackAssembler ../pong/Pong.asm
HackAssembler ../pong/PongL.asm
HackAssembler ../rect/Rect.asm
HackAssembler ../rect/RectL.asm
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

- pseudocode:
    - create output file `Prog.hack`
        - for each line `line` string in `Prog.asm`:
            - create empty string `outputLine`
            - if `line` is C-instruction,
                - get fields
                - translates fields to their bit codes
                - set `outputLine` to  16-digit bit char string
            - else (if `line` is A-instruction),
                - converts `xxx` into a 16-bit (`1` and `0` chars) string
                - set `outputLine` to  16-digit bit char string
            - append string to `Prog.hack`

- How to set up a Python 3.14 project with?
    - library test for writing unit / integration tests
    - pinned Python version and library dependencies defined in a config file
    - script / pipeline for building the Python program into an executable file
    - structure that:
        - allows an entry file named `main.py`
        - `main.py` to import and use custom, locally-defined modules
    - paths for `.gitignore` to exclude local package dependencies
