class SymbolTable:
    def __init__(self):
        self.symbol_to_address = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
        }
        self.next_variable_address = self.symbol_to_address["R15"] + 1
    
    def add_entry(
        self, symbol: str, address: int | None = None, is_variable: bool = True
    ) -> None:
        address = address if address else self.next_variable_address
        self.symbol_to_address[symbol] = address
        if is_variable:
            self.next_variable_address += 1

    def contains(self, symbol: str) -> bool:
        return symbol in self.symbol_to_address

    def get_address(self, symbol: str) -> int:
        if not self.contains(symbol):
            return -1
        return self.symbol_to_address[symbol]
