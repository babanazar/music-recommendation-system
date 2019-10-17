import pickle
from os import path
from os import listdir
import numpy
import pandas as pd
from scipy.spatial.distance import cosine
import traceback
from math import*

def jaccard_similarity(list1, list2):
    list3 = numpy.array(list1)-numpy.array(list2)
    sum=0
    for num in list3:
        sum+=abs(num)
    union = sum/len(list3)
    return union

def square_rooted(x):

    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):

    input1 = {}
    input2 = {}
    vector2 = []
    vector1 =[]

    if len(x) >= len(y):
        input1 = x
        input2 = y
    else:
        input1 = y
        input2 = x


    vector1 = list(input1.values())

    for k in input1.keys():    # Normalizing input vectors.
        if k in input2:
            vector2.append(float(input1[k]))
        else :
            vector2.append(float(0))

    return cosine(vector1,vector2),jaccard_similarity(vector1,vector2)

with open("ArtistListen" + '.pkl', 'rb') as f:
    a = pickle.load(f)

filePath = path.join(".\\dataset\\LFM-1b_UGP", "LFM-1b_artist_genres_freebase.txt")

filePath1 = path.join(".\\dataset", "LFM-1b_artists.txt")
file2= open(filePath1,'r', encoding="UTF-8")

file = open(filePath,'r', encoding="UTF-8")

artistGenreMatrix = {}
artistIdMatrix = {}

for line in file2:
    try:
        temp = file2.readline()
        splited = temp.split("\t")
        artistIdMatrix.update({splited[1].rstrip("\n"):splited[0]})
    except Exception:
        pass

for line1 in file:
    try:
        temp = file.readline()
        splited = temp.split("\t")
        artistGenreMatrix.update({artistIdMatrix[splited[0]]:{splited[i]:1 for i in range(1,len(splited)-1)}})
    except Exception:
        pass

print("startin")
for line2 in a:
    try:
        userVectorTemp = {}
        min1=10000
        min2=10000
        min3=10000
        artistId11=""
        artistId12=""
        artistId13=""
        for i in a[line2]:
            try:
                for j in artistGenreMatrix[i]:
                    if j not in userVectorTemp:
                        userVectorTemp.update({j:a[line2][i]})
                    else:
                        userVectorTemp[j] += a[line2][i]
            except:
                pass
            cosSim, jacSim = cosine_similarity(userVectorTemp, artistGenreMatrix[i])
            if jacSim < min1:
                min3 = min2
                min2 = min1
                min1 = jacSim
                artistId13 = artistId12
                artistId12 = artistId11
                artistId11 = i
                print(line2 + " " + i + " min1 " + str(min1) + " " + str(cosSim))
            elif jacSim < min2:
                artistId13 = artistId12
                artistId12 = i
                min3 = min2
                min2 = jacSim
                print(line2 + " " + i + " min2 " + str(min2) + " " + str(cosSim))
            elif jacSim < min3:
                artistId13 = i
                min3 = jacSim
                print(line2 + " " + i + " min3 " + str(min3) + " " + str(cosSim))
    except Exception:
        pass

# for line in a:
#     try:
#         for x in a[line]: