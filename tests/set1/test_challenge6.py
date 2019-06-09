from os import path
import base64

from crypto.xor import transpose, repeating_key_xor, break_repeating_key_xor


def test_transpose():
    numbers = [i for i in range(1, 10)]
    transposed = transpose(numbers, 3)
    assert transposed == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_break_repeating_key_xor():
    phrase = "It is better to be feared than loved, if you cannot be both."
    bs = bytes(phrase, "utf-8")
    real_key = bytes("foobar", "utf-8")
    encrypted = repeating_key_xor(bs, real_key)
    score, key, answer = break_repeating_key_xor(encrypted)
    assert answer == phrase
    assert key == real_key


def test_s1c6():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "challenge6.data")
    with open(data_file) as f:
        data = base64.b64decode(f.read())
    score, key, answer = break_repeating_key_xor(data)

    answer_file = path.join(basepath, "challenge6.expected_output")
    with open(answer_file) as f:
        expected_answer = f.read()
    assert answer.split() == expected_answer.split()
    assert key == bytes("Terminator X: Bring the noise", "utf-8")
