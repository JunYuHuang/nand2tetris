// loop 8192 times to traverse all 512 x 256 pixels in the screen in 16-bit increments
@8192
D = A - 1
@i
M = D

(LOOP_OUTER)

  // exit loop if i < 0
  @i
  D = M
  @END
  D ; JLT

  // make the 16 pixels at `RAM[SCREEN + offset]` black
  @i
  D = M
  @SCREEN
  A = D + A
  M = -1

  // decrement `i` by 1
  @i
  M = M - 1

  // go to next iteration
  @LOOP_OUTER
  0 ; JMP

// end program with infinite loop
(END)
@END
0 ; JMP
