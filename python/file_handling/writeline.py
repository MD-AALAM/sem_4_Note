f=open('myfile2.txt','w')
line=['line1\n','line2\n','line3\n','line4\n']
f.writelines(line)
f.close()