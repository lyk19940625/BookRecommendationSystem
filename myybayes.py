import numpy as np
import math
import kMeans
import word
import NewBook
import pymysql

def getTestset():
    db = pymysql.connect("localhost","root","123456","booksrecommendationsystem",charset="utf8" )


    cursor = db.cursor()
    testset = []
    # SQL 鏌ヨ璇彞
    sql = "SELECT * FROM newbook"
    try:
        # 鎵цSQL璇彞
        cursor.execute(sql)
        # 鑾峰彇鎵�鏈夎褰曞垪琛�
        results = cursor.fetchall()
        for row in results:
            for i in range(3,33):
                testset.append(int(row[i]))
    except:
        print ("Error: unable to fetch data")
    # 鍏抽棴鏁版嵁搴撹繛鎺�
    db.close()
    return testset

def calAverage(dateset):
    a = len(dateset)
    b = len(dateset[0])
    Average = []
    for i in range(b):
        sum = 0
        for j in range(a):
            sum = dateset[j][i] + sum
        average = sum / a
        if average == 0:
            average = 0.0000000000001
        Average.append(average)
    return Average

def calVar(dateset,Average):
    a = len(dateset)
    b = len(dateset[0])
    Var = []
    for i in range(b):
        var = 0
        for j in range(a):
            var = var + math.pow(dateset[j][i] - Average[i],2)
        var = var / a
        if var == 0:
            var = 0.00000000000000001
        Var.append(var)
    return Var

def calPro(testset, Average, Var):
    b = len(testset)
    P = []
    for i in range(b):
        Pro = 1/math.pow(2*Var[i]*math.pi,1/2)*math.exp(-math.pow(testset[i]-Average[i],2)/2*Var[i])
        P.append(Pro)
    return P

def predict(P):
    a = len(P)
    b = len(P[0])
    predict = -1
    rs = -1
    for i in range(a):
        pro = 1
        for j in range(b):
            pro = pro *P[i][j]
        if pro>predict:
            predict = pro
            rs = i
    return rs

def getLabel(rs,labels,countAll):
    label =[]
    j = 0
    for i in countAll:
        if i == rs:
            label.append(labels[j])
        j+=1
    return label

def mainBayes():
    testset = getTestset()
    group,labels = word.getArrays()
    dateset = np.array(group)
    a =dateset.shape[0]
    k = 6
    countAll,count = kMeans.kMeans(dateset, k)
    types = kMeans.mainKMeans2()
    Count =[]
    CountAll = []
    for i in range(len(count)):
        Count.append(count[i])
    for i in range(len(Count)):
        Count[i] = int(Count[i])
    for i in range(len(countAll)):
        CountAll.append(countAll[i])
    for i in range(len(CountAll)):
        CountAll[i] = int(CountAll[i])
    k = 6
    datesetC = kMeans.classifyDateset(dateset,countAll,count,k)
    Average = []
    Var = []
    Pro = []
    for i in range(k):
        Average.append(calAverage(datesetC[i]))
        Var.append(calVar(datesetC[i],Average[i]))
        Pro.append(calPro(testset, Average[i], Var[i]))
    a = len(count)
    rs =predict(Pro)
    label = getLabel(rs,labels,countAll)
    return label

#print(mainBayes())
