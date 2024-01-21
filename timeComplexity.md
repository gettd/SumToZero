### Analysis on 'sumToZero()'

```python
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
```
Let the first three variable declaration be c1, c2 and c3(constant time)
Ignoring all constant time to proof that T(n) = O(n^2)
The "for j in range" loop will use n time
The "for k in range" and "for m in range" in "else" condition will use n time each
So else condition will use n+n = 2n time
The loop with else condition will use a total of T(n) = 2n^2 ; n>=1
This conclude that sumToZero function use time complexity of O(n^2)
