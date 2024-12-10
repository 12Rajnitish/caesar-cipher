
# Caesar Cipher

This is a Python implementation of the Caesar Cipher encryption and decryption technique. The program allows you to encode and decode messages by shifting letters of the alphabet.

## Features
- **Encoding**: Shift letters forward in the alphabet by a specified number.
- **Decoding**: Shift letters backward in the alphabet by the same number.
- **Handles non-alphabet characters**: Spaces, punctuation, and other symbols remain unchanged.
- **User-friendly interface**: The program prompts the user for input and allows continuous use.

## Usage

1. Run the program.
2. You will be prompted to choose between encoding and decoding.
3. Enter your message to encode or decode.
4. Enter the number of positions to shift the letters.
5. The program will display the encoded or decoded result.
6. You can continue encoding/decoding other messages or exit by typing `no`.

## Example

```bash
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
Here is the encoded result: khoor
```

## Requirements

- Python 3.x
- Ensure the `art.py` file is in the same directory as the main program.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/12Rajnitish/caesar-cipher.git
   ```

2. Navigate to the project directory:
   ```bash
   cd caesar-cipher
   ```

3. Run the program:
   ```bash
   python caesar_cipher.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
