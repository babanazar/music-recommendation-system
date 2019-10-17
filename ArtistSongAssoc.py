from os import path


size = 3190372
filePath = path.join(".\\dataset", "LFM-1b_tracks.txt")
strs = ["%s"%x for x in range(size)]


print("starting classification")

with open(filePath, "r", encoding="UTF-8") as f:
    for line in f:
        splitted = line.split("\t")
        strs[int(splitted[2])] = strs[int(splitted[2])]+"\t "+ splitted[0]
        if int(splitted[0])%1000000 == 1:
            print(splitted[0])

with open('artistSong.txt', 'w') as f:
    for item in strs:
        f.write("%s" % item)