symbols = "$¢£¥€¤"


def test_codes_listcomp():
    # This listcomp is much easier to read than the for loop in example 2.1.
    # Listcomps are easier to read because they read like sentences and say
    # exactly what they do.
    codes = [ord(symbol) for symbol in symbols]
    assert codes == [36, 162, 163, 165, 8364, 164]
