// Sets the `A` register to the address of the RAM register 
// that represents the 16 left-most pixels at the screen's
// top row:
// @SCREEN

// Sets this RAM register to 1111111111111111
// M = -1

//
// Blacken all 512 x 256 pixels of the screen
//

// loop 8192 times to traverse all 512 x 256 pixels in the screen in 16-bit increments
@8192
D = A
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
  A = A + D
  M = -1

  // i--
  @i
  M = M - 1

  // next iteration
  @LOOP_OUTER
  0 ; JMP

// end program with infinite loop
(END)
@END
0 ; JMP
