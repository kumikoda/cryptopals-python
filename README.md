# Cryptopals Python

https://cryptopals.com/

## Setup

- `python3 -m pip install --user virtualenv` to install virtualenv.
- `python3 -m virtualenv env` to create a local virtualenv in a folder called `env`.
- `source env/bin/activate` activate the local virtualenv. all dependencies installed will now be installed in the virtual env instead of the global env.
- `deactivate` to exit the local virtual env.

## Dependencies

- `pip3 install requirements.txt` to install dependencies
- `pip3 freeze > requirements.txt` to save newly installed dependencies

## Run tests

- `pip3 install -e .` to install the crypto package itself for tests
- `pytest` to run all tests
- `pytest -k name_of_test_file` to run all tests in a file
- `pytest -k name_of test` to run a single test
