#write
f=open("test.txt","w")
f.write("hi")
f.close()

#Append
f=open("test.txt","a")
f.write("\nbyee")
f.close()

#read garni
f=open ("test.txt","r")
print(f.read())
f.close()

