from hack_assembler.parser import *

A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"
INVALID_INSTRUCTION = "INVALID_INSTRUCTION"
INVALID_SYMBOL = "INVALID_SYMBOL"
INVALID_DEST = "INVALID_DEST"
INVALID_COMP = "INVALID_COMP"
INVALID_JUMP = "INVALID_JUMP"

def test_is_executable_line():
    assert is_executable_line(123) == False
    assert is_executable_line("      ") == False
    assert is_executable_line("   // i am comment  ") == False
    assert is_executable_line("a") == True
    assert is_executable_line("") == False
    assert is_executable_line("\n") == False
    assert is_executable_line("  // If (D > 0) goto ITSR0") == False
    assert is_executable_line("// Symbol-less version of the Rect.asm program.") == False
    assert is_executable_line("// Designed for testing the basic version of the assembler.") == False
    assert is_executable_line("@0") == True

def test_is_a_instruction():
    assert is_a_instruction("a  ") == False
    assert is_a_instruction(" @i  ") == True
    assert is_a_instruction("@my_variable") == True
    assert is_a_instruction("@9asd") == False
    assert is_a_instruction("@_my:12A2_s") == True
    assert is_a_instruction("@-1") == False
    assert is_a_instruction("@0") == True
    assert is_a_instruction("@1.2") == False
    assert is_a_instruction("@32768") == False
    assert is_a_instruction("@32767") == True

def test_is_c_instruction():
    assert is_c_instruction("M=1;JLE") == True
    assert is_c_instruction("DM=0") == True
    assert is_c_instruction("-A;JMP") == True
    assert is_c_instruction("D&A") == True
    assert is_c_instruction("=D+1") == False
    assert is_c_instruction("!M;") == False
    assert is_c_instruction("!D-1") == False
    assert is_c_instruction("D&M;null") == False

def test_is_l_instruction():
    assert is_l_instruction(" as  ") == False
    assert is_l_instruction("()") == False
    assert is_l_instruction("  )") == False
    assert is_l_instruction(" ( ") == False
    assert is_l_instruction("(a)") == True
    assert is_l_instruction("   (LOOP) ") == True
    assert is_l_instruction("(_myV4r:$.)") == True

def test_get_symbol():
    assert get_symbol(" @  ") == INVALID_SYMBOL
    assert get_symbol("  @ sum ") == "sum"
    assert get_symbol("   (LOOP) ") == "LOOP"

def test_get_dest():
    assert get_dest(" @lol   ") == INVALID_DEST
    assert get_dest("ADM=-A") == "ADM"
    assert get_dest("M=1;JLE") == "M"
    assert get_dest("D|A") == ""
    assert get_dest("-A;JMP") == ""

def test_get_comp():
    assert get_comp(" @lol   ") == INVALID_COMP
    assert get_comp("ADM=-A") == "-A"
    assert get_comp("M=1;JLE") == "1"
    assert get_comp("D|A") == "D|A"
    assert get_comp("-A;JMP") == "-A"

def test_get_jump():
    assert get_jump(" @lol   ") == INVALID_JUMP
    assert get_jump("ADM=-A") == ""
    assert get_jump("M=1;JLE") == "JLE"
    assert get_jump("D|A") == ""
    assert get_jump("-A;JMP") == "JMP"

def test_Parser_class_with_add_program():
    parser = Parser("../add/Add.asm")
    assert parser.has_more_lines() == True
    assert parser.fd_line == ""
    
    # Go to line 8: `@2`
    parser.advance()
    assert parser.fd_line == "@2"
    assert parser.instruction_type() == A_INSTRUCTION
    assert parser.symbol() == "2"
    assert parser.dest() == INVALID_DEST
    assert parser.comp() == INVALID_COMP
    assert parser.jump() == INVALID_JUMP

    # Go to line 11: `D=D+A`
    parser.advance()
    parser.advance()
    parser.advance()
    assert parser.fd_line == "D=D+A"
    assert parser.instruction_type() == C_INSTRUCTION
    assert parser.symbol() == INVALID_SYMBOL
    assert parser.dest() == "D"
    assert parser.comp() == "D+A"
    assert parser.jump() == ""

    # Go to line 14: ``
    parser.advance()
    parser.advance()
    parser.advance()
    assert parser.has_more_lines() == False
    assert parser.fd_line == ""

    # Try to go out-of-bounds (line 15)
    parser.advance()
    assert parser.has_more_lines() == False
    assert parser.fd_line == ""

def test_Parser_class_with_max_program():
    parser = Parser("../max/Max.asm")
    assert parser.has_more_lines() == True
    assert parser.fd_line == ""
    
    # Go to line 10: `  @R0`
    parser.advance()
    assert parser.fd_line == "  @R0"
    assert parser.instruction_type() == A_INSTRUCTION
    assert parser.symbol() == "R0"
    assert parser.dest() == INVALID_DEST
    assert parser.comp() == INVALID_COMP
    assert parser.jump() == INVALID_JUMP

    # Go to line 11: `  D=M`
    parser.advance()
    assert parser.fd_line == "  D=M"

    # Go to line 12: `  @R1`
    parser.advance()
    assert parser.fd_line == "  @R1"

    # Go to line 13: `  D=D-M`
    parser.advance()
    assert parser.fd_line == "  D=D-M"

    # Go to line 15: `  @ITSR0`
    parser.advance()
    assert parser.fd_line == "  @ITSR0"
    assert parser.instruction_type() == A_INSTRUCTION
    assert parser.symbol() == "ITSR0"
    assert parser.dest() == INVALID_DEST
    assert parser.comp() == INVALID_COMP
    assert parser.jump() == INVALID_JUMP

def test_Parser_class_with_rectl_program():
    parser = Parser("../rect/RectL.asm")
    assert parser.has_more_lines() == True
    assert parser.fd_line == ""
    
    # Go to line 9: `@0`
    parser.advance()
    assert parser.fd_line == "@0"
    assert parser.instruction_type() == A_INSTRUCTION
    assert parser.symbol() == "0"
    assert parser.dest() == INVALID_DEST
    assert parser.comp() == INVALID_COMP
    assert parser.jump() == INVALID_JUMP

    # Go to line 10: `D=M`
    parser.advance()
    assert parser.fd_line == "D=M"
    assert parser.instruction_type() == C_INSTRUCTION
    assert parser.symbol() == INVALID_SYMBOL
    assert parser.dest() == "D"
    assert parser.comp() == "M"
    assert parser.jump() == ""
