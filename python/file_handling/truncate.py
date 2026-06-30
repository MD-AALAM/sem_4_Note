with open('truncate.txt','w') as f:
    f.write("hello world")
    # ye bata hai ki kitne character sirf write honi chahiye
    f.truncate(5)

with open('truncate.txt','r') as f:
    print(f.read())
