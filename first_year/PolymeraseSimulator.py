import os
import random

x = 0
y = 0
triplet = ""
uuu = 0
uuc = 0
ucc = 0
ccc = 0
ccu = 0
cuu = 0
cuc = 0
ucu = 0

sequenceType = int(input("RNA (1) or DNA (2) sequence? (1)/(2): "))
tripletNumber = int(input("Please enter target number of triplet codons for your sequence: "))
GTP = input("GTP in sequence? y/n: ")
CTP = input("CTP in sequence? y/n: ")
ATP = input("ATP in sequence? y/n: ")
TTP = "n"
UTP = "n"
if sequenceType == 2:
    TTP = input("TTP in sequence? y/n: ")
elif sequenceType == 1:
    UTP = input("UTP in sequence? y/n: ")
#else:
    #pass

baseNumber = -1

#GTP
if GTP == "y":
    baseNumber = baseNumber + 1
#elif GTP == "n":
    #pass
#else:
    #pass
#CTP
if CTP == "y":
    baseNumber = baseNumber + 1
#elif CTP == "n":
    #pass
#else:
    #pass
#ATP
if ATP == "y":
    baseNumber = baseNumber + 1
#elif ATP == "n":
    #pass
#else:
    #pass
#TTP
if TTP == "y":
    baseNumber = baseNumber + 1
#elif TTP == "n":
    #pass
#else:
    #pass
#UTP
if UTP == "y":
    baseNumber = baseNumber + 1
#elif UTP == "n":
    #pass
#else:
    #pass

print(baseNumber)
baseList = []

while x <tripletNumber:
    while y < 3:
        ran_num = random.randint(0,baseNumber)
        if ran_num == 0:
            triplet = triplet+"G"
        elif ran_num == 1:
            triplet = triplet+"C"
        elif ran_num == 2:
            triplet = triplet+"A"
        elif ran_num == 3:
            if sequenceType == 1:
                triplet = triplet+"U"
            elif sequenceType == 2:
                triplet = triplet+"T"
            #else:
                #pass

        y = y + 1

    ###TEST AREA###
    #if triplet is in array, then pass, if not, then append
    if triplet not in baseList:
        baseList.append(triplet)
        print("triplet added")

    print(triplet)
    if triplet == "UUU":
        uuu = uuu + 1
    elif triplet == "UUC":
        uuc = uuc + 1
    elif triplet == "UCC":
        ucc = ucc + 1
    elif triplet == "CCC":
        ccc = ccc + 1
    elif triplet == "CCU":
        ccu = ccu + 1
    elif triplet == "CUU":
        cuu = cuu + 1
    elif triplet == "UCU":
        ucu = ucu + 1
    elif triplet == "CUC":
        cuc = cuc + 1




    triplet = ""
    y = 0
    x = x + 1

print("UUU:", uuu)
print("UUC:", uuc)
print("UCC:", ucc)
print("CCC:", ccc)
print("CCU:", ccu)
print("CUU:", cuu)
print("UCU:", ucu)
print("CUC:", cuc)

print(len(baseList))
#for x in range(len(baseList)):
    #print(baseList[x])
print("printing")
print(baseList)
