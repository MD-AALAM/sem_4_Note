with open("myfileSeek.txt",'r') as f:
    # move to the 10th byte in the  file
    f.seek(10)

    # tell function bata ta hai ki kitne character se read  start kar rahe hai
    
    print(f.tell())
    # read the next five bytes
    data=f.read(5)
    print(data)