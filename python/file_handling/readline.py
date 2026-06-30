# # ye readline method line by line print karke deta hai
# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)


f=open('myfile1.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])   
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"marks of student {i} in maths is:{m1}")
    print(f"marks of student {i} in python is:{m2}")
    print(f"marks of student {i} in java is:{m3}")
    print(line)