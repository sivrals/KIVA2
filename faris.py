#ORDERAN MASUK
import random
import time

def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))




i = 0



def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d/%m/%Y %I:%M %p', prop)


while True:
    if i < 10:
        print(randomDate("1/7/2019 1:30 PM", "20/7/2019 4:50 AM", random.random()))
        i = i + 1 
    elif i>=10:
        break
#diambil due date paling dikit        
    

#MANHATAN DISTANCE
a = [[13,16],[24,1],[28,2],[26,18],[33,30]] #koordinat (x,y) pada AGV

p1 = [8,20,2,8,3]       #korrdinat (x) pada POD
p2 = [2,11,16,17,32]    #koordinat (y) pada POD                          

i=0
j=0

matriks = []             #membuat matrix 
while j<5:               #looping untuk ke-5 AGV
    i=0
    k=[]
    while i<5:           #looping untuk ke-5 POD
        manhattan = ((abs(a[j][0]-p1[i])+abs(a[j][1]-p2[i])))
        k.append (manhattan)
        #print (manhattan)
        i+=1
    matriks.append(k)
        
    j+=1

print ("")
print ("Manhattan distance between AGV and POD =") 
print ("========================================")
print ("")
#print ("AGV 1","AGV 2","AGV 3","AGV 4","AGV 5",)

print ("POD 1", matriks[0])
print ("POD 2", matriks[1])
print ("POD 3", matriks[2])
print ("POD 4", matriks[3])
print ("POD 5", matriks[4])

#print (matriks[0],"", matriks[5],"",matriks[10],"", matriks[15],"", matriks[20])
#print (matriks[1],"", matriks[6],"",matriks[11],"", matriks[16],"", matriks[21])
#print (matriks[2],"", matriks[7],"",matriks[12],"", matriks[17],"", matriks[22])
#print (matriks[3],"","", matriks[8],"",matriks[13],"", matriks[18],"", matriks[23])
#print (matriks[4],"", matriks[9],"",matriks[14],"", matriks[19],"", matriks[24])

#import numpy as np
#matrix = np.zeros( (5, 10) )
#print(matrix)