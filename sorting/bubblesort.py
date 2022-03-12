

inputarray = [1,4,2,3,6,2]
print(inputarray)

lenarray = len(inputarray)

for itnr in range(lenarray):
 #print("Iteration: {}".format(itnr))

 for swaplook in range(lenarray-itnr-1):
  #print(" {}".format(swaplook))
  if (inputarray[swaplook] > inputarray[swaplook+1]):
   inputarray[swaplook], inputarray[swaplook+1] = inputarray[swaplook+1], inputarray[swaplook]

print(inputarray)


 
