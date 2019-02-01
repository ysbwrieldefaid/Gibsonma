# SRC - The indentation is all wrong here!
# Spend some time making this work.

def recursive_bsearch(test, first, last, guess): 
  middle = (first+last) // 2 
  if test[middle] == guess:
    return middle
   else:
  if guess > test[middle]
    first = middle + 1
   else:
    last = middle - 1 
   return recursive_bsearch(test, first, last, guess) 
   
  test = [3, 15, 25, 29, 36, 42, 53, 59, 74, 82, 96, 190] 
  position = - 1 
  first = 0
  last = len(test) - 1 
  
  guess = int(input("enter value to look for: "))
  posit = recursive_bsearch(test, first, last, guess) 
  print(posit) 
  
  
