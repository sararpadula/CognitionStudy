import pandas as pd

data = pd.read_csv("visitsJan5.csv")

kio1Visits = data['KIO1'].dropna().tolist()
kio2Visits = data['KIO2'].dropna().tolist()
kio3Visits = data['KIO3'].dropna().tolist()
kio4Visits = data['KIO4'].dropna().tolist()
kio5Visits = data['KIO5'].dropna().tolist()
kio6Visits = data['KIO6'].dropna().tolist()
kio7Visits = data['KIO7'].dropna().tolist()
kio8Visits = data['KIO8'].dropna().tolist()
allRFIDs = ["011016E3DC","011016F820","011016D53D","011016DA0D","011016CC76","011016E5EA","011016D2FD","0110171369","011016D969","01103F4BE2","0700E7DDD82","011016EE9B","011016CD35","3B001835CC","01103F7597","3B00492FBD","3B001950B7","3B0018F820","3B0018FB5A","01103FAC0D","3B00193FCF","3B001835B6","3B00192449","3B0019073E","3B0018A000","3B00194277","3B00183CAA","3B0018FF4A","3B00183748","3B0018487A","3B00184E29","3B001974F4","3B0019065A","01101732F9","3B0018651F","3B0018965B","01103FB335","3B0018564D","3B00186E09"]

isitinlist = 1
feederCount1 = 0
feederCount2 = 0
feederCount3 = 0
feederCount4 = 0
feederCount5 = 0
feederCount6 = 0
feederCount7 = 0
feederCount8 = 0
visitingBirds = ["start"]
visitingBirds1 = ["start"]
visitingBirds2= ["start"]
visitingBirds3 = ["start"]
visitingBirds4 = ["start"]
visitingBirds5 = ["start"]
visitingBirds6 = ["start"]
visitingBirds7 = ["start"]
visitingBirds8 = ["start"]

#KIO 1
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio1Visits):
    while j < len(allRFIDs):
        if kio1Visits[i] == allRFIDs[j]:
            feederCount1 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds1):
                if kio1Visits[i] == visitingBirds1[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                 if kio1Visits[i] == visitingBirds[l]:
                     masterList = 1
                 l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds1.append(kio1Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio1Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0
#KIO 2
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio2Visits):
    while j < len(allRFIDs):
        if kio2Visits[i] == allRFIDs[j]:
            feederCount2 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds2):
    
                if kio2Visits[i] == visitingBirds2[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio2Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds2.append(kio2Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio2Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0
#KIO 3
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio3Visits):
    while j < len(allRFIDs):
        if kio3Visits[i] == allRFIDs[j]:
            feederCount3 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds3):
                if kio3Visits[i] == visitingBirds3[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio3Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds3.append(kio3Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio3Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0
#KIO 4
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio4Visits):
    while j < len(allRFIDs):
        if kio4Visits[i] == allRFIDs[j]:
            feederCount4 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds4):
                if kio4Visits[i] == visitingBirds4[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio4Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds4.append(kio4Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio4Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0

#KIO 6
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio6Visits):
    while j < len(allRFIDs):
        if kio6Visits[i] == allRFIDs[j]:
            feederCount6 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds6):
                if kio6Visits[i] == visitingBirds6[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio6Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds6.append(kio6Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio6Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0
#KIO 7
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio7Visits):
    while j < len(allRFIDs):
        if kio7Visits[i] == allRFIDs[j]:
            feederCount7 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds7):
                if kio7Visits[i] == visitingBirds7[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio7Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds7.append(kio7Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio7Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    
t=0
#KIO 8
i = 0
j = 0
k = 0
l = 0
isitinlist = 1
masterList = 1
while i < len(kio8Visits):
    while j < len(allRFIDs):
        if kio8Visits[i] == allRFIDs[j]:
            feederCount8 += 1
            masterList =  0
            isitinlist = 0
            while k < len(visitingBirds8):
                if kio8Visits[i] == visitingBirds8[k]:
                    isitinlist = 1
                k+=1
            while l < len(visitingBirds):
                  if kio8Visits[i] == visitingBirds[l]:
                      masterList = 1
                  l+=1
        j += 1
    if isitinlist == 0:
        visitingBirds8.append(kio8Visits[i])
        isitinlist = 1
    if masterList == 0:
        visitingBirds.append(kio8Visits[i])
    j = 0
    k = 0
    l=0
    i += 1
    

t=0
print("ALL CHICKADEES THAT VISITED KIO FEEDER -------------------------------------------------------------------")
totalcount = feederCount1+feederCount2+feederCount3+feederCount4+feederCount5+feederCount6+feederCount7+feederCount8
totalcount = str(totalcount)
print("TOTAL VISITS TO KIO FEEDER:"+totalcount)
length = len(visitingBirds)
length = str(length)
print("TOTAL UNIQUE INDIVIDUALS:"+length)
while t < len(visitingBirds):
    print(visitingBirds[t])
    t += 1
t=0


print("KIO1 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount1 = str(feederCount1)
print("TOTAL KIO1 VISITS:"+feederCount1)
length1 = len(visitingBirds1)
length1 = str(length1)
print("TOTAL UNIQUE INDIVIDUALS:"+length1)
while t < len(visitingBirds1):
    print(visitingBirds1[t])
    t += 1

t=0
print("KIO2 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount2 = str(feederCount2)
print("TOTAL KIO2 VISITS:"+feederCount2)
length2 = len(visitingBirds2)
length2 = str(length2)
print("TOTAL UNIQUE INDIVIDUALS:"+length2)
while t < len(visitingBirds2):
    print(visitingBirds2[t])
    t += 1
    
t=0
print("KIO3 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount3 = str(feederCount3)
length3 = len(visitingBirds3)
length3 = str(length3)
print("TOTAL UNIQUE INDIVIDUALS:"+length3)
print("TOTAL KIO3 VISITS:"+feederCount3)
while t < len(visitingBirds3):
    print(visitingBirds3[t])
    t += 1

t=0
print("KIO4 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount4 = str(feederCount4)
print("TOTAL KIO4 VISITS:"+feederCount4)
length4 = len(visitingBirds4)
length4 = str(length4)
print("TOTAL UNIQUE INDIVIDUALS:"+length4)
while t < len(visitingBirds4):
    print(visitingBirds4[t])
    t += 1
t=0
print("KIO6 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount6 = str(feederCount6)
print("TOTAL KIO6 VISITS:"+feederCount6)
length6 = len(visitingBirds6)
length6 = str(length6)
print("TOTAL UNIQUE INDIVIDUALS:"+length6)
while t < len(visitingBirds6):
    print(visitingBirds6[t])
    t += 1

t=0
print("KIO7 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount7 = str(feederCount7)
print("TOTAL KIO7 VISITS:"+feederCount7)
length7 = len(visitingBirds7)
length7 = str(length7)
print("TOTAL UNIQUE INDIVIDUALS:"+length7)
while t < len(visitingBirds7):
    print(visitingBirds7[t])
    t += 1

t=0
print("KIO8 CHICKADEES ------------------------------------------------------------------------------------------")
feederCount8 = str(feederCount8)
print("TOTAL KIO8 VISITS:"+feederCount8)
length8 = len(visitingBirds8)
length8 = str(length8)
print("TOTAL UNIQUE INDIVIDUALS:"+length8)
while t < len(visitingBirds8):
    print(visitingBirds8[t])
    t += 1
