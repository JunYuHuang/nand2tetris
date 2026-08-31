INVALID_MNEMONIC_BINARY_CODE = "INVALID_MNEMONIC_BINARY_CODE"

dest_to_binary = {
    "": "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "ADM": "111"
}

comp_to_binary = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "M": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "-M": "110011",
    "!M": "110001",
    "D+1": "011111",
    "A+1": "110111",
    "M+1": "110111",
    "D-1": "001110",
    "D-M": "010011",
    "A-1": "110010",
    "M-1": "110010",
    "D+A": "000010",
    "D+M": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "M-D": "000111",
    "D&A": "000000",
    "D&M": "000000",
    "D|A": "010101",
    "D|M": "010101"
}

jump_to_binary = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

def dest(dest_mnemonic: str) -> str:
    if dest_mnemonic not in dest_to_binary:
        return INVALID_MNEMONIC_BINARY_CODE
    return dest_to_binary[dest_mnemonic]

def comp(comp_mnemonic: str) -> str:
    if comp_mnemonic not in comp_to_binary:
        return INVALID_MNEMONIC_BINARY_CODE
    return comp_to_binary[comp_mnemonic]

def jump(jump_mnemonic: str) -> str:
    if jump_mnemonic not in jump_to_binary:
        return INVALID_MNEMONIC_BINARY_CODE
    return jump_to_binary[jump_mnemonic]
