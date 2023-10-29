#!/usr/bin/node
/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/

// Check if there are at least two command-line arguments (including the script name).
if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1);
}

// Parse the size argument as an integer.
const size = parseInt(process.argv[2]);

// Check if the parsed size is a valid positive integer.
if (isNaN(size) || size < 1) {
    process.stderr.write("Invalid size. Please provide a positive integer.\n");
    process.exit(1);
}

// Loop to print the square of "#" characters.
for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}