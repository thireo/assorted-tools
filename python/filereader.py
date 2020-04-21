import os

def num_there(s):
    return any(i.isdigit() for i in s)


def process(path,plot):
    for date in sorted(os.listdir(path)):
        #print(path+date)
        if(os.path.isdir(path+date) and date != "firmware"): #and date.__contains__("2019_07_01")):
            errorOccurred = False
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
                            splitLine = line.split("\t")
                            if(splitLine.__len__() > 2):
                                continue
                            elif(splitLine.__len__() == 2 and splitLine[0].__contains__("/")):
                                if(num_there(splitLine[1])):
                                    data.append(int(splitLine[1]))
                    collData[currentPackage] = data
                    if(collData.__len__() < currentPackage):
                        print(date,"Missing Data ERROR")
                        print("File: ",file)
                        errorOccurred = True
                        break
                    if(currentPackage == 0 and collData.__len__()>1):
                        for i in range(len(collData)):
                            tempData.extend(collData.get(collData.__len__()-i-1,[]))
                        collData = {}
                        currentPackage = 0
            if(not errorOccurred):
                f = open("data/"+date,"w+")
                for line in tempData:
                    f.write("%d\n"%line)
                f.close()
            else:
                if(os.path.exists(("data/"+date))):
                    os.remove("data/"+date)
                    #print("data/"+date)

def main(argv):
    import argparse
    parser = argparse.ArgumentParser(description="Does stuff")
    parser.add_argument("-d", "--directory", dest='path',default= '', required=True,help='filenamo')
    parser.add_argument("-p","--plot", dest="plot",default=False,required=False,help='PLOOTT')
    args = parser.parse_args(argv)
    print(args.path)
    process(args.path,False)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
