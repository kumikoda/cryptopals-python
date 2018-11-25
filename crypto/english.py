def score_by_weight(s: str) -> float:
    freqs = {
        ' ': 15,
        'e': 12.70,
        't': 9.06,
        'a': 8.17,
        'o': 7.51,
        'i': 6.97,
        'n': 6.75,
        's': 6.33,
        'h': 6.09,
        'r': 5.99,
        'd': 4.25,
        'l': 4.03,
        'c': 2.78,
        'u': 2.76,
        'm': 2.41,
        'w': 2.36,
        'f': 2.23,
        'g': 2.02,
        'y': 1.97,
        'p': 1.93,
        'b': 1.29,
        'v': 0.98,
        'k': 0.77,
        'j': 0.15,
        'x': 0.15,
        'q': 0.10,
        'z': 0.07
    }
    score = 0
    for c in s.lower():
        score += freqs.get(c, 0)
    return score / len(s) / 15


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


def matches(s1, s2):
    count = 0
    for c in s1:
        if c in s2:
            count += 1
    return count


def score_by_order(str):
    str = str.lower()
    standard_frequency_order = " etaoinshrdlcumwfgypbvkjxqz"
    letter_counts = get_letter_counts(str)
    frequency_order = get_frequency_order(letter_counts)
    top_matches = matches(standard_frequency_order[:7], frequency_order[:7])
    bot_matches = matches(standard_frequency_order[-6:], frequency_order[-6:])
    score = top_matches + bot_matches
    return score / 13


def score_blended(s):
    order_score = score_by_order(s)
    weight_score = score_by_weight(s)
    return order_score + weight_score
