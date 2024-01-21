#L=[a1,a2,...,an], write an O(n^2)
#return(ai,aj,ak)
#ai+aj+ak = 0
#ai != aj != ak
#3 <= n <= 3000 means len(L) more than 3 less than 3000
#-10^6 <= ai <= 10^6, for all 1 <= i <= n.

import numpy as np

def sumToZero(A, low, high):
    min = A[low]
    max = A[high]
    result = []
    for j in range(low, high+1):
      if A[j]+max+min == 0 and A[j] != max and A[j] != min and max != min:
        result.append(A[j])
        result.append(max)
        result.append(min)
        return result
      else:
        for k in range(low,high+1):
          min = A[k]
          if A[j]+max+min == 0 and A[j] != max and A[j] != min and max != min:
            result.append(A[j])
            result.append(max)
            result.append(min)
            return result
        for m in range(low,high+1):
          max = A[m]
          if A[j]+max+min == 0 and A[j] != max and A[j] != min and max != min:
            result.append(A[j])
            result.append(max)
            result.append(min)
            return result
            
A = np.random.randint(low=-1000000, high=1000000, size=(3000)).tolist()
#A = [-200, -1,2,3,600,-4,-2] #edge case
IndexLow = 0
IndexHigh = len(A) - 1
result = sumToZero(A, IndexLow, IndexHigh)
print(result)
