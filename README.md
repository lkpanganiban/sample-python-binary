# Sample Python Binary
How to package a Python program using Pyinstaller

## Requirements
- Python 3.8+
- Pyinstaller
- Fire

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
    python -m nuitka binary.py
    ```
2. More [info](https://github.com/Nuitka/Nuitka)
