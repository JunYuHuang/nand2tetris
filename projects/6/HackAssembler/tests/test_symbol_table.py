from hack_assembler.symbol_table import SymbolTable

def test_contains():
    my_symbol_table = SymbolTable()

    assert my_symbol_table.contains("lol") == False
    assert my_symbol_table.contains("R5") == True
    assert my_symbol_table.contains("KBD") == True
    assert my_symbol_table.contains("kbd") == False

def test_add_entry():
    my_symbol_table = SymbolTable()
    assert ("lol" in my_symbol_table.symbol_to_address) == False

    my_symbol_table.add_entry("lol", 30)
    assert ("lol" in my_symbol_table.symbol_to_address) == True

    my_symbol_table.add_entry("var")
    assert ("var" in my_symbol_table.symbol_to_address) == True

def test_get_address():
    my_symbol_table = SymbolTable()
    assert my_symbol_table.get_address("not_here") == -1
    assert my_symbol_table.get_address("R15") == 15

    my_symbol_table.add_entry("i")
    assert my_symbol_table.get_address("i") == 16
