#Task1

Radius = 5
Area=3.14*Radius*Radius
print("Area:",Area)

#Task2

Name=str(input("Input the File Name:"))
sep = Name.split(".")
extn = sep[-1]
if(extn == "py")==True:
    print("Python")
    
if(extn == "java")==True:
    print("JavaScript")
    
if(extn == "c")==True:
    print("C language")
