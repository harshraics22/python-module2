# Python program to merge two files 
data = data2 = "" 
# Reading data from first file 
with open('footballer.txt') as fp: 
    data = fp.read()

with open('coaches.txt') as fp: 
    data2 = fp.read() 

# Merging two files into one another file 
data += "\n"
data += data2 
f2 = open("final.txt","w")
d = f2.write(data)
print(d)

    

