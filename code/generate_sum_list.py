"""
J. Chanenson
June 21, 2021
This file contains one helper function that generates a list of n elements which sum to m. n and m are set by the user.
"""
import numpy as np

def main():
  while True:
    try:
      eleNum = int(input("Enter the number of elements you want in the list: "))
    except:
      print("Incorrect Input. Next time, please enter an integer")
      continue
    
    try:
      sumNum = int(input("Enter the desired sum of the list: "))
    except:
      print("Incorrect Input. Next time, please enter an integer")
      continue
    
    try:
      iterNum = abs(int(input("How many lists do you want: ")))
      break #leave while loop
    except:
      print("Incorrect Input. Next time, please enter an integer")
      continue 

  for i in range(iterNum):
    b = randLst(eleNum, sumNum)
    print(b)

def randLst(eleNum, sumNum=100):
  """
  @params:
    -eleNum: How many elements in the ret list
    -sumNum: what number all of the elements should sum to
  @ret: the list that sums to numNum
  """
  a = np.random.random(eleNum) #generate array
  a /= a.sum() #norm array
  b = np.round_(a, decimals=2) * sumNum
  correction = sumNum-b.sum()

  if correction < 0: #correction is neg, add to largest element
    idx = np.argmax(b)
  else: #correction is pos, add to smallest element
    idx = np.argmin(b)
  b[idx]+=correction
  
  return b

if __name__ == "__main__":
  main()