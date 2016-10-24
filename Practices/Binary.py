import binascii

a = "test"
a_bytes = bytes(a, "ascii")
print(' '.join(["{0:b}".format(x) for x in a_bytes]))