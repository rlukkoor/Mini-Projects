myfile = open("file1.txt","w")

R = ["My first name is Rohith \n","My middle name is Anjan \n","My last name is Lukkoor \n"] 
  
myfile.write("Hello \n")
myfile.writelines(R)
myfile.close()

myfile = open("myfile.txt","a")
myfile.write("I am from California \n")
myfile.close()
  
myfile = open("myfile.txt","r+") 
  
print "Output of Read function is "
print myfile.read()
print
  
myfile.seek(0) 
  
print "Output of Readline function (returns 1st line only) is "
print myfile.readline()
print
  
myfile.seek(0)

print "Output of Readlines function (returns each line as a separate element in a list) is "
print myfile.readlines()
print
myfile.close()