import myHashSet as mhs

hs = mhs.HashSet()
print("Hash Values for {},{},{} are {},{},{}".format( \
 1, 5, 11, hs.hash_values(1), hs.hash_values(5), hs.hash_values(11) ))

print("Adding these values to hash_table")
hs.add(1)
hs.add(5)
hs.add(11)

print("Check if these values are in hash table")
print(" {} : {}".format(1,hs.contains(1)))
print(" {} : {}".format(5,hs.contains(5)))
print(" {} : {}".format(11,hs.contains(11)))
print(" {} : {}".format(16,hs.contains(16)))

print("Full hash table:")
hs.display()

print("Remove 11")
hs.remove(11)

print("Check if these values are in hash table")
print(" {} : {}".format(1,hs.contains(1)))
print(" {} : {}".format(5,hs.contains(5)))
print(" {} : {}".format(11,hs.contains(11)))
print(" {} : {}".format(16,hs.contains(16)))

print("Full hash table:")
hs.display()

