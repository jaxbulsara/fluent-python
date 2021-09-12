symbols = "$¢£¥€¤"


def test_genexp_tuple():
    # if the generator expression is the only argument, then you don't need
    # to put additional parentheses around it.
    result = tuple(ord(symbol) for symbol in symbols)

    assert result == (36, 162, 163, 165, 8364, 164)


def test_genexp_array():
    import array

    # Since the generator expression is its own argument, parentheses are
    # placed around them
    result = array.array("I", (ord(symbol) for symbol in symbols))

    assert repr(result) == "array('I', [36, 162, 163, 165, 8364, 164])"
