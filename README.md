# Sample Python Binary
This is a sample python binary which contains different implementations of common python tasks.

## Requirements (Development)
- Python 3.8+
- Nuitka
- Fire
- Fernet

## Compiling with Nuitka
### Accelerated Mode
- Execute the following to compile with [Nuitka](https://github.com/Nuitka/Nuitka):
    ```
    env/bin/python -m nuitka binary.py
    ```

### For Distribution (One File)
- Run the build script `build.sh`
    ```
    bash build.sh
    ```
    Modify the `build.sh` if you encounter any issues on your dependencies.

## License File
The license file which is the `data_dir/sample_license` contains an encrypted `LICENSE_EXPIRY`. This uses a binary string under the `modules/settings.py` to decrypt the contents of the license file. The encryption and decryption is done using the `cryptography` library. Refer to this [repo](https://github.com/lkpanganiban/license-generator-toolbox) on how to generate a license file.

## Running Test
```
python -m unittest
```

## Usage
After creating the binary, it requires a `sample_license` file. A sample is found under `data_dir/sample_license`.
- Index Directory
    ```
    binary-exec index-directory <directory-path>
    ```