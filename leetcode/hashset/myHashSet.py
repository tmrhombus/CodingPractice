#Design HashSet in python
#checking the values and will return the output class

# These are the values in the hash table
class checkingvalues:
   #initialization function which has list mathfun
   def __init__(self):
      self.mathfun=[]
     
   #update vales function
   def update(self, key):
      found=False
      for i,k in enumerate(self.mathfun):
         if key==k:
            self.mathfun[i]=key
            found=True
            break
      if not found:
         self.mathfun.append(key)
    
   #get values function
   def get(self, key):
      for k in self.mathfun:
         if k==key:
            return True
      return False

   #remove values function
   def remove(self, key):
      for i,k in enumerate(self.mathfun):
         if key==k:
            del self.mathfun[i]
 
#class HashSet main class
class HashSet:
   #Initialization function
   def __init__(self):
      self.key_space = 2096 # how long the hash table is
      # h_t is an array of length key_space, initialized with
      # that many checkingvalues objects
      self.hash_table=[checkingvalues() for i in range(self.key_space)]

   # make hash_key from value you give it, just mod by length of h_t
   def hash_values(self, key):
       hash_key=key%self.key_space
       return hash_key

   #add function
   def add(self, key):
      self.hash_table[self.hash_values(key)].update(key)

   #remove function
   def remove(self, key):
      self.hash_table[self.hash_values(key)].remove(key)

   #contains function
   def contains(self, key): 
      return self.hash_table[self.hash_values(key)].get(key)

   def display(self):
       ls=[]
       for i in self.hash_table:
           if len(i.mathfun)!=0:ls.append(i.mathfun[0])
       print(ls)
  
    
print(" {}".format( checkingvalues() ))
hash_table=[checkingvalues() for i in range(10)]
print(" {}".format( hash_table ) )

        
ob = HashSet()
print(ob.hash_values(5))
print("Add 5 ")
ob.add(5)
print(ob.hash_values(6))
print("Add 6 ")
ob.add(6)
print(ob.hash_values(7))
print("Add 7 ")
ob.add(7)
print("Contains 5 : ",ob.contains(5))
print("Contains 7: ",ob.contains(7))
print("Contains 10 : ",ob.contains(10))
print(ob.hash_values(2))
print("Add 2 ")
ob.add(2)
print(ob.hash_values(3))
print("Add 3 ")
ob.add(3)
print("Contains 2 : ",ob.contains(2))
print("Remove 2 ")
ob.remove(2)
print("Contains 2 : ",ob.contains(2))
print("Contains 3 : ",ob.contains(3))
ob.display()
