# 6. Assembler

## 6.1 Background

- Hack machine language formats:
    - 1) binary: 1s & 0s bits, hard to read
    - 2) symbolic; human language like AKA assembly; easier to read
- symbol = short-form word that represents a memory address e.g., `LOOP` = 12
    - types / reasons (3):
        - 1) labels = place in code e.g., `LOOP`
        - 2) variables = value that can change e.g., `sum`
        - 3) predefined symbols = meaninful, special address constants e.g., KBD
- assembler = software program that translates assembly to binary
    - why? computers only understand binary
    - depends on symbol table
    - diagram:
        ```
        Assembly     -----> Assembler ------> Binary 
        E.g., sum.asm           |             E.g., sum.hack
                                | uses
                                |
                                v
                            Symbol table
                            ------------
                            R0         0
                            R1         1
                            R2         2
                            ...      ...
                            i         16
                            KBD    24576
        ```

## 6.2 The Hack Machine Language Specification

### 6.2.1 Programs

- binary Hack program:
    - series of text lines of 16-bit numbers each
    - `0` prefix ? A-instruction : else, a C-instruction
- assembly Hack program:
    - series of text lines that are 1 of the following:
        - 1) assembly instruction: A or C instruction
        - 2) label declaration: of a symbol `xxx`
        - 3) comment: `//`-prefixed line, ignored

### 6.2.2 Symbols

- symbol types:
    - predefined symbols: e.g., `R0` represents memory address `0`
    - label symbols: pseudo-instruction in form `(xxx)`
        - `xxx` is ROM address that points to next program instruction
    - variable symbols: a variable if not predefined + not a label
        - addresses are set to next / incremented RAM address from 16

### 6.2.3 Syntax Conventions

- symbols: series of a-z,A-Z,0-9,_,.,$,: & not digit-prefixed
- constants: only in A-instruction in form `@xxx`
- white space: ignore leading space chars + empty lines
- case conventions:
    - assembly mnemonics: UPPERCASE e.g., `JEQ`
    - label symbols: UPPERCASE
    - variable symbols: lowercase

## 6.3 Assembly-to-Binary Translation

- assembler = handle instructions + handle symbols

### 6.3.2 Handling Instructions

- instructions
    - -> extract fields
    - -> field to bit-code
    - -> resolves symbols to value
    - -> configs binary codes into 16 bit (`0` and `1`) chars
    - -> writes string to output file

### 6.3.2 Handling Symbols

- assembly programs can use label symbols before they are defined
    - how? two-pass assembler
- two-pass assembler:
    - first pass:
        - build symbol table (labels -> addresses in ROM)
    - second pass:
        - resolves variable symbols
            - adds variables (in RAM) to symbol table
        - generates binary code via symbol table

## 6.4 Implementation

- usage:
```
prompt > HackAssembler Prog.asm
```
    - `prompt` = shell terminal
    - `HackAssembler` = compiled binary executable program of assembler
    - `Prog.asm` = Hack assembly program file

### 6.4.1 Developing a Basic Assembler

- todo