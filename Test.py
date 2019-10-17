with open('artistSong.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

with open('artistSong.txt', 'w') as f:
    f.writelines(lines)

with open('artistSong.txt', 'r') as f:
    for x in range(10):
        temp = f.readline()
        temp = temp.split("\t")
        print(temp)