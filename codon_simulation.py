import os
import random

x = 0
y = 0
letter = ""
uuu = 0
uuc = 0
ucc = 0
ccc = 0
ccu = 0
cuu = 0
cuc = 0
ucu = 0

while x <100001:
    while y < 3:
        ran_num = random.randint(0,1)
        if ran_num == 0:
            letter = letter+"U"
        elif ran_num == 1:
            letter = letter+"C"

        y = y + 1

    print(letter)
    if letter == "UUU":
        uuu = uuu + 1
    elif letter == "UUC":
        uuc = uuc + 1
    elif letter == "UCC":
        ucc = ucc + 1
    elif letter == "CCC":
        ccc = ccc + 1
    elif letter == "CCU":
        ccu = ccu + 1
    elif letter == "CUU":
        cuu = cuu + 1
    elif letter == "UCU":
        ucu = ucu + 1
    elif letter == "CUC":
        cuc = cuc + 1
   

    letter = ""
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

    
