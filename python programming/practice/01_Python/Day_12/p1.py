# frozenset areimmutable sets, they cannot be changed after they are created
# they are created using the frozenset() function

fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

print(fs1|fs2)

# write operations don't work on frozenset

# 2D frozensets

fs = frozenset([frozenset([1,2]), frozenset([3,4])])
print(fs)

