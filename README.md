# String Calculator Kata

This is a simple String Calculator implemented using Test-Driven Development (TDD).

## Features:
- Sums numbers from a string separated by commas or newlines.
- Supports multiple custom delimiters of any length as defined in the string.
- Ignores numbers greater than 1000.
- Raises an exception for negative numbers.

## Usage:
You can use the `StringCalculator`'s `add` method to sum numbers in a string separated by commas, newlines, or custom delimiters (e.g., `//[delimiter]\n`). Custom delimiters can be of any length and defined within square brackets. 

Example: `calculator.add("//[;]\n1;2;3")` will return 6.
