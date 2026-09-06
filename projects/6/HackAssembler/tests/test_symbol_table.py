from hack_assembler.symbol_table import SymbolTable

def test_contains():
    symbol_table = SymbolTable()

    assert symbol_table.contains("lol") == False
    assert symbol_table.contains("R5") == True
    assert symbol_table.contains("KBD") == True
    assert symbol_table.contains("kbd") == False

def test_add_entry():
    symbol_table = SymbolTable()
    assert ("lol" in symbol_table.symbol_to_address) == False

    symbol_table.add_entry("lol", 30)
    assert ("lol" in symbol_table.symbol_to_address) == True

    symbol_table.add_entry("var")
    assert ("var" in symbol_table.symbol_to_address) == True

    symbol_table.add_entry("LABEL", is_variable=False)
    assert ("LABEL" in symbol_table.symbol_to_address) == True
    assert symbol_table.symbol_to_address["LABEL"] == 18

    symbol_table.add_entry("LABEL2", False)
    assert ("LABEL" in symbol_table.symbol_to_address) == True
    assert symbol_table.symbol_to_address["LABEL2"] == 18
    assert symbol_table.next_variable_address == 19

    symbol_table.add_entry("LABEL3", 42, False)
    assert ("LABEL" in symbol_table.symbol_to_address) == True
    assert symbol_table.symbol_to_address["LABEL3"] == 42
    assert symbol_table.next_variable_address == 19

def test_get_address():
    symbol_table = SymbolTable()
    assert symbol_table.get_address("not_here") == -1
    assert symbol_table.get_address("R15") == 15

    symbol_table.add_entry("i")
    assert symbol_table.get_address("i") == 16
