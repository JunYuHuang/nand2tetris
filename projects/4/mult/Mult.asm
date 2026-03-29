// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

  // set product result `R2` to 0
  @R2
  M = 0

  // set up loop by setting variable `i` to `R0`'s value
  @R0
  D = M
  @i
  M = D

// while index `i` > 0, add `R1` to `R2` and `i--`
(LOOP)
  // exit loop if `i` is 0
  @i
  D = M
  @LOOPEND
  D ; JEQ

  // add `R1` to `R2`
  @R1
  D = M
  @R2
  M = D + M

  // decrement `i`
  @i
  M = M - 1

  // repeat the loop
  @LOOP
  0 ; JMP

(LOOPEND)

// end program with an infinite loop
(END)
@END
0 ; JMP
