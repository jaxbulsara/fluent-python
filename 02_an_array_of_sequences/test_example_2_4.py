colors = ["black", "white"]
sizes = ["S", "M", "L"]


def test_cartesian_product_by_colors():
    tshirts = [(color, size) for color in colors for size in sizes]

    assert tshirts == [
        ("black", "S"),
        ("black", "M"),
        ("black", "L"),
        ("white", "S"),
        ("white", "M"),
        ("white", "L"),
    ]


def test_cartesian_product_by_size():
    tshirts = [(color, size) for size in sizes for color in colors]

    assert tshirts == [
        ("black", "S"),
        ("white", "S"),
        ("black", "M"),
        ("white", "M"),
        ("black", "L"),
        ("white", "L"),
    ]


def test_cartesian_product_for_loop():
    tshirts = list()
    for color in colors:
        for size in sizes:
            tshirts.append((color, size))

    assert tshirts == [
        ("black", "S"),
        ("black", "M"),
        ("black", "L"),
        ("white", "S"),
        ("white", "M"),
        ("white", "L"),
    ]
