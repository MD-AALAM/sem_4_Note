def  filter_function(a):
    return a>2
l=[1,2,4,6,4,3]
# agar bina filter ke use karna ho to
result=[]
for i in l:
    if filter_function(i):
        result.append(i)
print(result)  # Output: [4, 6, 4, 3]

# agar filter ke sath use karna ho to
result_filter = list(filter(filter_function, l))
print(result_filter)  # Output: [4, 6, 4, 3]
