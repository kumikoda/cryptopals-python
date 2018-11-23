from os import path
from test_problem3 import single_byte_xor, score_frequency


def find_encrypted(hex_strs):
    max_score = 0
    best_string = None
    for s in hex_strs:
        for x in range(0, 127):
            bs = bytes.fromhex(s)
            xored = single_byte_xor(bs, x)
            try:
                xored_string = xored.decode("utf-8")
            except:
                continue
            score = score_frequency(xored_string)
            if score > max_score:
                max_score = score
                best_string = xored_string
    return best_string


def test_problem4():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "problem4.data")
    with open(data_file) as f:
        lines = f.read().splitlines()
    best = find_encrypted(lines)
    assert best == "Now that the party is jumping\n"
