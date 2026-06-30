def mysum(x,y):
    return x + y
from functools import reduce
l=[1,2,3,4,5]
# agar bina reduce ke use karna ho to
result = 0
for i in l:
    result = mysum(result, i)
print(result)  # Output: 15

# agar reduce ke sath use karna ho to
result_reduce = reduce(mysum, l)
print(result_reduce)  # Output: 15
