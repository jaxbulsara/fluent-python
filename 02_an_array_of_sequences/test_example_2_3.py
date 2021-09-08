symbols = "$¢£¥€¤"

# The listcomp is much easier to comprehend than the filter/map combination.
# This is because it reads like a sentence and says exactly what it does.

result = [162, 163, 165, 8364, 164]


def test_beyond_ascii_listcomp():
    # Very readable
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

    assert beyond_ascii == result


def test_beyond_ascii_filter_map():
    # Not very readable
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

    assert beyond_ascii == result
