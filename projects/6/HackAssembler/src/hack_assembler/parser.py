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

# TODO: to test
def is_executable_line(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    if len(text_line) == 0:
        return False
    if text_line[:2] == "//":
        return False
    return True

# TODO: to test
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
        0 <= int(symbol_or_constant) <= 32767) and
        value == str(int(symbol_or_constant)
    ):
        return True
    return False

# TODO: to test
# Valid C-instruction format and examples:
# [dest'=']{comp}[';'jump]
# todo
def is_c_instruction(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    # TODO
    no_dest_c_instruction_regex = re.compile(
        r'^$'
    )
    if no_dest_c_instruction_regex.match(text_line):
        return True
    # TODO
    full_c_instruction_regex = re.compile(
        r'^$'
    )
    if full_c_instruction_regex.match(text_line):
        return True
    return False

# TODO: to test
def is_l_instruction(text_line: str) -> bool:
    if not isinstance(text_line, str):
        return False
    text_line = text_line.replace(" ", "")
    label_regex = re.compile(
        r'^\((_|\.|\$|\:|[a-zA-Z])(_|\.|\$|\:|\w)*\)$'
    )
    return bool(label_regex.match(text_line))

# TODO: to test
def get_symbol(a_or_l_instruction: str) -> str:
    a_or_l_instruction = a_or_l_instruction.replace(" ", "")
    if is_a_instruction(a_or_l_instruction):
        return a_or_l_instruction[1:]
    if is_c_instruction(a_or_l_instruction):
        return a_or_l_instruction[1:-1]
    return INVALID_SYMBOL

# TODO: to test
def get_dest(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_DEST
    # TODO

# TODO: to test
def get_comp(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_COMP
    # TODO

# TODO: to test
def get_jump(c_instruction: str) -> str:
    c_instruction = c_instruction.replace(" ", "")
    if not is_c_instruction(c_instruction):
        return INVALID_JUMP
    # TODO


class Parser:
    def __init__(self, assembly_file_path: str):
        self.assembly_file_path

    # TODO: to test
    # - returns true if `assembly_file_path` has more lines
    # - else returns false
    def has_more_lines(self) -> bool:
        pass

    # TODO: to test
    def advance(self) -> None:
        pass

    # TODO: to test
    # - returns A, C, or L instruction string constants
    def instruction_type(self) -> str:
        pass

    # TODO: to test
    def symbol(self) -> str:
        pass

    # TODO: to test
    def comp(self) -> str:
        pass

    # TODO: to test
    def jump(self) -> str:
        pass
