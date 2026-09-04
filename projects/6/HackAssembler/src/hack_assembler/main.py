# TODO: fix broken imports when running test `uv run pytest tests/test_main.py`
# import parser
from parser import *
import code
from symbol_table import SymbolTable
import sys
import os

#
# Constants
#
INVALID_DIR = "INVALID_DIR"
INVALID_FILE = "INVALID_FILE"
A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"

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

# TODO: to test
# Copied and modified from `is_a_instruction()` function in `./parser.py`
def is_symbol_constant(symbol: str) -> bool:
    return (
        re.compile(r'^\d+$').match(symbol) and
        (0 <= int(symbol) <= 32767) and
        symbol == str(int(symbol))
    )

# TODO: to test
def main():
    if len(sys.argv) != 2:
        sys.exit("[Error] Missing input symbolic Hack assembly '.asm' file")
    input_file_path = sys.argv[1]
    if not is_valid_symbolic_assembly_file_path(input_file_path):
        sys.exit(f"[Error] '{input_file_path}' is not a valid Hack assembly '.asm' file")
    my_parser = None
    symbol_to_address = SymbolTable()
    output_dir = symbolic_assembly_file_parent_dir(input_file_path)
    output_path = f"{output_dir}{os.sep}{symbolic_assembly_file(input_file_path)[:-4]}.hack"
    output_file = None

    try:
        my_parser = parser.Parser(input_file_path)
        output_file = open(output_path, "w", encoding="utf-8")
        output_line = ""

        # 1st pass thru input `.asm` file
        while my_parser.has_more_lines():
            my_parser.advance()
            if (
                my_parser.instruction_type() != A_INSTRUCTION or
                my_parser.instruction_type() != L_INSTRUCTION
            ):
                continue
            symbol = my_parser.symbol()
            if is_symbol_constant(symbol):
                continue
            if symbol_to_address.contains(symbol):
                continue
            symbol_to_address.add_entry(symbol)
            
        # 2nd pass thru input `.asm` file
        my_parser.reset()
        while my_parser.has_more_lines():
            my_parser.advance()
            if my_parser.instruction_type() == C_INSTRUCTION:
                dest_bits = code.dest(my_parser.dest())
                comp_bits = code.comp(my_parser.comp())
                jump_bits = code.jump(my_parser.jump())
                output_line = f"111{dest_bits}{comp_bits}{jump_bits}\n"
            elif my_parser.instruction_type() == A_INSTRUCTION:
                symbol = my_parser.symbol()
                if not is_symbol_constant(symbol):
                    symbol = symbol_to_address.get_address(symbol)

                # `format()` call converts integer constant as a 15-bit binary value
                output_line = f"0{format(int(symbol), '015b')}\n"
            else:
                continue
            output_file.write(output_line)
    except Exception as err:
        sys.exit(f"[Error] Unexpected '{err}', {type(err)=}")
    finally:
        if my_parser:
            del my_parser
        if output_file:
            output_file.close()

main()
