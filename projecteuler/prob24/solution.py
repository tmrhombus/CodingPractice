
import itertools

def solution(permnr):
 
 arr = list(range(10))
 temp = itertools.islice(itertools.permutations(arr), permnr-1, None)
 #print(next(temp))
 thenum = "".join(str(x) for x in next(temp))

 return thenum	
