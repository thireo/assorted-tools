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



for date in sorted(os.listdir(path)):
    if(os.path.isdir(path+date) and date != "firmware"): #and date.__contains__("2019_07_01")):
        print(date)
        currentPackage = 0
        tempData = []
        collData = {}
        for file in sorted(os.listdir(path+date)):
            
            if(file.__contains__(".bin")):
                with open(path+date+"/"+file, errors="ignore") as f:
                    data = []
                    test = f.readlines()
                    for line in test:
                        splitLine = line.split(" ")
                        if(splitLine[0].__contains__("Package")):
                            currentPackage = int(splitLine[2])
                            #print(currentPackage)
                        splitLine = line.split("\t")
                        if(splitLine.__len__() > 2):
                            cc0 += 1
                        elif(splitLine.__len__() == 2 and splitLine[0].__contains__("/")):
                            if(num_there(splitLine[1])):
                                data.append(int(splitLine[1]))
                                cc1 += 1
                            else:
                                cc += 1
                collData[currentPackage] = data
                #print(collData.__len__()," - ",currentPackage)
                if(collData.__len__() < currentPackage):
                    print("Missing Data ERROR")
                    break
                if(currentPackage == 0 and collData.__len__()>1):
                    #print(collData.__len__())
                    #print("bob")
                    for i in range(len(collData)):
                        #print(collData[collData.__len__()-1-i])
                        tempData.extend(collData[collData.__len__()-i-1])
                    collData = {}
                    currentPackage = 0

        #print(cc1)
        count = 0
        cc = 0
        cc0 = 0
        cc1 = 0
        #print(collData.__len__())
        #print(collData)
        #tempo = []
        #for i in range(.__len__()):
        #    tempo.extend(collData[collData.__len__()-i-1])
        plt.plot(tempData)
        plt.show()
        #print(tempData)
        #print(collData[9])
