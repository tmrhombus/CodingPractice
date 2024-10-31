from typing import List
from collections import Counter
import collections

class Solution:
 def evalRPN(self, tokens: List[str]) -> int:

  stack = []

  for i in tokens:
   print(f"stack: {stack}, i: {i}")
   if i=="+":
    v1,v2 = stack.pop(), stack.pop()
    stack.append( v1 + v2 )
    print(f" {v2} + {v1}, new stack: {stack}")

   elif i=="-":
    v1,v2 = stack.pop(), stack.pop()
    stack.append( v2 - v1 )
    print(f" {v2} - {v1}, new stack: {stack}")

   elif i=="*":
    v1,v2 = stack.pop(), stack.pop()
    stack.append( v1 * v2 )
    print(f" {v2} * {v1}, new stack: {stack}")

   elif i=="/":
    v1,v2 = stack.pop(), stack.pop()

    ## integer division should truncate towards 0
    if v1*v2 > 0:
     stack.append( v2 // v1 )
    else:
     stack.append( - int( (-v2) // v1 ) )
    print(f" {v2} // {v1}, new stack: {stack}")

   else:
    stack.append(int(i))

  return stack[0]
