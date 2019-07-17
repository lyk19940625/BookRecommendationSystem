from numpy import *
import operator
import NewBook
import word
import pymysql

def createDataSet():
    group = array([[1,1.1],[1,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels




def classify(inX,dataSet,labels,k) :
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis = 1)
    distance = sqDistance ** 0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    knnBooks = []
    knnBooks.append(sortedClassCount[0][0])
    knnBooks.append(sortedClassCount[1][0])
    knnBooks.append(sortedClassCount[2][0])
    return knnBooks

    
