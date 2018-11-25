def bit_distance(b1: bytes, b2: bytes) -> int:
    assert len(b1) == len(b2)
    distance = 0
    for i in range(0, len(b1)):
        for j in range(0, len(b1)):
            bit1 = (b1[i] >> j) % 2
            bit2 = (b2[i] >> j) % 2
            if bit1 != bit2:
                distance += 1
    return distance


def normalized_bit_distance(bs: bytes, x: int) -> float:
    s1 = bs[:1 * x]
    s2 = bs[1 * x:2 * x]
    return bit_distance(s1, s2) / x


def average_bit_distance(bs: bytes, x: int) -> float:
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
