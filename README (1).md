# 🔐 Password Generator


A simple command-line password generator written in Python. It creates random passwords of a length you choose, using the cryptographically secure `secrets` module.

## Features

- Password length from **8 to 20** characters
- Uses `secrets` (not `random`), which is designed for security-sensitive values
- No external dependencies
- Clear message if the length is out of range

## Requirements

- Python 3.13.7 (the version the project was written on)
- Should also work on any Python 3.6+, since the `secrets` module was added in 3.6

## Usage

1. Clone the repository or download the script.
2. Run it:

   ```bash
   python secpass.py
   ```

3. Enter the desired password length when prompted.

### Example

```
How long should the password be? 8-20 digits12
k3#x9qmw2ptz
```

If the length is outside the allowed range:

```
How long should the password be? 8-20 digits5
password is too short or too long
```

## How it works

1. The program asks for the password length.
2. It checks that the number is between 8 and 20.
3. For each position, it picks one random character from the allowed set with `secrets.choice()`.
4. The characters are joined into a string and printed.

## Character set

Passwords can contain:

- lowercase Latin letters `a–z`
- digits `0–9`
- the symbol `#`


