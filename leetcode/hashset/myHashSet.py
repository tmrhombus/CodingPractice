#!/bin/python

class checkingvalues:
   '''
   Helper class for HashSet class
   
   These are the entries in the hash table
   Each entry is itself an array (named klist) to 
    handle collisions of multiple values hashing 
    to the same klist
   Functions are defined to
    update: add a value to klist
    get: check if value is in klist
    remove: remove a value from klist
   '''
   #initialization function to define array klist
   def __init__(self):
      self.klist=[]
     
   #update vales function
   def update(self, key):
      '''
      Go through klist, looking for key
      If key is already in klist, do nothing
      If key isn't in klist, add it to the end
      '''
      found=False
      for i,k in enumerate(self.klist):
         if key==k:
            self.klist[i]=key
            found=True
            break
      if not found:
         self.klist.append(key)
    
   #get values function
   def get(self, key):
      '''
      return True if key in klist
             False if key isn't there
      '''
      for k in self.klist:
         if k==key:
            return True
      return False

   #remove values function
   def remove(self, key):
      '''
      if key is in klist, delete it
      '''
      for i,k in enumerate(self.klist):
         if key==k:
            del self.klist[i]
 
# The actual HashSet class
class HashSet:
   #Initialization function
   def __init__(self):
      '''
      Initialize hash_table as an array of length key_space 
       with an empty checkingvalues() at each entry of array
      '''
      self.key_space = 10 # how long the hash table is
      self.hash_table=[checkingvalues() for i in range(self.key_space)]

   # make hash_key from value you give it, just mod by length of h_t
   def hash_values(self, key):
       '''
       The hash_table only has key_space buckets, so use mod(key_space)
        on input key to determine which bucket it goes to
       Bucket number is the hash_key
       '''
       hash_key=key%self.key_space
       return hash_key

   #add function
   def add(self, key):
      ''' add key to hash_table in location key % key_space '''
      self.hash_table[self.hash_values(key)].update(key)

   #remove function
   def remove(self, key):
      ''' remove key from hash_table '''
      self.hash_table[self.hash_values(key)].remove(key)

   #contains function
   def contains(self, key): 
      ''' check if klist contains key '''
      return self.hash_table[self.hash_values(key)].get(key)

   def display(self):
      ''' print the full hash_table '''
      ls=[]
      for i in self.hash_table:
          if len(i.klist)!=0: ls.append(i.klist[0])
      print(ls)
  
    

### Checks

# make a new HashSet 
hs = HashSet()
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

hs.display()

#
#print(hs.hash_values(5))
#print("Add 5 ")
#hs.add(5)
#print(hs.hash_values(6))
#print("Add 6 ")
#hs.add(6)
#print(hs.hash_values(7))
#print("Add 7 ")
#hs.add(7)
#print("Contains 5 : ",hs.contains(5))
#print("Contains 7: ",hs.contains(7))
#print("Contains 10 : ",hs.contains(10))
#print(hs.hash_values(2))
#print("Add 2 ")
#hs.add(2)
#print(hs.hash_values(3))
#print("Add 3 ")
#hs.add(3)
#print("Contains 2 : ",hs.contains(2))
#print("Remove 2 ")
#hs.remove(2)
#print("Contains 2 : ",hs.contains(2))
#print("Contains 3 : ",hs.contains(3))
#hs.display()
