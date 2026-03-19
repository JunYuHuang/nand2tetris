# 3. Memory

- mental patterns / shortcuts for memory chips:
  ```
  Split address:
  upper bits → choose block
  lower bits → pass down


  RAM(2^(n+k)) =
    DMux(upper n bits) → 2^n smaller RAMs
    Mux (upper n bits) ← outputs
    lower k bits → passed into each smaller RAM
  ```
