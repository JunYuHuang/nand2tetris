# 1. Boolean Logic - Notes

- boolean algebra cheatsheet:
```
IDENTITY Laws: Doing nothing leaves the value unchanged
A · 1 = A
A + 0 = A

NULL (Annihilator) Laws: One value dominates the result
A · 0 = 0
A + 1 = 1

IDEMPOTENT Laws: Repeating doesn't change anything
A · A = A
A + A = A

COMPLEMENT Laws: A value and its opposite
A · ¬A = 0
A + ¬A = 1
¬¬A = A

COMMUTATIVE Laws: Order does not matter
A · B = B · A
A + B = B + A

ASSOCIATIVE Laws: Group does not matter
(A · B) · C = A · (B · C)
(A + B) + C = A + (B + C)

DISTRIBUTIVE Laws: AND distributes over OR and vice versa
A · (B + C) = (A · B) + (A · C)
A + (B · C) = (A + B) · (A + C)

ABSORPTION Laws: One term makes the other redundant
A + (A · B) = A
A · (A + B) = A

DE MORGAN Laws: How NOT interacts with AND / OR
¬(A · B) = ¬A + ¬B
¬(A + B) = ¬A · ¬B

NAND TRICKS
¬A = A NAND A
A · B = ¬(A NAND B)
A + B = (¬A) NAND (¬B)
```