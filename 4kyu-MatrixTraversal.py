# https://www.codewars.com/kata/snail/python
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
import numpy as np
def snail(array):
    array = np.array(array)
    if len(array) == 0 or len(array[0]) == 0: # [[]] or []
      return []
    n = len (array[0])-1
    res1,res2,res3,res4 = [],[],[],[]
    if n == 0:  # [[i]]
      return [array[0][0]]
    for i in range(n):
      res1.append(array[0,i])
      res2.append(array[i,n])
      res3.append(array[n,n-i])
      res4.append(array[n-i,0])
    return res1+res2+res3+res4+snail(array[1:n,1:n])

    
