def single_byte_xor(hex_str, byte):
    hex_bytes = bytes.fromhex(hex_str)
    bytes_out = []
    for i in range(0, len(hex_bytes)):
        bytes_out.append(hex_bytes[i] ^ byte)
    return bytes(bytes_out).decode("utf-8")


def get_letter_counts(string):
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
        ' ': 0
    }
    for c in string.lower():
        if c in counts:
            counts[c] += 1
    return counts


def get_frequency_order(letter_counts):
    sorted_counts = sorted(
        letter_counts.items(), key=lambda kv: kv[1], reverse=True)
    return "".join(s[0] for s in sorted_counts)


def matches(str1, str2):
    matches = 0
    max_pos = 0
    for c in str1:
        pos = str2.find(c)
        if pos >= max_pos:
            max_pos = pos
            matches += 1
    return matches


def score_frequency(string):
    standard_frequency_order = " etaoinshrdlcumwfgypbvkjxqz"
    letter_counts = get_letter_counts(string)
    frequency_order = get_frequency_order(letter_counts)
    top_matches = matches(standard_frequency_order[:6], frequency_order[:6])
    bot_matches = matches(standard_frequency_order[-6:], frequency_order[-6:])
    return top_matches + bot_matches
