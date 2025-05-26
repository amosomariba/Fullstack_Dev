# How to open a python file
# We use open() function always when handling pyhthon files
# We use read() methon if we want to read a python file
# You can use readlines() , read() , readline()
# Also close our files by close()


f = open("example.txt")

print(f.read())
f.close()

print('---------------------')


#2
# It is advisable to close file with the close () when you are done

f = open("example.txt")
print(f.readline()) 
f.close()

print('-------------------------')

# 3
# Using readlines()
f=open('example.txt')
print(f.readlines())
f.close()

print('-------------------------')