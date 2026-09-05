from hack_assembler.main import *

"""
To run this test correctly, modify `../src/hack_assembly/main.py`:
- comment out `main()` function call
"""

def test_is_symbol_constant():
    assert is_symbol_constant("") == False
    assert is_symbol_constant("9asd") == False
    assert is_symbol_constant("   ") == False
    assert is_symbol_constant("_my:12A2_s") == False
    assert is_symbol_constant("-1") == False
    assert is_symbol_constant("0") == True
    assert is_symbol_constant("123") == True
    assert is_symbol_constant("1.2") == False
    assert is_symbol_constant("32768") == False
    assert is_symbol_constant("32767") == True
