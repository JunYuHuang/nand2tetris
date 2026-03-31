// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// outer loop for reading the key pressed
(LOOP_OUTER)

  // store the key character code in variable `keyPressed`
  @KBD
  D = M
  @keyPressed
  M = D

  // set the counter and index for the inner loop
  // we are looping 8192 times because:
  // 1. there are 512 x 256 = 131072 pixels
  // 2. pixels are represented in groups of 16 in RAM
  // 3. we traverse all pixels 16 at a time (131072 / 16) = 8192 times
  @8192
  D = A - 1
  @screenOffset
  M = D

  // if no key was pressed, set pixel color to white (16-bits of all 0's)
  @keyPressed
  D = M
  @SET_PIXELS_WHITE
  D ; JEQ

  // if any key was pressed, set pixel color to black (16-bits of all 1's)
  @keyPressed
  D = M
  @SET_PIXELS_BLACK
  D ; JNE

  (SET_PIXELS_WHITE)
    @pixelColor
    M = 0

    @LOOP_INNER
    0 ; JMP

  (SET_PIXELS_BLACK)
    @pixelColor
    M = -1

    @LOOP_INNER
    0 ; JMP

  // inner loop for coloring all pixels of the 512 x 256 screen
  (LOOP_INNER)

    // exit inner loop if looped thru all screen pixels
    @screenOffset
    D = M
    @LOOP_INNER_END
    D ; JLT

    // store the address of the 16 pixels at `RAM[SCREEN + offset]`
    // in the variable `screenAddress`
    @screenOffset
    D = M
    @SCREEN
    D = D + A
    @screenAddress
    M = D

    // set the 16 pixels at `RAM[screenAddress]` to `pixelColor`'s value
    @pixelColor
    D = M
    @screenAddress
    A = M
    M = D

    // decrement `screenOffset` by 1
    @screenOffset
    M = M - 1

    // continue the inner loop
    @LOOP_INNER
    0 ; JMP

  (LOOP_INNER_END)

// continue the outer loop
@LOOP_OUTER
0 ; JMP
