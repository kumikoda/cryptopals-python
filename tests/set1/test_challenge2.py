from crypto.xor import fixed_xor


def test_s1c2():
    b1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b2 = bytes.fromhex("686974207468652062756c6c277320657965")
    b = fixed_xor(b1, b2)
    assert b.hex() == "746865206b696420646f6e277420706c6179"
