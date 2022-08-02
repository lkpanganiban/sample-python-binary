# Sample Python Binary
How to package a Python program using Pyinstaller

## Requirements (Development)
- Python 3.8+
- Pyinstaller
- Nuitka
- Fire
- Fernet

## Compiling with Pyinstaller
1. How to Compile: The `binary.py` act as the entrypoint for Pyinstaller.
    ```
    pyinstaller binary.spec # execute the spec file
    ```
2. How to include packages: In the generated `binary.spec` file and enter the location of the `site-packages` directory in the `pathex`.
3. If you need to include a binary files like ML models, add them to `datas`.

## Compiling with Nuitka
1. Execute the following to compile with Nuitka:
    ```
    env/bin/python -m nuitka binary.py
    ```
2. More [info](https://github.com/Nuitka/Nuitka)

## License File
The license file which is the `sample_license` contains the `LICENSE_EXPIRY` key. This uses a binary string under the `modules/settings.py` to decrypt the license file. The encryption and decryption is done using the `cryptography` library.  
