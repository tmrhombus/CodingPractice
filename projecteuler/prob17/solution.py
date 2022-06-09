
def solution( top ):
 """
 returns the number of characters used to spell the
 numbers from one to <top> inclusive

 method:
 use lists to pick out the right word combo for a given number
 keep track of charactar count in parallel
 """

 tot = 0
 
 w_ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
 n_ones = [3,   3,   5,     4,    4,    3,   5,     5,     4  ]

 w_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", \
            "sixteen", "seventeen", "eighteen", "nineteen"]
 n_teens = [ 3,     6,        6,        8,          8,          7, \
             7,         9,           8,          8]

 w_tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
 n_tens = [ 6,        6,        6,        5,       5,       7,         6,        6] 

 for i in range(1,top+1):

  word = ""
  num = 0

  thous = i // 1000
  hunds = (i % 1000) // 100
  tens = (i % 100) // 10
  units = (i % 10)

  print(" {} :  {}  {}  {}  {}   ".format(i,thous,hunds,tens,units)), 

  if(thous):
   word = word + w_ones[thous-1] + " thousand"
   num  = num  + n_ones[thous-1] + 8

  if(hunds):
   word = word + " " + w_ones[hunds-1] + " hundred"
   num  = num  +       n_ones[hunds-1] + 7

  

  # # i from 1 - 10
  # if(0<i<10):
  print(" {}".format(word))
  print(" {}".format(num))
   
 


  #print(" {}: {}: {}".format( i, word, num)) 

  
 return tot

