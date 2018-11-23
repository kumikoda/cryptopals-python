def single_byte_xor(bytes_in, byte):
    bytes_out = []
    for i in range(0, len(bytes_in)):
        bytes_out.append(bytes_in[i] ^ byte)
    return bytes(bytes_out)


def get_letter_counts(s):
    counts = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        ' ': 0,
    }
    for c in s:
        if c in counts:
            counts[c] += 1
    return counts


def get_frequency_order(letter_counts):
    sorted_counts = sorted(
        letter_counts.items(), key=lambda kv: kv[1], reverse=True)
    return "".join(s[0] for s in sorted_counts)


def matches(str1, str2):
    count = 0
    for c in str1:
        if c in str2:
            count += 1
    return count


def special_penalty(str):
    str = str.lower()
    english_chars = " etaoinshrdlcumwfgypbvkjxqz"
    special_chars = []
    for c in str:
        if c not in english_chars:
            if c not in special_chars:
                special_chars.append(c)
    return len(special_chars)


def score_frequency(str):
    str = str.lower()
    standard_frequency_order = " etaoinshrdlcumwfgypbvkjxqz"
    letter_counts = get_letter_counts(str)
    frequency_order = get_frequency_order(letter_counts)
    top_matches = matches(standard_frequency_order[:7], frequency_order[:7])
    bot_matches = matches(standard_frequency_order[-6:], frequency_order[-6:])
    score = top_matches + bot_matches
    return score


def break_single_xor_cipher(hex_str):
    candidates = []
    for b in range(0, 127):
        xored = single_byte_xor(hex_str, b)
        xored_string = xored.decode("utf-8")
        f_score = score_frequency(xored_string)
        penalty = special_penalty(xored_string)
        score = f_score - 1.5 * penalty
        candidates.append((score, xored_string, chr(b)))

    sorted_candidates = sorted(candidates, key=lambda x: x[0], reverse=True)
    best_score, best_string, best_key = sorted_candidates[0]
    return best_key, best_string


def test_problem3():
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    bs = bytes.fromhex(hex_string)
    key, best_string = break_single_xor_cipher(bs)
    assert best_string == "Cooking MC's like a pound of bacon"
