from hack_assembler import code

INVALID_MNEMONIC_BINARY_CODE = "INVALID_MNEMONIC_BINARY_CODE"

def test_dest():
    assert code.dest("lmao") == INVALID_MNEMONIC_BINARY_CODE
    assert code.dest("") == "000"
    assert code.dest("AM") == "101"

def test_comp():
    assert code.comp("lmao") == INVALID_MNEMONIC_BINARY_CODE
    assert code.comp("-1") == "111010"
    assert code.comp("-A") == "110011"
    assert code.comp("-M") == "110011"

def test_jump():
    assert code.jump("null") == INVALID_MNEMONIC_BINARY_CODE
    assert code.jump("") == "000"
    assert code.jump("JLT") == "100"
    assert code.jump("JMP") == "111"
