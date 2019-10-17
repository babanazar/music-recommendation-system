import pickle
import numpy
from sklearn import metrics
from scipy import spatial


def jaccard_similarity(list1, list2):
    list3 = numpy.array(list1)-numpy.array(list2)
    sum=0
    for num in list3:
        sum+=abs(num)
    union = sum/len(list3)
    return union

with open("ArtistListen" + '.pkl', 'rb') as f:
    a = pickle.load(f)

print("here")
# similarityDict = [[-1 for i in range(len(a.keys()))]for j in range(len(a.keys()))]

for count,(userId,dicto) in enumerate(a.items()):
    if userId!="-1":
        print("\n"+userId)
        userListenEvents = []
        for j in a[userId]:
            userListenEvents.append(a[userId][j])
        print(count)

        min1 = 10000
        min2 = 10000
        min3 = 10000
        userId11 = ""
        userId12 = ""
        userId13 = ""

        for count2,(userId2,dicto2) in enumerate(a.items()):
            if count2>count:
                tempListeningEvents = []
                for x in a[userId]:
                    if x in a[userId2]:
                        tempListeningEvents.append(a[userId2][x])
                    else:
                        tempListeningEvents.append(0)

                jacSim = jaccard_similarity(tempListeningEvents,userListenEvents)
                cosSim =  1 - spatial.distance.cosine(tempListeningEvents, userListenEvents)
                if jacSim < min1:
                    min3 = min2
                    min2 = min1
                    min1 = jacSim
                    userId13 = userId12
                    userId12 = userId11
                    userId11 = userId2
                    print(userId + " " + userId2 + " min1 " + str(min1) + " " + str(cosSim))
                elif jacSim < min2:
                    userId13 = userId12
                    userId12 = userId2
                    min3 = min2
                    min2 = jacSim
                    print(userId + " " + userId2 + " min2 " + str(min2) + " " + str(cosSim))
                elif jacSim < min3:
                    userId13 = userId2
                    min3 = jacSim
                    print(userId + " " + userId2 + " min3 " + str(min3) + " " + str(cosSim))
        with open ("SimilarUserMatrix.txt",'a+') as similarArtists:
            similarArtists.write(userId + " " + userId11 + " " + userId12 + " " + userId13+"\n")




# for x in a[line]:
#     print(str(line) + " "+str(x) + " " +str(a[line][str(x)]))