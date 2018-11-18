from os import path


def repeating_key_xor(string, key):
    str_bytes = bytes(string, "utf-8")
    key_bytes = bytes(key, "utf-8")
    out_bytes = []
    for i in range(0, len(str_bytes)):
        out_bytes.append(str_bytes[i] ^ key_bytes[i % 3])
    return bytes(out_bytes).hex()


def test():
    phrase = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    xored = repeating_key_xor(phrase, key)
    # what_i_expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\na282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    assert xored == expected


def test_other():
    phrase = "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this."
    repeating_key_xor(phrase, "ICE")
    # 0c2d263b3a353d632469213027202d692c236930313c2523693636202d22693a2a3c31653b26352c2231202d2264282030631d0611652f362b2a372c262d6b69062b2a313c393765302c303b6328282a29676300272037303331693a2a3c31653922363a342a3b27652f2a292c6d65102c303b636b3a2a2269252c25266b6904203d63246925202c2f652f2c37692a3167630c693337262e2c3a26696934206922372c2d623d6332283031202d22693a2a3c31653d2a282c633220372d69372d20306b
    repeating_key_xor(phrase, "BURNING")
    # 073b31302c223675336237272c363a623a346226263733346220212b3b35622c3d3727723030222734262b3b356f3e373b750a0d077224203c21213b2d3b7c62103c21272b3221723b3a2730753f233c3e6c75172c36203b2526622c3d37277232342131223d303172243c3e277b721b3a2730757c313c3562333b2e307c621237367533623337273972243a20623c266c751b6225202d383b31307e622237623420273b753675252326262b3b35622c3d372772363c3f2775252b213a62213a2b267c


def test_data():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "problem4.data")
    with open(data_file) as f:
        out = repeating_key_xor(f.read(), "ICE")
    output_filepath = path.join(basepath, "problem5.output")
    f = open(output_filepath, "w+")
    f.write(out)
    f.close()
