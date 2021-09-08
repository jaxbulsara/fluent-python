from example_2_3 import beyond_ascii_listcomp, beyond_ascii_filter_map


def test_beyond_ascii():
    beyond_ascii = [162, 163, 165, 8364, 164]

    assert beyond_ascii_listcomp == beyond_ascii
    assert beyond_ascii_filter_map == beyond_ascii
