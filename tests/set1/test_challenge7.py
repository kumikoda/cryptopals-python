# using openssl https://wiki.openssl.org/index.php/Enc
# openssl enc -aes-128-ecb -a -d -in tests/set1/challenge7.data -K 59454c4c4f57205355424d4152494e45

from os import path
from crypto.aes import aes_ecb_128
import base64


def strip(s):
    return s.replace('\x04', '')


def test_s1c7():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "challenge7.data")
    output_file = path.join(basepath, "challenge7.expected_output")

    with open(data_file) as f:
        data = base64.b64decode(f.read())

    decrypted = aes_ecb_128(bs=data, key="YELLOW SUBMARINE")

    with open(output_file) as f:
        expected_output = f.read()

    assert strip(decrypted.decode()) == expected_output
