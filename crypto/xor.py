from typing import Tuple, List
from crypto.english import score_blended
from crypto.hamming import average_bit_distance


def fixed_xor(bs1: bytes, bs2: bytes) -> bytes:
    bytes_out = []
    for i in range(0, len(bs1)):
        bytes_out.append(bs1[i] ^ bs2[i])
    return bytes(bytes_out)


def single_byte_xor(bs: bytes, b: int) -> bytes:
    assert b >= 0 and b < 128, "b must be between 0 and 127"

    bytes_out = []
    for i in range(0, len(bs)):
        bytes_out.append(bs[i] ^ b)
    return bytes(bytes_out)


def break_single_byte_xor(bs: bytes) -> Tuple[float, int, str]:
    best_score = 0
    best_key = None
    best_answer = None
    for b in range(0, 127):
        xored = single_byte_xor(bs, b)
        try:
            xored_string = xored.decode("utf-8")
        except:
            continue
        score = score_blended(xored_string)
        if score > best_score:
            best_score = score
            best_answer = xored_string
            best_key = b

    return best_score, best_key, best_answer


def repeating_key_xor(bs: bytes, key: bytes) -> bytes:
    out_bytes = []
    for i in range(0, len(bs)):
        out_bytes.append(bs[i] ^ key[i % len(key)])
    return bytes(out_bytes)


def transpose(bs: bytes, key_size: int) -> List[bytes]:
    shards = [[] for x in range(0, key_size)]
    for i in range(0, len(bs)):
        shards[i % key_size].append(bs[i])
    return shards


def guess_key(bs: bytes, key_size: int) -> Tuple[float, int, str]:
    keys = []
    for shard in transpose(bs, key_size):
        score, key, answer = break_single_byte_xor(shard)
        keys.append(key)
    return bytes(keys)


def guess_key_sizes(bs: bytes) -> List[Tuple[float, int]]:
    key_sizes = {}
    for x in range(2, 40):
        try:
            key_sizes[x] = average_bit_distance(bs, x)
        except:
            pass
    return sorted(key_sizes.items(), key=lambda kv: kv[1])


def break_repeating_key_xor(bs: bytes) -> Tuple[float, int, str]:
    best_score = 0
    best_key = None
    best_answer = None
    key_sizes = guess_key_sizes(bs)
    for key_size, distance in key_sizes[:len(key_sizes) // 3]:
        key = guess_key(bs, key_size)
        answer = repeating_key_xor(bs, key).decode("utf-8")
        score = score_blended(answer)
        if score > best_score:
            best_score = score
            best_answer = answer
            best_key = key
    return best_score, best_key, best_answer
