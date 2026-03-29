// Blacken the first 16 pixels of the top left corner of 
// a 512 x 256 screen

// Sets the `A` register to the address of the RAM register 
// that represents the 16 left-most pixels at the screen's
// top row:
@SCREEN

// Sets this RAM register to 1111111111111111
M = -1
