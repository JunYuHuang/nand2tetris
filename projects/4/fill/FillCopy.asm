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

  // get the key pressed
  @KBD
  D = M
  @keyPressed
  M = D

  // set the counter and index for the inner loop
  @255
  D = A
  @screenRowOffset
  M = D

  // if no key was pressed, set pixel color to white (16-bits of all 0's)
  @keyPressed
  D = M
  @SET_PIXEL_WHITE
  D ; JEQ

  (SET_PIXEL_WHITE)
  @pixelColor
  M = 0

  @LOOP_INNER
  0 ; JMP

  // if any key was pressed, set pixel color to black (16-bits of all 1's)
  @keyPressed
  D = M
  @SET_PIXEL_BLACK
  D ; JNE

  (SET_PIXEL_BLACK)
  @pixelColor
  M = -1

  @LOOP_INNER
  0 ; JMP

  // inner loop for coloring all pixels of the 512 x 256 screen
  (LOOP_INNER)

    // exit inner loop if looped thru all screen rows pixels
    @screenRowOffset
    D = M
    @LOOP_INNER_END
    D ; JLT

    // compute and store the screen row index in `screenRow`
    @SCREEN
    D = M
    @screenRow
    M = D
    D = M
    @screenRowOffset
    D = D + M
    @screenRow
    M = D

    // set the 16 pixels at `RAM[screenRow]` to `pixelColor`'s value
    @pixelColor
    D = M
    @screenRow
    M = D

    // decrement `screenRowOffset` by 1
    @screenRowOffset
    M = M - 1

    // continue the inner loop
    @LOOP_INNER
    0 ; JMP

  (LOOP_INNER_END)

// continue the outer loop
@LOOP_OUTER
0 ; JMP
