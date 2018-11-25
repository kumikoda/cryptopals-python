from crypto.xor import break_single_byte_xor


def test_s1c3():
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    bs = bytes.fromhex(hex_string)
    score, key, decoded_string = break_single_byte_xor(bs)
    assert decoded_string == "Cooking MC's like a pound of bacon"
