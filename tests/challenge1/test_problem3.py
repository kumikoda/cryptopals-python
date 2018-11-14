from single_byte_xor import single_byte_xor, score_frequency


def break_cipher(hex_str):
    max_score = 0
    best_string = None
    for x in range(0, 127):
        xored = single_byte_xor(hex_str, x)
        score = score_frequency(xored)
        if score > max_score:
            max_score = score
            best_string = xored
    return best_string


def test3():
    h = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    best_string = break_cipher(h)
    assert best_string == "Cooking MC's like a pound of bacon"
