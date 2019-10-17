import time
import itertools
from os import path
import multiprocessing as mp,os



def process_wrapper(chunkStart, chunkSize):
    filePath = path.join(".\\dataset", "LFM-1b_LEs.txt")
    count = 0
    print(chunkStart)
    with open(filePath, "r", encoding="UTF-8") as f:
        f.seek(chunkStart)
        lines = f.read(chunkSize).splitlines()
        for line in lines:
            count+=1


def chunkify(fname,size=24*4096):
    fileEnd = os.path.getsize(fname)
    with open(fname,'rb') as f:
        chunkEnd = f.tell()
        while True:
            chunkStart = chunkEnd
            f.seek(size,1)
            f.readline()
            chunkEnd = f.tell()
            yield chunkStart, chunkEnd - chunkStart
            if chunkEnd > fileEnd:
                break
if __name__ == '__main__':
#init objects
    pool = mp.Pool(mp.cpu_count())
    jobs = []

    #create jobs
    filePath = path.join(".\\dataset", "LFM-1b_LEs.txt")

    for chunkStart,chunkSize in chunkify(filePath):
        jobs.append( pool.apply_async(process_wrapper,(chunkStart,chunkSize)) )

    #wait for all jobs to finish
    for job in jobs:
        job.get()

    #clean up
    pool.close()