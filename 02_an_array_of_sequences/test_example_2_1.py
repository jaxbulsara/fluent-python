symbols = "$¢£¥€¤"


def test_codes_for_loop():
    # codes here is made with a longhand for loop
    # though readable, it is less explicit than a listcomp
    # there is always the possibility that it might be doing something else
    codes = list()
    for symbol in symbols:
        codes.append(ord(symbol))

    assert codes == [36, 162, 163, 165, 8364, 164]
