# Collatz Sequence Generator

## Overview

The Collatz Sequence Generator is a simple Python program that generates and visualizes the Collatz sequence for a given starting number. The Collatz sequence, also known as the 3n + 1 problem, involves iteratively applying specific rules to a starting number until it reaches the value 1. The rules are as follows:

1. If the number is even, the next number is obtained by dividing it by 2.
2. If the number is odd, the next number is obtained by multiplying it by 3 and adding 1.

While the Collatz sequence problem is straightforward, it remains an unsolved mathematical conjecture that every starting number eventually reaches 1. The program provides users with an interactive interface to explore the sequences and analyze the behavior of different starting numbers.

## Features

1. **Collatz Sequence Generation**: Generates the Collatz sequence for a user-specified starting number.

2. **User Input Handling**: Ensures that the user enters a valid positive integer as the starting number.

3. **Interactive Interface**: Allows users to explore Collatz sequences for various starting numbers until they choose to exit.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/collatz-sequence-generator.git
   cd collatz-sequence-generator
   ```

2. **Run the Program:**

   ```bash
   python collatz_sequence_generator.py
   ```

3. **Follow On-screen Prompts:**

   - Enter a positive integer as the starting number.
   - Type "QUIT" to exit the program.

## Dependencies

- Python 3.x

## Contribution Guidelines

If you'd like to contribute to the project, follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure code quality.
4. Submit a pull request with a clear explanation of the changes.

## License

This project is licensed under the MIT License 

## Acknowledgments

- The Collatz Sequence problem was introduced by Lothar Collatz in 1937. More information about the Collatz sequence can be found [here](https://en.wikipedia.org/wiki/Collatz_conjecture).
