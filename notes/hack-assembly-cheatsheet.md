# Hack Assembly Cheat Sheet

# ⚙️ 1. Big Picture Model

Hack computer has:

* **Registers**
  * `A` → address / general-purpose
  * `D` → data register
* **Memory**
  * `M` → refers to `RAM[A]`
* **Program Counter (PC)** → tracks current instruction
  * `instruction` → refers to `ROM[A]`

👉 Key idea:

> `M` is not a register — it means “memory at address A”

# 🔤 2. Two Instruction Types


## 🅰️ A-instruction

```asm
@value
```

### Meaning:

* Set `A = value`

### Examples:

```asm
@10        // A = 10
@i         // A = address of variable i
@LOOP      // A = address of label LOOP
```

---

## 🅲 C-instruction

```asm
dest = comp ; jump
```

All parts are optional, but `comp` is required.

---

# 🧩 3. C-instruction Breakdown

---

## ✅ `comp` (computation)

This is the **ALU operation**.

### Constants

```asm
0   1   -1
```

### Single registers

```asm
D   A   M
```

### Negation / NOT

```asm
-D   -A   -M
!D   !A   !M
```

### Increment / Decrement

```asm
D+1   A+1   M+1
D-1   A-1   M-1
```

### Arithmetic

```asm
D+A   D+M
D-A   D-M
A-D   M-D
```

### Bitwise

```asm
D&A   D&M
D|A   D|M
```

---

## 📦 `dest` (where result goes)

Controls which registers are updated.

```asm
M     D     A
MD    AM    AD
AMD
```

### Examples:

```asm
D=M        // D = RAM[A]
M=D+1      // RAM[A] = D+1
AD=D+A     // A and D both updated
```

---

## 🚀 `jump` (conditional jump)

Triggers jump based on `comp` result.

```asm
JGT   // > 0
JEQ   // == 0
JGE   // >= 0
JLT   // < 0
JNE   // != 0
JLE   // <= 0
JMP   // unconditional
```

### Example:

```asm
D;JGT     // if D > 0, jump to A
```

👉 Important:

> Jump goes to the address currently in `A`

---

# 🔁 4. Labels (Flow Control)

```asm
(LOOP)
```

Defines a label.

### Example:

```asm
(LOOP)
@LOOP
0;JMP
```

Creates an infinite loop.

---

# 📦 5. Variables (Symbols)

```asm
@i
```

* First time seen → assigned RAM address starting at 16

So:

```asm
@i
M=0
```

means:

* `i` is stored in RAM[16], then RAM[17], etc.

---

# 🧮 6. Predefined Symbols

---

## 🧱 Registers

```asm
R0  - R15   → RAM[0] - RAM[15]
```

---

## 🖥️ Special Pointers

```asm
SP     → 0
LCL    → 1
ARG    → 2
THIS   → 3
THAT   → 4
```

---

## 🖼️ Memory-mapped I/O

```asm
SCREEN → 16384
KBD    → 24576
```

---

# 🧠 7. Common Patterns (VERY IMPORTANT)

---

## ➕ Set D = constant

```asm
@10
D=A
```

---

## 📥 Load from memory

```asm
@i
D=M
```

---

## 📤 Store to memory

```asm
@i
M=D
```

---

## ➕ Add two values

```asm
@x
D=M
@y
D=D+M
```

---

## 🔁 Infinite loop

```asm
(END)
@END
0;JMP
```

---

## ❓ If condition (if D > 0)

```asm
@LABEL
D;JGT
```

---

## 🔄 While loop pattern

```asm
(LOOP)
   // condition
   @END
   D;JEQ   // exit if condition met

   // body

   @LOOP
   0;JMP
(END)
```

---

# ⚠️ 8. Subtle Gotchas

---

## ❗ 1. `M` depends on `A`

```asm
@10
M=1   // writes to RAM[10]
```

---

## ❗ 2. Jump uses `A`

```asm
@LOOP
D;JGT   // jumps to LOOP if D > 0
```

---

## ❗ 3. No direct memory-to-memory ops

❌ Not allowed:

```asm
M=M+1   // OK
M=D+M   // OK
M=M+M   // ❌ (invalid comp)
```

---

## ❗ 4. No multiplication/division

You must build:

* multiplication → repeated addition
* division → repeated subtraction

---

# 🧪 9. Mental Execution Model

For each C-instruction:

1. Compute `comp`
2. Store result in `dest`
3. If `jump` → possibly change PC

---

# 🚀 10. Project 4 Mindset

You’ll likely implement:

### 🧮 Mult.asm

* Loop
* Counter
* Accumulator

### 🖥️ Fill.asm

* Infinite loop
* Check keyboard (`KBD`)
* Write to screen (`SCREEN`)

---

# 🔑 Final Intuition

> You are manually controlling:
>
> * **Registers (A, D)**
> * **Memory (M)**
> * **Control flow (jumps)**

Everything reduces to:

```asm
Load → Compute → Store → Jump
```
