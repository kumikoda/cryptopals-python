from os import path


def repeating_key_xor_string(string, key):
    str_bytes = bytes(string, "utf-8")
    key_bytes = bytes(key, "utf-8")
    return repeating_key_xor_bytes(str_bytes, key_bytes).hex()


def repeating_key_xor_bytes(str_bytes, key_bytes):
    out_bytes = []
    for i in range(0, len(str_bytes)):
        out_bytes.append(str_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return bytes(out_bytes)


def test():
    phrase = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    xored = repeating_key_xor_string(phrase, key)
    # what_i_expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\na282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    assert xored == expected


def test_other_phrase():
    phrase = "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this."
    out1 = repeating_key_xor_string(phrase, "ICE")
    expected1 = "0c2d263b3a353d632469213027202d692c236930313c2523693636202d22693a2a3c31653b26352c2231202d2264282030631d0611652f362b2a372c262d6b69062b2a313c393765302c303b6328282a29676300272037303331693a2a3c31653922363a342a3b27652f2a292c6d65102c303b636b3a2a2269252c25266b6904203d63246925202c2f652f2c37692a3167630c693337262e2c3a26696934206922372c2d623d6332283031202d22693a2a3c31653d2a282c633220372d69372d20306b"
    assert out1 == expected1
    out2 = repeating_key_xor_string(phrase, "BURNING")
    expected2 = "073b313c303e336234722c3c20242a753d28693d333733346e3c3d2e2c327237263b356227373e2c2f332b3b3563222b3e620d1d1c6928322c36262726206962103c2d3b373736752b213c3c672f343b22676e022c362037393a673b3a273c693e26312625213b2a67243c3e2b676e1e2d20206e673d2e25753427252b696212373a692f672430372269282830753b3a676e0e62252021242734277972392c6e2630303c693d6e30232626272729673b3a273c693a2e2f307239203a2f62213a273a60"
    assert out2 == expected2


def test_data():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "problem4.data")
    with open(data_file) as f:
        out = repeating_key_xor_string(f.read(), "ICE")
    output_filepath = path.join(basepath, "problem5.output")
    f = open(output_filepath, "w+")
    f.write(out)
    f.close()
