import re

#
# Constants
#
A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"
INVALID_INSTRUCTION = "INVALID_INSTRUCTION"
INVALID_SYMBOL = "INVALID_SYMBOL"
INVALID_DEST = "INVALID_DEST"
INVALID_COMP = "INVALID_COMP"
INVALID_JUMP = "INVALID_JUMP"

#
# Helper functions
#
def is_executable_line(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    if len(text_line) == 0:
        return False
    if text_line == "\n" or text_line[:2] == "//":
        return False
    return True

def is_a_instruction(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    if len(text_line) < 2:
        return False
    if text_line[0] != "@":
        return False
    symbol_or_constant = text_line[1:]
    symbol_regex = re.compile(
        r'^(_|\.|\$|\:|[a-zA-Z])(_|\.|\$|\:|\w)*$'
    )
    if symbol_regex.match(symbol_or_constant):
        return True
    if (
        re.compile(r'^\d+$').match(symbol_or_constant) and
        (0 <= int(symbol_or_constant) <= 32767) and
        symbol_or_constant == str(int(symbol_or_constant))
    ):
        return True
    return False

# Valid C-instruction formats:
# [dest'=']{comp}[';'jump]
# [dest'=']{comp}
# {comp}[';'jump]
# {comp}
def is_c_instruction(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    full_c_instruction_regex = re.compile(
        r'^([ADM]{1,3}\=)?(0|1|\-|\!|\+|\&|\||A|D|M){1,3}(\;J[GTEQLNMP]{2})?$'
    )
    if full_c_instruction_regex.match(text_line):
        return True
    return False

def is_l_instruction(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    label_regex = re.compile(
        r'^\((_|\.|\$|\:|[a-zA-Z])(_|\.|\$|\:|\w)*\)$'
    )
    return bool(label_regex.match(text_line))

def get_symbol(a_or_l_instruction: str) -> str:
    a_or_l_instruction = a_or_l_instruction.replace(" ", "")
    if is_a_instruction(a_or_l_instruction):
        return a_or_l_instruction[1:]
    if is_l_instruction(a_or_l_instruction):
        return a_or_l_instruction[1:-1]
    return INVALID_SYMBOL

def get_dest(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_DEST
    equals_pos = c_instruction.find("=")
    if equals_pos == -1:
        return ""
    return c_instruction[:equals_pos]

def get_comp(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_COMP
    equals_pos = c_instruction.find("=")
    if equals_pos != -1:
        c_instruction = c_instruction.replace(
            c_instruction[:equals_pos + 1], ""
        )
    semicolon_pos = c_instruction.find(";")
    if semicolon_pos != -1:
        c_instruction = c_instruction.replace(
            c_instruction[semicolon_pos:], ""
        )
    return c_instruction

def get_jump(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_JUMP
    semicolon_pos = c_instruction.find(";")
    if semicolon_pos == -1:
        return ""
    return c_instruction[semicolon_pos + 1:]

class Parser:
    def __init__(self, symbolic_assembly_file_path: str):
        self.symbolic_assembly_file_path = symbolic_assembly_file_path
        self.fd = open(
            symbolic_assembly_file_path, "r", encoding="utf-8"
        )
        self.fd_last_pos = 0
        self.fd_curr_pos = 0
        self.fd_line = ""
        while self.fd.read() != "":
            self.fd_last_pos = self.fd.tell()
            self.fd.read()
        self.fd.seek(0)

    def __del__(self):
        if self and self.fd:
            self.fd.close()

    def reset(self) -> None:
        self.fd.seek(0)
        self.fd_curr_pos = 0
    
    def has_more_lines(self) -> bool:
        return self.fd_curr_pos < self.fd_last_pos

    # TODO: to fix
    def advance(self) -> None:
        while self.has_more_lines():
            self.fd_line = self.fd.readline()[:-1]   # skip last newline `\n` char
            self.fd_curr_pos = self.fd.tell()

            if is_executable_line(self.fd_line):
                # print(f"Line '{self.fd_line}' is executable")
                return
        # at last line; no more lines to move to
        self.fd_line = ""

    def instruction_type(self) -> str:
        if is_a_instruction(self.fd_line):
            return A_INSTRUCTION
        elif is_c_instruction(self.fd_line):
            return C_INSTRUCTION
        # TODO: untested in `test_parser.py`
        elif is_l_instruction(self.fd_line):
            return L_INSTRUCTION
        else:
            return INVALID_INSTRUCTION

    def symbol(self) -> str:
        # e.g., `(LOOP)`
        if is_l_instruction(self.fd_line):
            return self.fd_line.replace(" ", "")[1:-1]
        if not is_a_instruction(self.fd_line):
            return INVALID_SYMBOL
        return self.fd_line.replace(" ", "")[1:]

    def dest(self) -> str:
        if not is_c_instruction(self.fd_line):
            return INVALID_DEST
        return get_dest(self.fd_line)

    def comp(self) -> str:
        if not is_c_instruction(self.fd_line):
            return INVALID_COMP
        return get_comp(self.fd_line)

    def jump(self) -> str:
        if not is_c_instruction(self.fd_line):
            return INVALID_JUMP
        return get_jump(self.fd_line)
