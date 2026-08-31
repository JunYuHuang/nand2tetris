# HackAssembler

## Usage

TODO

## Prereqs

Install `astral-sh/uv`:
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Test

```
# Go to project root:
cd nand2tetris/projects/6/HackAssembler

# Run all tests
uv run pytest

# Run a specific test
uv run pytest tests/test_symbol_table.py
```

## Build

```
# Go to project root:
cd nand2tetris/projects/6/HackAssembler

# Option 1: for production
uv run pyinstaller --name HackAssembler --onefile src/hack_assembler/main.py

# Option 2: for dev work
rm -rf build dist HackAssembler.spec

uv run pyinstaller --clean --noconfirm --name HackAssembler --onefile src/hack_assembler/main.py
```
