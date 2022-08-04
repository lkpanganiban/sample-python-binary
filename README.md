# Sample Python Binary
This is a sample python binary which contains different implementations of common python tasks.

## Requirements (Development)
- Python 3.8+
- Nuitka
- Fire
- Cryptography

## Developers
### Models and Other Configs
ML model files can be placed inside the `data_dir` directory. This folder can also be used as a container for other static binaries that you need to use in your code. 
### Settings File
The `settings.py` is located under `sample_python_binary/modules/`. You can configure the parameters and constants inside this file but it is recommended to use the environment variables to configure or modify this file instead of hardcoding the values.

### Running Tests
```
python -m unittest
```

### Compiling
#### Accelerated Mode
- Execute the following to compile with [Nuitka](https://github.com/Nuitka/Nuitka):
    ```
    env/bin/python -m nuitka binary.py # if you're using a virtual environment
    ```
#### For Distribution
##### Standalone packaged with Docker
- Run the build script `build.sh` The generated standalone dist folder also works with Docker
    ```
    docker build -t sample_python_binary .
    ```
##### Onefile Binary
- Run the following command to build with Onefile.
    ```
    bash build.sh
    ```
    Modify the `build.sh` if you encounter any issues on your dependencies.


## Usage
### Parameters
You can set the environment variables of the following parameters:
- DEBUG: True or False
- DB_Name: Name of output Database
- LICENSE_FILE: Location of the license file

### License File
The license file which is the `data_dir/sample_license` contains an encrypted `LICENSE_EXPIRY`. This uses a binary string under the `modules/settings.py` to decrypt the contents of the license file. The encryption and decryption is done using the `cryptography` library. Refer to this [repo](https://github.com/lkpanganiban/license-generator-toolbox) on how to generate a license file.

### CLI Usage
After creating the binary, it requires a `sample_license` file. A sample is found under `data_dir/sample_license`.
- Index Directory
    ```
    binary-exec index-directory <directory-path>
    ```