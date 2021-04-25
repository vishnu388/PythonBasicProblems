fileopen=open("file.txt", "w")
L=["my name is vishnu \n", "i am from AndhraPradesh \n", "city Ongole \n"]
fileopen.write("Hello \n")
fileopen.writelines(L)
fileopen.close()

fileopen=open("file.txt", "r+")
print("output of read ")
print(fileopen.read())
print()