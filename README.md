# Sample Python Binary
This is a sample python binary which contains different implementations of common python tasks.

## Requirements (Development)
- Python 3.8+
- Pyinstaller
- Nuitka
- Fire
- Fernet

## Compiling with Nuitka
1. Execute the following to compile with Nuitka:
    ```
    env/bin/python -m nuitka binary.py
    ```
2. More [info](https://github.com/Nuitka/Nuitka)

## License File
The license file which is the `sample_license` contains the `LICENSE_EXPIRY` key. This uses a binary string under the `modules/settings.py` to decrypt the license file. The encryption and decryption is done using the `cryptography` library.

## Running Test
```
python -m unittest
```

## Usage
After creating the binary, it requires a `sample_license` file.
- Index Directory
    ```
    binary-exec index-directory <directory-path>
    ```