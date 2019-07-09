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


collData = {}
for date in os.listdir(path):
    if(os.path.isdir(path+date) and date != "firmware" and date.__contains__("2018_11_21")):
        print(date)
        currentPackage = 0
        tempData = []
        for file in os.listdir(path+date):
            if(file.__contains__(".bin")):
                with open(path+date+"/"+file, errors="ignore") as f:
                    data = []
                    test = f.readlines()
                    for line in test:
                        splitLine = line.split(" ")
                        if(splitLine[0].__contains__("Package")):
                            currentPackage = int(splitLine[2])
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
        count = 0
        cc = 0
        cc0 = 0
        cc1 = 0

tempo = []
print(collData.__len__())
print(range(collData.__len__()))
for i in range(collData.__len__()):
    tempo.extend(collData[collData.__len__()-i-1])

plt.plot(tempo)
plt.show()
