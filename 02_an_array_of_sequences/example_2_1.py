symbols = "$¢£¥€¤"
codes = list()
for symbol in symbols:
    codes.append(ord(symbol))

# codes here is made with a longhand for loop
# though readable, it is less explicit than a listcomp
# there is always the possibility that it might be doing something else
