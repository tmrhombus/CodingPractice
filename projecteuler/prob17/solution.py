
def solution( top ):
 """
 returns the number of characters used to spell the
 numbers from one to <top> inclusive

 method:
 use lists to pick out the right word combo for a given number
 keep track of charactar count in parallel
 """

 if(top > 9999):
  print("Choose a top number below 10,000")
  return(-1)

 tot = 0

 # weird Brittish convention to insert "and" 
 dobrit = True
 
 w_ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
 n_ones = [3,      3,    5,       4,      4,      3,     5,       5,       4  ]

 w_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", \
            "sixteen", "seventeen", "eighteen", "nineteen"]
 n_teens = [ 3,     6,        6,        8,          8,          7, \
             7,         9,           8,          8]


 w_lows = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", \
           "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", \
           "sixteen", "seventeen", "eighteen", "nineteen"]
 n_lows = [3,      3,    5,       4,      4,      3,     5,       5,       4, \
           3,     6,        6,        8,          8,          7, \
           7,         9,           8,          8]


 w_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
 n_tens = [ 6,        6,        5,       5,       5,       7,         6,        6] 

 for i in range(1,top+1):

  word = ""
  num = 0

  thous = i // 1000
  hunds = (i % 1000) // 100
  tens = (i % 100) // 10
  ones = (i % 10)

  #print(" {} :  {}  {}  {}  {}   ".format(i,thous,hunds,tens,ones)), 

  if(thous):
   #word = word + w_ones[thous-1] + " thousand"
   #num  = num  + n_ones[thous-1] + 8
   word = word + w_lows[thous-1] + " thousand"
   num  = num  + n_lows[thous-1] + 8

  if(hunds):
   #word = word + " " + w_ones[hunds-1] + " hundred"
   #num  = num  +       n_ones[hunds-1] + 7
   word = word + " " + w_lows[hunds-1] + " hundred"
   num  = num  +       n_lows[hunds-1] + 7

   if(dobrit and (tens or ones)):
    word = word + " and"
    num  = num  + 3

  if(tens > 1):
   word = word + " " + w_tens[tens-2]
   num  = num  +       n_tens[tens-2]
  
   if(ones):
    #word = word + " " + w_ones[ones-1]
    #num  = num  +       n_ones[ones-1]
    word = word + " " + w_lows[ones-1]
    num  = num  +       n_lows[ones-1]
  
  elif(tens or ones):
   #word = word + " " + w_ones[ones-1]
   #num  = num  +       n_ones[ones-1]
   word = word + " " + w_lows[10*tens+ones-1]
   num  = num  +       n_lows[10*tens+ones-1]


  tot = tot + num
  print(" {}: {}   {}".format( i, word, num ) )
  #print(" {}".format(word))
  #print("  {}".format(num))
  #print("  {}".format(tot))
  
 return tot

