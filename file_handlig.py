#file handling 
#READ/ WRITE(APPEND)

#File opening modes
# r-read 
# w-write
# a-append(write)
# x-c reate
# b-binary
# t-text

# READING through File
# f=open("softwarica.txt","r")
# print(f.read())
# print(f.readline()) #print the first line
# print(f.readline()) #print 2nd line
# print(f.readline(2)) #it print only two characters in 3rd line

# for x in f:
    # print(x,end="") #end decrease the spacing
    
# print(f.readlines()) #line's' will display the list in horizontal


f=open("D:\\File Handling\softwarica.txt","r")
print(f.readline())
