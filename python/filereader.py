import os
import numpy as np
import matplotlib.pyplot as plt

path = "data/"
count = 0
cc = 0
cc0 = 0
cc1 = 0

def num_there(s):
    return any(i.isdigit() for i in s)

collData = []
for date in os.listdir(path):
    if(os.path.isdir(path+date) and date != "firmware" and date.__contains__("2018_11_21")):
        print(date)
        currentPackage = 0
        
        for file in os.listdir(path+date):
            if(file.__contains__(".bin")):
                with open(path+date+"/"+file, errors="ignore") as f:
                    data = []
                    test = f.readlines()
                    for line in test:
                        splitLine = line.split(" ")
                        if(splitLine[0].__contains__("Package")):
                            #print(splitLine.__len__())
                            #print(int(splitLine[2]))
                            currentPackage = int(splitLine[2])
                        splitLine = line.split("\t")
                        if(splitLine.__len__() > 2):
                            #print(bob.__len__())
                            #print(bob)
                            cc0+=1
                        elif(splitLine.__len__() == 2 and splitLine[0].__contains__("/")):
                            #with int(splitLine[1],base=10) as temp:
                            #    tt = temp
                            #    print(tt)
                            if(num_there(splitLine[1])):
                                data.append(int(splitLine[1]))
                                collData[currentPackage].append(int(splitLine[1]))
                                cc1 += 1
                        else: 
                            cc += 1
                    #print(test[5:7])
                    #print(file)
                    #cc += test.__len__()
                    #collData[0][:] = data
                    
                #count+=1
        #print(cc0,"/",cc1," - ",cc)
        count = 0
        cc = 0
        cc0 = 0
        cc1 = 0
print(collData)
plt.plot(collData)
plt.show()
