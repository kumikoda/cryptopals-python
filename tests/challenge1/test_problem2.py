def fixed_xor(hex_str1, hex_str2):
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)
    bytes_out = []
    for i in range(0, len(bytes1)):
        bytes_out.append(bytes1[i] ^ bytes2[i])
    return bytes(bytes_out).hex()


def test():
    h1 = "1c0111001f010100061a024b53535009181c"
    h2 = "686974207468652062756c6c277320657965"
    h3 = fixed_xor(h1, h2)
    assert h3 == "746865206b696420646f6e277420706c6179"
