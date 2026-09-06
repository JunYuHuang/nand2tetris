# HackAssembler

## Prereqs

Install software package `astral-sh/uv`:
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Run Usage

Run in Python:
```
# Go to project root:
cd nand2tetris/projects/6/HackAssembler

uv run src/hack_assembler/main.py {path_to_asm_file}

# Example 1:
uv run src/hack_assembler/main.py ../add/Add.asm

# Example 2:
uv run python -m hack_assembler.main ../add/Add.asm

# Example 3:
uv run HackAssembler ../add/Add.asm
```

Run as standalone executable binary:
```
# Go to `dist` folder in project root:
cd nand2tetris/projects/6/HackAssembler/dist

# Add execute permissions if needed:
chmod +x HackAssembler

# Example run:
./HackAssembler ../../add/Add.asm
```

## Build

```
# Go to project root:
cd nand2tetris/projects/6/HackAssembler

# Optional clean-up:
rm -rf build dist HackAssembler.spec

# Required:
uv run pyinstaller --clean --noconfirm --name HackAssembler --onefile src/hack_assembler/main.py
```

Built executable lives at `./dist/HackAssembler`

## Test

```
# Go to project root:
cd nand2tetris/projects/6/HackAssembler

# Run tests
uv run pytest tests/test_symbol_table.py
uv run pytest tests/test_code.py
uv run pytest tests/test_parser.py
uv run pytest tests/test_integration.py
uv run pytest tests/main.py
```
