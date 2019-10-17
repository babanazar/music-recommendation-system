import pickle
from os import path
from os import listdir
import numpy
import pandas as pd
from scipy.spatial.distance import cosine
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
    # numerator = sum(a*b for a,b in zip(vector2,vector1))
    # denominator = square_rooted(vector1)*square_rooted(vector2)
    # return round(numerator/float(denominator),3)

artistNum = 3190371

userProfile={}


for uf in listdir(".\\dataset\\LFM-1b_UGP\\user_sets_min100"):
    tf = path.join(".\\dataset\\LFM-1b_UGP\\user_sets_min100", uf)
    with open(tf,'r') as file:
        for line in file:
            at = file.readline()
            temp = at.split("\t")
            if temp[0] not in userProfile:
                try:
                    userProfile.update({temp[0]:temp[1]+temp[2]})
                except:
                    pass


for uf in listdir(".\\dataset\\LFM-1b_UGP\\user_sets_min200"):
    tf = path.join(".\\dataset\\LFM-1b_UGP\\user_sets_min200", uf)
    with open(tf,'r') as file:
        for line in file:
            at = file.readline()
            temp = at.split("\t")
            if temp[0] not in userProfile:
                try:
                    userProfile.update({temp[0]:temp[1]+temp[2]})
                except:
                    pass

for uf in listdir(".\\dataset\\LFM-1b_UGP\\user_sets_min500"):
    tf = path.join(".\\dataset\\LFM-1b_UGP\\user_sets_min500", uf)
    with open(tf,'r') as file:
        for line in file:
            at = file.readline()
            temp = at.split("\t")
            if temp[0] not in userProfile:
                try:
                    userProfile.update({temp[0]:temp[1]+temp[2]})
                except:
                    pass

for uf in listdir(".\\dataset\\LFM-1b_UGP\\user_sets_min1000"):
    tf = path.join(".\\dataset\\LFM-1b_UGP\\user_sets_min1000", uf)
    with open(tf,'r') as file:
        for line in file:
            at = file.readline()
            temp = at.split("\t")
            if temp[0] not in userProfile:
                try:
                    userProfile.update({temp[0]:temp[1]+temp[2]})
                except:
                    pass


profileType = {}

count=0

for i in userProfile:
    if userProfile[i] not in profileType:
        profileType.update({userProfile[i]:count})
        count+=1

with open("ArtistListen" + '.pkl', 'rb') as f:
    a = pickle.load(f)

artistUserTypeMatrix = {}



faulty = 0
normal = 0

for line in a:
    try:
        type = userProfile[line]
        for x in a[line]:
            if str(x) not in artistUserTypeMatrix:
                artistUserTypeMatrix.update({str(x):{type:a[line][x]}})
            else:
                if type not in artistUserTypeMatrix[str(x)]:
                    artistUserTypeMatrix[str(x)].update({type:a[line][x]})
                else:
                    artistUserTypeMatrix[str(x)][type]+= a[line][x]
        normal+=1
    except:
        faulty+=1

print(faulty)
print(normal)

count = 0
delete = []

for i in artistUserTypeMatrix:
    if len(artistUserTypeMatrix[i])<5:
        delete.append(i)
    else:
        count+=1

for key in delete: del artistUserTypeMatrix[key]


for count,(artistId,dicto) in enumerate(artistUserTypeMatrix.items()):
    artistProfile = dicto
    min1 = 10000
    min2 = 10000
    min3 = 10000
    artistId11 = ""
    artistId12 = ""
    artistId13 = ""
    print(artistId)
    for count2,(artistId2,dicto2) in enumerate(artistUserTypeMatrix.items()):
        if count2 > count:
            cosSim,jacSim = cosine_similarity(dicto,dicto2)
            if count2%1000==0:
                print(count2)
            if jacSim< min1:
                min3 = min2
                min2=min1
                min1 = jacSim
                artistId13 = artistId12
                artistId12 = artistId11
                artistId11 = artistId2
                print(artistId+" "+artistId2+" min1 "+str(min1)+" "+ str(cosSim))
            elif jacSim < min2:
                artistId13 = artistId12
                artistId12 = artistId2
                min3=min2
                min2 = jacSim
                print(artistId + " " + artistId2 + " min2 " + str(min2) + " " + str(cosSim))
            elif jacSim < min3:
                artistId13 = artistId2
                min3 = jacSim
                print(artistId + " " + artistId2 + " min3 " + str(min3) + " " + str(cosSim))
    with open("SimilarArtistMatrix.txt",'a+') as similarArtists:
        similarArtists.write(artistId +" "+artistId11+" "+artistId12+" "+artistId13+"\n")

print(count)
