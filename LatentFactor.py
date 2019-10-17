import numpy as np
import platform
import multiprocessing as mp
from operator import itemgetter
from multiprocessing import Process
import math
# from datetime import datetime
import datetime


def readDataset(fileName, userSongRating):
    print(f'\n\nstarted reading file {fileName} at {datetime.datetime.now().time()}')
    # userSongRating.append([11, 12, 13])
    with open(fileName, 'r') as f:
        i = 0
        for line in f:
            user_id, song_id, rating = line.split()
            user_id = int(user_id)
            song_id = int(song_id)
            rating = int(rating) * 1.0
            userSongRating.append([song_id, user_id, rating])
            i += 1
            # print(f'line {i}')
            # if i == 1000000:
            if user_id == 50:
                print(f'done with file {fileName}')
                break
    print(f'finished reading file {fileName} at {datetime.datetime.now().time()}\n\n')

def dotProduct(r, c, x, y):
    ret = 0;

    for i in range(len(r[x])):
        ret += r[x][i] * c[i][y];

    return ret;

def main():
    # resultFileName = input("Enter the file name you want to record results:")

    resultFileName = input('Enter file name to save result, (time to be unique):')
    now = datetime.datetime.now().time().strftime("%m/%d/%Y, %H:%M:%S")
    # print(resultFileName)
    result = open(resultFileName, "a")

    # result.write('deneme')
    result.write(f'started reading at {now}\n')

    # print(f'platform is {platform.architecture()}')
    trains = ['train_0.txt', 'train_1.txt', 'train_2.txt', 'train_3.txt', 'train_4.txt', 'train_5.txt', 'train_6.txt',
              'train_7.txt', 'train_8.txt', 'train_9.txt']
    tests = ['test_0.txt', 'test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt', 'test_6.txt',
             'test_7.txt', 'test_8.txt', 'test_9.txt']
    manager = mp.Manager()
    matrix_R = manager.list()
    # print(matrix_R)

    p0 = mp.Process(target=readDataset, args=(trains[0], matrix_R))
    p1 = mp.Process(target=readDataset, args=(trains[1], matrix_R))
    p2 = mp.Process(target=readDataset, args=(trains[2], matrix_R))
    p3 = mp.Process(target=readDataset, args=(trains[3], matrix_R))
    p4 = mp.Process(target=readDataset, args=(trains[4], matrix_R))
    p5 = mp.Process(target=readDataset, args=(trains[5], matrix_R))
    p6 = mp.Process(target=readDataset, args=(trains[6], matrix_R))
    p7 = mp.Process(target=readDataset, args=(trains[7], matrix_R))
    p8 = mp.Process(target=readDataset, args=(trains[8], matrix_R))
    p9 = mp.Process(target=readDataset, args=(trains[9], matrix_R))
    #
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    #
    p0.join()
    p1.join()
    p2.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()



    now = datetime.datetime.now().time().strftime("%H:%M:%S")
    print(f'finished reading at {now}')
    result.write(f'finished reading at {now}\n')
    # result.write(now)


    now = datetime.datetime.now().time().strftime("%H:%M:%S")
    print(f'starting calculation at {now}')
    result.write(f'starting calculation at {now}\n')
    # result.write(now)

    print(f'-{matrix_R}-')

    print(f'size of train {len(matrix_R)}')
    result.write(f'size of train data is {len(matrix_R)}\n')
    print('converting to np array...')

    matrix_R = np.array(matrix_R)  # convert list to numpy array
    print(f'length of user song rating {len(matrix_R)}')

    ratingToplam = {}
    userSayisi = {}

    print('initializing ratingToplam & userSayisi')
    for i in range(len(matrix_R)):
        ratingToplam[int(matrix_R[i][1])] = 0
        userSayisi[int(matrix_R[i][1])] = 0

    print('calculating overall sum, ratingToplam, and userSayisi')
    overall_sum = 0
    for i in range(len(matrix_R)):
        overall_sum += matrix_R[i][2]
        ratingToplam[int(matrix_R[i][1])] += matrix_R[i][2]
        userSayisi[int(matrix_R[i][1])] += 1

    print('rating toplam:')
    print(ratingToplam)

    print('user sayisi:')
    print(userSayisi)

    # normalization
    print('normalization...')
    for i in range(len(matrix_R)):
        matrix_R[i][2] = matrix_R[i][2] - ratingToplam[matrix_R[i][1]]/userSayisi[matrix_R[i][1]]

    print('after normalization')
    # print(matrix_R)





    ############ test ############
    manager_test = mp.Manager()
    matrix_test = manager_test.list()

    p0 = mp.Process(target=readDataset, args=(tests[0], matrix_test))
    p1 = mp.Process(target=readDataset, args=(tests[1], matrix_test))
    p2 = mp.Process(target=readDataset, args=(tests[2], matrix_test))
    p3 = mp.Process(target=readDataset, args=(tests[3], matrix_test))
    p4 = mp.Process(target=readDataset, args=(tests[4], matrix_test))
    p5 = mp.Process(target=readDataset, args=(tests[5], matrix_test))
    p6 = mp.Process(target=readDataset, args=(tests[6], matrix_test))
    p7 = mp.Process(target=readDataset, args=(tests[7], matrix_test))
    p8 = mp.Process(target=readDataset, args=(tests[8], matrix_test))
    p9 = mp.Process(target=readDataset, args=(tests[9], matrix_test))

    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()

    p0.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()

    print('converting test to np array...')

    matrix_test = np.array(matrix_test)  # convert list to numpy array

    result.write(f'length of matrix test is {len(matrix_test)}\n')
    # normalizing test

    ratingToplamTest = {}
    userSayisiTest = {}
    # print('initializing ratingToplam & userSayisi')
    for i in range(len(matrix_test)):
        ratingToplamTest[int(matrix_test[i][1])] = 0
        userSayisiTest[int(matrix_test[i][1])] = 0

    # print('calculating overall sum, ratingToplam, and userSayisi')
    overall_sum = 0
    for i in range(len(matrix_test)):
        overall_sum += matrix_test[i][2]
        ratingToplamTest[int(matrix_test[i][1])] += matrix_test[i][2]
        userSayisiTest[int(matrix_test[i][1])] += 1

    # print('rating toplam:')
    # print(ratingToplamTest)
    #
    # print('user sayisi:')
    # print(userSayisiTest)
    #
    # normalization
    # print('normalization...')
    for i in range(len(matrix_test)):
        # print(f'matrix_test is {matrix_test[i][2]}')
        matrix_test[i][2] = matrix_test[i][2] - ratingToplamTest[int(matrix_test[i][1])] / userSayisiTest[int(matrix_test[i][1])]
        # print(f'matrix_test became {matrix_test[i][2]}')

    # print('after test normalization')

    # print(matrix_test)


    # matrix_test, matrix_R = matrix_R, matrix_test
    # ratingToplam, ratingToplamTest = ratingToplamTest, ratingToplam
    # userSayisi, userSayisiTest = userSayisiTest, userSayisi




    k = 3  # this is number of factors
    print(f'\noverall->{overall_sum}\n')

    # train_mean = overall_sum / len(matrix_R)

    overall_sum = overall_sum / len(matrix_R)
    print(f'average {overall_sum}')
    value = math.sqrt(overall_sum/k)
    print(f'\nvalue ->{value}\n')

    maxUser = 0
    maxSong = 0
    # this line subtracts mean of user's rating from each rating to normalize user's ratings
    for i in range(len(matrix_R)):
        if matrix_R[i][0] > maxSong:
            maxSong = matrix_R[i][0]

        if matrix_R[i][1] > maxUser:
            maxUser = matrix_R[i][1]

    maxSong = int(maxSong)
    maxUser = int(maxUser)

    print(f'max song is {maxSong}')
    print(f'max user is {maxUser}')

    q = np.random.rand(140000, k) * 2 - 1
    pt = np.random.rand(k, 2000000) * 2 -1

    # print('pt is')
    # print(pt)
    #
    # print(f'q len {len(q[0])} ')
    # print(q)

    threshhold = 0.05  # change this to correct value
    epsilon_xi = 1

    result.write(f'threshold is {threshhold}\n')

    myu_1 = 0.002
    myu_2 = 0.005
    lam_1 = 0.02
    lam_2 = 0.02
    iter = 0
    eps = 1;

    while abs(eps) > threshhold:
    # while 1 == 1:
        iter += 1
        print(f'iteration is {iter}')
        print(f'epsilon {eps}')
        eps = 0;

        # if iter == 100:
        #     print(f'faced break')
        #     break

        for i in range(len(matrix_R)):
            song_i = int(matrix_R[i][0])
            user_i = int(matrix_R[i][1])

            dot_product = dotProduct(q, pt, song_i, user_i);

            tmp = ratingToplam[user_i] / userSayisi[user_i];
            eps += abs(round(matrix_R[i][2]+tmp) - round(dot_product+tmp))

            epsilon_xi = matrix_R[i][2] - dot_product;

            for j in range(k):
                q_i = q[song_i][j]
                pt_i = pt[j][user_i]

                q[song_i][j] += myu_1 * (epsilon_xi * pt_i - lam_2 * q_i)

                pt[j][user_i] += myu_2 * (epsilon_xi * q_i - lam_1 * pt_i)
                # print(f'pt_x->{pt[j][int(matrix_R[i][1])]}')
        eps = eps / len(matrix_R)

    # print(f'epsilon is {eps}')




    sum_squares = 0
    sm = 0;
    for i in range(len(matrix_test)):
        si = int(matrix_test[i][0])
        ui = int(matrix_test[i][1])
        ri = matrix_test[i][2];

        dot_product = dotProduct(q, pt, si, ui)
        tmp = ratingToplamTest[ui] / userSayisiTest[ui]
        diff = round(ri + tmp) - round(dot_product + tmp);

        sum_squares += diff**2;
        sm += abs(diff)
        #print(f'i={i}=>{sum_squares}')

    #
    # px_sum = 0
    # qi_sum = 0
    # for i in range(len(matrix_R)):
    #     for j in range(k):
    #         px_sum += pt[j][int(matrix_R[i][1])]**2
    #         qi_sum += q[int(matrix_R[i][0])][j]**2
    #
    # sum_squares += lam_1 * px_sum + lam_2 * qi_sum
    #
    # now = datetime.datetime.now().time().strftime("%H:%M:%S")
    # print(f'starting calculation at{now}')
    # result.write(f'starting calculation at{now}\n')
    # result.write(now)

    rmse = math.sqrt(sum_squares/len(matrix_test));
    print('RMSE is :')
    print(rmse)
    print(sm / len(matrix_test))

    result.write(f'RMSE is {rmse}')

    now = datetime.datetime.now().time().strftime("%H:%M:%S")
    print(f'finished everything at {now}')
    result.write(f'\nfinished everything at {now}\n')

    result.close()

    # print(sm / len(matrix_R))
    #
    # sum_squares = 0
    # sm = 0;
    # for i in range(len(matrix_R)):
    #     si = int(matrix_R[i][0])
    #     ui = int(matrix_R[i][1])
    #     ri = matrix_R[i][2];
    #
    #     dot_product = dotProduct(q, pt, si, ui)
    #     tmp = ratingToplam[ui] / userSayisi[ui]
    #     diff = round(ri + tmp) - round(dot_product + tmp);
    #
    #     sum_squares += diff**2;
    #     sm += abs(diff)
    #     #print(f'i={i}=>{sum_squares}')
    #
    # rmse = math.sqrt(sum_squares/len(matrix_R));
    # print('RMSE is :')
    # print(rmse)



if __name__ == '__main__':
    main()
