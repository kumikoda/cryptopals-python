from os import path
from single_byte_xor import single_byte_xor, score_frequency


def find_encrypted(hex_strs):
    max_score = 0
    best_string = None
    for s in hex_strs:
        for x in range(0, 127):
            try:
                xored = single_byte_xor(s, x)
            except:
                continue
            score = score_frequency(xored)
            if score > max_score:
                max_score = score
                best_string = xored
    return best_string


def test_4():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "problem4.data")
    with open(data_file) as f:
        lines = f.read().splitlines()
    best = find_encrypted(lines)
    assert best == "Now that the party is jumping\n"
