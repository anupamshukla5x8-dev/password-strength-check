def Journal_entry():
 Date = input("Date:")
 time = input("Time:")
 Content= input("Entry:")
 with open("C:/Users/Lenovo/Documents/Programs/python_files/simple-projects/journal.txt","a") as f:
    f.write("Date:")
    f.write(Date)
    f.write("\n")
    f.write("Time:")
    f.write(time)
    f.write("\n")
    f.write("Entry:")
    f.write(Content)
    f.write("\n")
    f.write(".......")
    f.write("\n")

HI = input("Hi!")  
if HI == "start" :
   Journal_entry()


