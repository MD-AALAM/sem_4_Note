def cube(x):
    return x * x * x
print(cube(3))  # Output: 27

l=[1,2,4,6,4,3]
# agar bina map ke use karna ho to
result=[]
for i in l:
    result.append(cube(i))
print(result)  # Output: [1, 8, 64, 216, 64, 27]

# agar map ke sath use karna ho to
result_map = list(map(cube, l))
print(result_map)  # Output: [1, 8, 64, 216

# isko lamda function ke sath bhi kar sakte hai
result_map_lambda = list(map(lambda x: x * x * x, l))
print(result_map_lambda)  # Output: [1, 8, 64, 216, 64, 27]