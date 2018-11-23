from os import path
import base64

from test_problem3 import break_single_xor_cipher, score_frequency
from test_problem5 import repeating_key_xor_bytes


def hamming_distance(s1, s2):
    b1 = bytes(s1, "utf-8")
    b2 = bytes(s2, "utf-8")
    return bit_distance(b1, b2)


def bit_distance(b1, b2):
    assert len(b1) == len(b2)
    distance = 0
    for i in range(0, len(b1)):
        for j in range(0, len(b1)):
            bit1 = (b1[i] >> j) % 2
            bit2 = (b2[i] >> j) % 2
            if bit1 != bit2:
                distance += 1
    return distance


def test_hamming():
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    assert hamming_distance(s1, s2) == 37


def transpose(bs, key_size):
    transposed = [[] for x in range(0, key_size)]
    for i in range(0, len(bs)):
        transposed[i % key_size].append(bs[i])
    return transposed


def average_bit_distance(bs, x):
    s1 = bs[:1 * x]
    s2 = bs[1 * x:2 * x]
    s3 = bs[2 * x:3 * x]
    s4 = bs[3 * x:4 * x]
    score = 0
    for i in [s1, s2, s3, s4]:
        for j in [s1, s2, s3, s4]:
            if i != j:
                score += bit_distance(i, j)
    return score / x


def normalized_bit_distance(bs, x):
    s1 = bs[:1 * x]
    s2 = bs[1 * x:2 * x]
    return bit_distance(s1, s2) / x


def guess_key_sizes(bs):
    key_sizes = {}
    for x in range(2, 40):
        try:
            score = average_bit_distance(bs, x)
            key_sizes[x] = score
        except:
            pass
    return sorted(key_sizes.items(), key=lambda kv: kv[1])


def break_repeating_key_xor(bs):
    candidates = []
    key_sizes = guess_key_sizes(bs)
    for key_size, _score in key_sizes[:10]:
        try:
            score, answer, key = break_repeating_key_xor_with_key_size(
                bs, key_size)
            candidates.append((score, answer, key))
        except:
            pass
    sorted_candidates = sorted(
        candidates, key=lambda x: (x[0], -1 * len(x[2])), reverse=True)
    best_score, best_answer, best_key = sorted_candidates[0]
    return best_answer, best_key


def break_repeating_key_xor_with_key_size(bs, key_size):
    transposed = transpose(bs, key_size)
    keys = []
    for shard in transposed:
        shard_key, best_string = break_single_xor_cipher(shard)
        keys.append(shard_key)
    key = bytes("".join(keys), "utf-8")
    answer = repeating_key_xor_bytes(bs, key).decode("utf-8")
    score = score_frequency(answer)
    return score, answer, key.decode("utf-8")


def test_transpose():
    numbers = [i for i in range(1, 10)]
    transposed = transpose(numbers, 3)
    assert transposed == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_break_without_key_size():
    examples = [
        ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f",
         "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
         "ICE"),
        ("0c2d263b3a353d632469213027202d692c236930313c2523693636202d22693a2a3c31653b26352c2231202d2264282030631d0611652f362b2a372c262d6b69062b2a313c393765302c303b6328282a29676300272037303331693a2a3c31653922363a342a3b27652f2a292c6d65102c303b636b3a2a2269252c25266b6904203d63246925202c2f652f2c37692a3167630c693337262e2c3a26696934206922372c2d623d6332283031202d22693a2a3c31653d2a282c633220372d69372d20306b",
         "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.",
         "ICE"),
        ("073b313c303e336234722c3c20242a753d28693d333733346e3c3d2e2c327237263b356227373e2c2f332b3b3563222b3e620d1d1c6928322c36262726206962103c2d3b373736752b213c3c672f343b22676e022c362037393a673b3a273c693e26312625213b2a67243c3e2b676e1e2d20206e673d2e25753427252b696212373a692f672430372269282830753b3a676e0e62252021242734277972392c6e2630303c693d6e30232626272729673b3a273c693a2e2f307239203a2f62213a273a60",
         "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.",
         "BURNING")
    ]
    for encrypted, original, key_used in examples:
        bs = bytes.fromhex(encrypted)
        answer, key = break_repeating_key_xor(bs)
        assert key == key_used
        assert answer == original


def test_break_given_key_size():
    examples = [
        ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f",
         "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
         "ICE"),
        ("0c2d263b3a353d632469213027202d692c236930313c2523693636202d22693a2a3c31653b26352c2231202d2264282030631d0611652f362b2a372c262d6b69062b2a313c393765302c303b6328282a29676300272037303331693a2a3c31653922363a342a3b27652f2a292c6d65102c303b636b3a2a2269252c25266b6904203d63246925202c2f652f2c37692a3167630c693337262e2c3a26696934206922372c2d623d6332283031202d22693a2a3c31653d2a282c633220372d69372d20306b",
         "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.",
         "ICE"),
        ("073b313c303e336234722c3c20242a753d28693d333733346e3c3d2e2c327237263b356227373e2c2f332b3b3563222b3e620d1d1c6928322c36262726206962103c2d3b373736752b213c3c672f343b22676e022c362037393a673b3a273c693e26312625213b2a67243c3e2b676e1e2d20206e673d2e25753427252b696212373a692f672430372269282830753b3a676e0e62252021242734277972392c6e2630303c693d6e30232626272729673b3a273c693a2e2f307239203a2f62213a273a60",
         "Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.",
         "BURNING")
    ]
    for encrypted, original, key_used in examples:
        bs = bytes.fromhex(encrypted)
        score, answer, key = break_repeating_key_xor_with_key_size(
            bs, len(key_used))
        assert key == key_used
        assert answer == original


def test_problem6_data():
    basepath = path.dirname(__file__)
    data_file = path.join(basepath, "problem6.data")
    with open(data_file) as f:
        data = base64.b64decode(f.read())
    answer, key = break_repeating_key_xor(data)

    answer_file = path.join(basepath, "problem6.expected_output")
    with open(answer_file) as f:
        expected_answer = f.read()
    print(answer)
    assert answer.split() == expected_answer.split()
    assert key == "Terminator X: Bring the noise"
