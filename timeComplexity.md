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
