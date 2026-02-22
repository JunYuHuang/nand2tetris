# 1. Boolean Logic - Notes

- boolean algebra cheatsheet:
```
IDENTITY
A · 1 = A
A + 0 = A

NULL
A · 0 = 0
A + 1 = 1

IDEMPOTENT
A · A = A
A + A = A

COMPLEMENT
A · ¬A = 0
A + ¬A = 1
¬¬A = A

COMMUTATIVE
A · B = B · A
A + B = B + A

ASSOCIATIVE
(A · B) · C = A · (B · C)
(A + B) + C = A + (B + C)

DISTRIBUTIVE
A · (B + C) = (A · B) + (A · C)
A + (B · C) = (A + B) · (A + C)

ABSORPTION
A + (A · B) = A
A · (A + B) = A

DE MORGAN
¬(A · B) = ¬A + ¬B
¬(A + B) = ¬A · ¬B

NAND TRICKS
¬A = A NAND A
A · B = ¬(A NAND B)
A + B = (¬A) NAND (¬B)
```