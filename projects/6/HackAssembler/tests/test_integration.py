import hack_assembler.parser as parser
import hack_assembler.code as code
from hack_assembler.symbol_table import SymbolTable
import sys
import os
import re

#
# Constants
#
INVALID_DIR = "INVALID_DIR"
INVALID_FILE = "INVALID_FILE"
A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"

#
# Helper functions
#
def is_valid_symbolic_assembly_file_path(path: str) -> bool:
    if len(path) < 5 or not os.path.exists(path):
        return False
    return path[-4:] == ".asm"

def symbolic_assembly_file_parent_dir(path: str) -> str:
    if not is_valid_symbolic_assembly_file_path(path):
        return INVALID_DIR
    full_path = os.path.abspath(path)
    last_sep_pos = full_path.rfind(os.sep)
    return full_path[:last_sep_pos]

def symbolic_assembly_file(path: str) -> str:
    if not is_valid_symbolic_assembly_file_path(path):
        return INVALID_FILE
    full_path = os.path.abspath(path)
    last_sep_pos = full_path.rfind(os.sep)
    return full_path[last_sep_pos + 1:]

# Copied and modified from `is_a_instruction()` function in `./parser.py`
def is_symbol_constant(symbol: str) -> bool:
    return bool(
        re.compile(r'^\d+$').match(symbol) and
        (0 <= int(symbol) <= 32767) and
        symbol == str(int(symbol))
    )

def test_process_add_program():
    my_parser = None
    symbol_table = SymbolTable()
    my_parser = parser.Parser("../add/Add.asm")
    output_line = ""

    # line 8: `@2`
    my_parser.advance()
    assert my_parser.fd_line == "@2"
    assert my_parser.instruction_type() == A_INSTRUCTION
    symbol = my_parser.symbol()
    output_line = f"0{format(int(symbol), '015b')}\n"
    assert output_line == "0000000000000010\n"

    # line 9: `D=A`
    my_parser.advance()
    assert my_parser.fd_line == "D=A"
    assert my_parser.instruction_type() == C_INSTRUCTION
    dest_bits = code.dest(my_parser.dest())
    assert dest_bits == "010"
    comp_bits = code.comp(my_parser.comp())
    assert comp_bits == "0110000"
    jump_bits = code.jump(my_parser.jump())
    assert jump_bits == "000"
    output_line = f"111{comp_bits}{dest_bits}{jump_bits}\n"
    assert output_line == "1110110000010000\n"

def test_process_max_program():
    my_parser = None
    symbol_table = SymbolTable()
    my_parser = parser.Parser("../max/Max.asm")
    output_line = ""
    line_number = -1

    # TODO: to fix
    # 1st pass thru `.asm` file: add label symbols to symbol table if needed
    while my_parser.has_more_lines():
        my_parser.advance()
        line_number += 1

        if not my_parser.instruction_type() == L_INSTRUCTION:
            continue
        symbol = my_parser.symbol()
        if is_symbol_constant(symbol):
            continue
        if symbol_table.contains(symbol):
            continue
        line_number -= 1
        symbol_table.add_entry(symbol, line_number + 1)

    assert symbol_table.contains("ITSR0") == True
    assert symbol_table.get_address("ITSR0") == 10
    assert symbol_table.contains("OUTPUT_D") == True
    assert symbol_table.get_address("OUTPUT_D") == 12
    assert symbol_table.contains("END") == True
    assert symbol_table.get_address("END") == 14

    # TODO: to test
    # 2nd pass thru input `.asm` file
    my_parser.reset()

    # line 10: `  @R0`
    my_parser.advance()
    assert my_parser.fd_line == "  @R0"
    assert my_parser.instruction_type() == A_INSTRUCTION
    symbol = my_parser.symbol()
    assert symbol == "R0"
    if not is_symbol_constant(symbol):
        symbol = symbol_table.get_address(symbol)
    output_line = f"0{format(int(symbol), '015b')}\n"
    assert output_line == "0000000000000000\n"

    # line 15: `  @ITSR0`
    my_parser.advance()
    my_parser.advance()
    my_parser.advance()
    my_parser.advance()
    assert my_parser.fd_line == "  @ITSR0"
    assert my_parser.instruction_type() == A_INSTRUCTION
    symbol = my_parser.symbol()
    assert symbol == "ITSR0"
    if not is_symbol_constant(symbol):
        symbol = symbol_table.get_address(symbol)
    assert symbol == 10
    output_line = f"0{format(int(symbol), '015b')}\n"
    assert output_line == "0000000000001010\n"
