# https://www.codewars.com/kata/snail/python
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]

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

print (snail(array))

"""
output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
"""
