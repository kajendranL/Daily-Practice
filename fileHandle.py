# how to open a file using py


f=open("fhandle.txt",'r')
print("File Name :",f.name)
print("File.Mode: ",f.mode)
f.close()
print("File is closed: ",f.closed)

#write the file that has been opened

n=open("fhandle.txt",'w')
print("File Name :",n.name)
print("File Mode: ",n.mode)
print("Is it readable?", n.readable())
print("is it writable",n.writable())
n.write("add")
n.write("\nproduct")
print("Data written")
n.close()

# when above code was written all the orginal values gone

# use below function which prevents the data from being over written

c = open("fhandle.txt",'a') # append data # to open we need to use the = and not (dot).

twinkle =("\nTwinkle,twinkle little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky, \nTwinkle, twinkle little star \n\tHow I wonder what you are.")
c.writelines(twinkle)# written lines to write multiple lines
print("Rhyme is written")
c.close()


