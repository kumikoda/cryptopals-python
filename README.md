# Cryptopals Python

https://cryptopals.com/

## Setup

- `python3 -m venv venv` to create a virtual env named `venv`.
- `source venv/bin/activate` activate the local virtualenv.
- `deactivate` to exit the local virtual env.

## Dependencies

- `pip3 install -r requirements.txt` to install dependencies
- `pip3 freeze > requirements.txt` to save newly installed dependencies

## Run tests

- `pip3 install -e .` to install the crypto package itself for tests
- `pytest` to run all tests
- `pytest -k name_of_test_file` to run all tests in a file
- `pytest -k name_of_test` to run a single test
