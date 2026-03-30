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

  // DEBUG mode: set `keyPressed` to 1 indicating some key was pressed
  @keyPressed
  M = 1

  // set the counter and index for the inner loop
  @8192
  D = A - A
  @screenOffset
  M = D

  // DEBUG mode: set `pixelColor` to black (all 16 bits are 1's)
  @pixelColor
  M = -1

  // inner loop for coloring all pixels of the 512 x 256 screen
  (LOOP_INNER)

    // exit inner loop if looped thru all screen pixels
    @screenOffset
    D = M
    @LOOP_INNER_END
    D ; JLT

    // make the 16 pixels at `RAM[SCREEN + offset]` black

    // set the 16 pixels at `RAM[screen]` to `pixelColor`'s value
    @pixelColor
    D = M
    @screen
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
