from os import path
import pickle


filePath = path.join(".\\dataset", "LFM-1b_LEs.txt")

userId = "-1"
userCount = 0
userIterator = 0

userList = {}
tempArray = {}

alreadyVisited = False

listeningEvents = []


with open(filePath, "r", encoding="UTF-8") as f:
    for line in f:
        temp = f.readline()
        temp = temp.split("\t")
        if temp[0]==userId:
            if temp[1] in tempArray:
                tempArray[temp[1]] += 1
            else:
                tempArray.update({temp[1]:1})
        else:
            try:
                userList.pop(userId)
            except:
                print(userId)
            userList[userId] = tempArray

            userIterator += 1

            if userCount%100 == 0:
                print(userCount)
                print(userId)

            tempArray = {}
            userId = temp[0]

            if userId not in userList:
                userCount += 1
                userList.update({temp[0]:tempArray})
                tempArray.update({temp[1]: 1})
            else:
                tempArray = userList[userId]
                if temp[1] in tempArray:
                    tempArray[temp[1]] += 1
                else:
                    tempArray.update({temp[1]: 1})

listenText = open('ListeningEvents.txt', 'w')

for k, v in userList.items():
    listenText.write(str(k) + "\t" + str(v) + '\n')
listenText.close()

with open("ArtistListen" + '.pkl', 'wb+') as f:
    pickle.dump(userList, f, pickle.HIGHEST_PROTOCOL)

with open("ArtistListen" + '.pkl', 'rb') as f:
    a = pickle.load(f)

print(a[0])

