f = open('source.txt','r')
data = f.read()
f2 = open('source2.txt','w')
data2 = f2.write(data)
print(data2)
f.close()