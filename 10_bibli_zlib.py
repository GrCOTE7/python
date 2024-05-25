import zlib

s = b"witch which has which witches wrist watch"
l=len(s)

t = zlib.compress(s)


a=len(t)

b=zlib.decompress(t)

c=zlib.crc32(s)

print(l, a,b,c)
