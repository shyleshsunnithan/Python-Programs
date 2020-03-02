import os

f1 = open("TextFile1.txt","a")
f2 = open("TextFile1.txt","r")

print("Do you wish to add any data?(YES/NO): ")
data_choice=input()

while data_choice=="YES":
    text = input("Enter text to be written: ")        
    newline = "\n"

    f1.write(text)
    f1.write(newline)

    print("Do you wish to add any data?(YES/NO): ")
    data_choice=input()

if data_choice == "NO":
    print("Do you want to overwrite the file?(Yes/No): ")
    choice = input()


print("Do you wish to view the data?(YES/NO): ")
view_choice=input()

if view_choice == "YES":
    print("Text read from file is ")
    for x in f2:
        print(x)
        print("\n")

f1.close()

print("\n")

print("Do you want to overwrite the file?(Yes/No): ")
choice = input()

while choice == "Yes" :
    f3 = open("TextFile1.txt","w")
    text1 = input("Enter text to be written: ")
    f3.write(text1)
    f3.close()

    f4 = open("TextFile1.txt","r")
    print("\v")
    print("Text read from file is ")
    for y in f4:
        print(y)
        print("\n")
    
    print("Do you want to overwrite the file?(Yes/No): ")
    choice = input()

    f4.close()
    f2.close()

if choice == "No":
    print("\v")
    print("Do you want to delete the file?(Yes/No): ")
    ch = input()
    if ch == "Yes":
        os.remove("TextFile1.txt")
        print("\n")
        print("File has been deleted successfuly!") 
        print("\n")  

    elif ch == "No":
        exit(0) 


