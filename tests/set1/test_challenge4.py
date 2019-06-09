from typing import List
from os import path
from crypto.xor import break_single_byte_xor


def find_encrypted(hex_strs: List[str]) -> str:
    max_score = 0
    best_answer = None
    for s in hex_strs:
        bs = bytes.fromhex(s)
        score, key, answer = break_single_byte_xor(bs)
        if score > max_score:
            max_score = score
            best_answer = answer
    return best_answer


def test_s1c4():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "challenge4.data")
    with open(data_file) as f:
        lines = f.read().splitlines()
    best_string = find_encrypted(lines)
    assert best_string == "Now that the party is jumping\n"
