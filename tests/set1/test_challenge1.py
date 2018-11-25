import base64


def hex_to_base64(data: str) -> str:
    hex_bytes = bytes.fromhex(data)
    b64_bytes = base64.b64encode(hex_bytes)
    return b64_bytes.decode("utf-8")


def test_s1c1():
    input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output_string = hex_to_base64(input_string)
    assert output_string == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
