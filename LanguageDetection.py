from langdetect import detect
from os import path
import threading
import time
import itertools
from multiprocessing import Process

numberOfTracks = 32291134

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def fromZerotoAHundredThousand():
    filePath = path.join(".\\dataset","LFM-1b_tracks.txt")
    counter = 0

    languages = open("languages2.txt","a",encoding="UTF-8")


    text_file = open(filePath, "r",encoding="UTF-8")
    lines = text_file.readlines()

    count = 0
    list = []
    langList = []


    ticks = 0
    for index,line in enumerate(lines):
        if (index > 2399999):
            if(index == 2600000):
                break
            list.append(line.split("\t"))
            try:
                languages.write(str(list[count][0])+"\t"+str(detect(list[count][1]))+"\t"+str(list[count][2]))
            except:
                languages.write(str(list[count][0])+"\tunknown\t"+str(list[count][2]))

            if count % 1000 == 0:
                ticks = time.process_time() - ticks
                print("thread1 "+str(ticks))
                ticks = time.process_time()
                print("thread1 "+str(count))
            count+=1

    text_file.close()

def from100000toTwoHoundredThousand():
    filePath = path.join(".\\dataset","LFM-1b_tracks.txt")
    counter = 0

    languages = open("languages3.txt","a",encoding="UTF-8")

    text_file = open(filePath, "r",encoding="UTF-8")
    lines = text_file.readlines()

    count = 0
    list = []
    langList = []


    ticks = 0
    for index,line in enumerate(lines):
        if(index>2599999):
            if(index == 2800000):
                break
            list.append(line.split("\t"))
            try:
                languages.write(str(list[count][0])+"\t"+str(detect(list[count][1]))+"\t"+str(list[count][2]))
            except:
                languages.write(str(list[count][0])+"\tunknown\t"+str(list[count][2]))

            if count % 1000 == 0:
                ticks = time.process_time() - ticks
                print("thread2 "+ str(ticks))
                ticks = time.process_time()
                print("thread2 " + str(count))
            count+=1

    text_file.close()

def from200000toThreeHoundredThousand():
    filePath = path.join(".\\dataset","LFM-1b_tracks.txt")
    counter = 0

    languages = open("languages4.txt","a",encoding="UTF-8")

    text_file = open(filePath, "r",encoding="UTF-8")
    lines = text_file.readlines()

    count = 0
    list = []
    langList = []


    ticks = 0
    for index,line in enumerate(lines):
        if(index>2799999):
            if(index == 3000000):
                break
            list.append(line.split("\t"))
            try:
                languages.write(str(list[count][0])+"\t"+str(detect(list[count][1]))+"\t"+str(list[count][2]))
            except:
                languages.write(str(list[count][0])+"\tunknown\t"+str(list[count][2]))

            if count % 1000 == 0:
                ticks = time.process_time() - ticks
                print("thread3 "+ str(ticks))
                ticks = time.process_time()
                print("thread3 " + str(count))
            count+=1

    text_file.close()

def from300000toFourHoundredThousand():
    filePath = path.join(".\\dataset","LFM-1b_tracks.txt")
    counter = 0

    languages = open("languages5.txt","a",encoding="UTF-8")

    text_file = open(filePath, "r",encoding="UTF-8")
    lines = text_file.readlines()

    count = 0
    list = []
    langList = []


    ticks = 0
    for index,line in enumerate(lines):
        if(index>2999999):
            if(index == 3200000):
                break
            list.append(line.split("\t"))
            try:
                languages.write(str(list[count][0])+"\t"+str(detect(list[count][1]))+"\t"+str(list[count][2]))
            except:
                languages.write(str(list[count][0])+"\tunknown\t"+str(list[count][2]))

            if count % 1000 == 0:
                ticks = time.process_time() - ticks
                print("thread4 "+ str(ticks))
                ticks = time.process_time()
                print("thread4 " + str(count))
            count+=1

    text_file.close()

if __name__ == '__main__':
    filePath = path.join(".\\dataset", "LFM-1b_tracks.txt")
    text_file = open(filePath, "r",encoding="UTF-8")
    lines = text_file.readlines()

    p = Process(target=fromZerotoAHundredThousand)
    p2 = Process(target=from100000toTwoHoundredThousand)
    p3 = Process(target=from200000toThreeHoundredThousand)
    p4 = Process(target=from300000toFourHoundredThousand)

    p.start()
    p2.start()
    p3.start()
    p4.start()

    p.join()
    p2.join()
    p3.join()
    p4.join()

# with open(filePath,"r",encoding="UTF-8") as infile:
#     for line in infile:
#         listOfStr=line.split("\t")
#         counter = int(listOfStr[0])
#         if counter > lastLine:
#             if counter == 1:
#                 ticks = time.process_time()
#
#             if len(listOfStr)>1:
#                 try:
#                     strLine = "{0}\t{2}\t{1}".format(counter, listOfStr[2] ,detect(listOfStr[1]))
#                     languages.write(strLine)
#                 except:
#                     strLine = "{0}\t{2}\t{1}".format(counter, listOfStr[2] , "unknown")
#                     languages.write(strLine)
#             if counter%1000 == 1:
#                 ticks = time.process_time() - ticks
#                 print(ticks)
#                 ticks = time.process_time()
#                 print(counter)
