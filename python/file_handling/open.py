# simple to write and read method 
with open('myfile.txt','a') as f:
    f.write("my age is 20")
    f.write("\ni am a student")


f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()