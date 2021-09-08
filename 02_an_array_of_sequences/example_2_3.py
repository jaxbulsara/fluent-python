symbols = "$¢£¥€¤"

# The listcomp is much easier to comprehend than the filter/map combination.
# This is because it reads like a sentence and says exactly what it does.
beyond_ascii_listcomp = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii_filter_map = list(filter(lambda c: c > 127, map(ord, symbols)))
