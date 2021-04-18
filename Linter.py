import os
def lineCount(fileName):
    file = open(fileName,"r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            Counter += 1
    return Counter

def gitignore(str):
    giti=list()
    try:
        f = open(str+"/.gitignore", "r")
        
        for x in f:
            giti.append(x[:-1])
        
    except:
        pass
    return giti

def lint(str):
    count =0
    for root, dirs, files in os.walk(str):
        if(files==[]):
            continue
        for i in files:
            count += lineCount(root+"/"+i)
    return count

def lintern(str):
    count = 0
    a = gitignore(str)
    a.append('.gitignore')
    for i in os.listdir(str):
        if i not in a and os.path.isdir(str+"/"+i)==True:
            count +=lint(str+"/"+i)
        elif i not in a and os.path.isfile(str+"/"+i)==True:
            count +=lineCount(str+"/"+i)
    return(count)

a = input("Enter the absolute path:")
print(lintern(a))
